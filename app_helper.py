import re
from docx import Document

from models.project_type import ProjectType
from models.projects import Projects
from models.images import Images


def get_project_highlights(session):
    """Method to get the highlight project list"""
    project_highlights = (
        session.query(
            Projects.project_code,
            Projects.project_name,
            Projects.project_description,
            Projects.highlights,
            Images.project_code,
            Images.src_path,
            Images.alt_text
        )
        .join(Images, Projects.project_code == Images.project_code)
        .filter(Projects.highlights == "true")
    ).all()

    highlights = []
    for project in project_highlights:
        response = {
            'id': project.project_code,
            "title": project.project_name,
            "description": project.project_description,
            "image_src": "static/" + project.src_path,
            "alt_text": project.alt_text
        }
        highlights.append(response.copy())

    return highlights


def get_list_of_projects(session):
    """Method to get the list of projects"""
    project_highlights = (
        session.query(
            Projects.project_code,
            Projects.project_name,
            Projects.project_description,
            Projects.highlights,
            Projects.page_url_slug

        )
        .order_by(Projects.project_name.desc())
    ).all()

    project_list = []
    for project in project_highlights:
        response = {
            'project_code': project.project_code.lower(),
            "title": project.project_name,
            "description": project.project_description,
            "page_url_slug": project.page_url_slug
        }
        project_list.append(response.copy())

    return project_list



def get_project_by_url(session, page_url_slug):
    """Method to get a project by id"""
    project = (
        session.query(
            Projects.project_code,
            Projects.project_name,
            Projects.project_description,
            Projects.page_url_slug,
            Projects.highlights,
            Projects.attributes.label("project_attributes"),
            Images.project_code,
            Images.src_path,
            Images.alt_text
        )
        .join(Images, Projects.project_code == Images.project_code)
        .filter(Projects.page_url_slug == page_url_slug)
    ).one()

    response = {
        'id': project.project_code,
        "title": project.project_name,
        "page_url_slug": project.page_url_slug,
        "description": project.project_description,
        "image_src": project.src_path,
        "alt_text": project.alt_text
    }

    if project.project_attributes:
        response.update(project.project_attributes)

    return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'doc', 'docx'}

def sanitize_filename(filename):
    return ''.join(c for c in filename if c.isalnum() or c in ('.', '_')).rstrip()

def is_heading(paragraph):
    for run in paragraph.runs:
        if run.bold:
            return True
    return False

def is_list_item(para):

    if para.style.name in ['List Paragraph', 'List Bullet', 'List Number'] or para.text.startswith("-"):
        return True
    return False

def convert_to_html(filepath, form={}):

    is_list = False
    doc = Document(filepath)
    html_content = '<html>\n<body>\n'

    if form != {}:
        heading_tag = form["headingRadios"]
        lists_tag = form["listsRadios"]

    # Process each paragraph in the document
    for para in doc.paragraphs:
        text = para.text.strip()

        if text:
            if is_heading(para):
                if is_list:
                    html_content += f' </{lists_tag}>\n'
                    is_list = False
                html_content += f'<{heading_tag}>{text}</{heading_tag}>\n'
            elif is_list_item(para):
                if not is_list:
                    html_content += f'<{lists_tag}>\n'
                    is_list = True
                html_content += f'<li>{text}</li>\n'
            else:
                if is_list:
                    html_content += f'  </{lists_tag}>\n'
                    is_list = False
                html_content += f'<p>{text}</p>\n'

    # Close any open list tags
    if is_list:
        html_content += f' </{lists_tag}>\n'

    # Close the HTML tags
    html_content += '</body>\n</html>'

    return html_content
