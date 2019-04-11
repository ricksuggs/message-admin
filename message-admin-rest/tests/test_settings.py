from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from api.settings import DOMAIN
from pathlib import Path

DEBUG = True
SQLALCHEMY_DATABASE_URI = (
    f"sqlite:////{Path.cwd()}/db.test.sqlite"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESOURCE_METHODS = ["GET", "POST", "DELETE"]

# The following two lines will output the SQL statements executed by
# SQLAlchemy. This is useful while debugging and in development, but is turned
# off by default.
# --------
# SQLALCHEMY_ECHO = True
# SQLALCHEMY_RECORD_QUERIES = True

# The default schema is generated using DomainConfig:
DOMAIN = DOMAIN