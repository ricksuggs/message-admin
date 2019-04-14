from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import ModelSchema
import uuid
from datetime import datetime
Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


class Source(Base):
    __tablename__ = "source"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    environment = Column(String, nullable=False)
    encoding = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)
    messages = relationship("Message", backref="source", lazy="noload")


class Message(Base):
    __tablename__ = "message"
    id = Column(String, primary_key=True, default=generate_uuid)
    source_id = Column(String, ForeignKey("source.id"), nullable=False)
    message = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime)
