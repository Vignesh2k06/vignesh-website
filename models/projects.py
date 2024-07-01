from sqlalchemy import JSON, TIMESTAMP, Column, ForeignKey, String, Boolean
from sqlalchemy.sql import func

from models.baseModel import BaseModel


class Projects(BaseModel):
    __tablename__ = 'projects'
    __table_args__ = {"schema": 'personal_website'}

    project_code = Column(String(length=50), primary_key=True)
    project_name = Column(String(length=100), nullable=False)
    project_description = Column(String(length=500), nullable=True)
    project_type_id = Column(String(length=20), ForeignKey(
        "personal_website.project_type.project_type_id"), nullable=False)
    attributes = Column(JSON, nullable=False)
    highlights = Column(Boolean, nullable = True)
    page_url_slug = Column(String(length=50), nullable=False)
    created_at = Column(TIMESTAMP(timezone=False),
                        server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=False),
                        server_default=func.now(), nullable=False)
