from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid

Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


class Source(Base):
    __tablename__ = "source"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    environment = Column(String)
    encoding = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    messages = relationship("Message", backref="source", lazy="noload")


class Message(Base):
    __tablename__ = "message"
    id = Column(String, primary_key=True, default=generate_uuid)
    source_id = Column(String, ForeignKey("source.id"))
    message = Column(String)
    status = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
