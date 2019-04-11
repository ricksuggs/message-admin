from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from api.models import Source, Message
from pathlib import Path
import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = (
    f"sqlite:////{Path.cwd()}/db.sqlite"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESOURCE_METHODS = ["GET", "POST", "DELETE"]

SQLALCHEMY_ECHO = True
SQLALCHEMY_RECORD_QUERIES = True

DOMAIN = DomainConfig(
    {
        "source": ResourceConfig(Source),
        "message": ResourceConfig(Message),
        "source_message": ResourceConfig(Message),
    },
    related_resources={
        (Source, "messages"): "message"
    },
).render()

DOMAIN["source_message"].update({"url": "source/<regex('.{36}'):source_id>/message"})

