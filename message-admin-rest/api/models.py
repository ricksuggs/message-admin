from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Source(Base):
    __tablename__ = "source"
    id = Column(String, primary_key=True)
    name = Column(String)
    environment = Column(String)
    encoding = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    messages = relationship("Message", backref="source", lazy='noload')


class Message(Base):
    __tablename__ = "message"
    id = Column(String, primary_key=True)
    source_id = Column(String, ForeignKey("source.id"))
    message = Column(String)
    status = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
