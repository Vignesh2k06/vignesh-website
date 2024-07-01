from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from models.baseModel import BaseModel


class Images(BaseModel):
    __tablename__ = 'images'
    __table_args__ = {"schema": 'personal_website'}

    mapping_id = Column(UUID(as_uuid=True), primary_key=True,
                        server_default=func.uuid_generate_v4())
    project_code = Column(String(length=50), ForeignKey(
        "personal_website.projects.project_code"), nullable=False)
    src_path = Column(String(length=100), nullable=False)
    alt_text = Column(String(length=50), nullable=True)

