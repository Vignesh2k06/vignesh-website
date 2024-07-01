from sqlalchemy import  Column, String

from models.baseModel import BaseModel


class ProjectType(BaseModel):
    __tablename__ = 'project_type'
    __table_args__ = {"schema": 'personal_website'}

    project_type_id = Column(String(length=20), primary_key=True)
    description = Column(String(length=50), nullable=True)
