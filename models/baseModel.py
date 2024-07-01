""" base model"""
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    """base model"""
    __abstract__ = True

    def to_dict(self):
        """to dict"""
        return {item.name: getattr(self, item.name) for item in self.__table__.columns}
