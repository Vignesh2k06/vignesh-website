import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

from database import DB
from app_helper import  get_project_highlights, get_list_of_projects, get_project_by_url, allowed_file, sanitize_filename, convert_to_html

app = Flask(__name__)
app.static_folder = 'static'

load_dotenv()
app.config.from_pyfile('settings.py')

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = DB(
    user=app.config["DATBASE_USER"],
    password=app.config["DATABASE_PASSWORD"],
    host=app.config["DATABASE_HOST"]
)

Session = db.get_session()
session = Session()

@app.route("/")
def home_page():
    project_highlights = get_project_highlights(session)
    return render_template('home.html',
                           projects=project_highlights)

@app.route("/projects")
def list_projects():
    project_list = get_list_of_projects(session)
    return render_template('list_projects.html',
                           projects=project_list)


@app.route("/projects/<page_url_slug>")
def get_project(page_url_slug):
    project_details = get_project_by_url(session, page_url_slug)
    return render_template('project.html',
                           project=project_details)

@app.route('/upload', methods=['POST'])
def upload_file():

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        filename = sanitize_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        html_content = convert_to_html(filepath, request.form)
        return html_content
    else:
        return 'File type not allowed'


session.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
