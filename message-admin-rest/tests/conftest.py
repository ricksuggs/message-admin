import pytest
from api import run
from pathlib import Path


@pytest.fixture
def app():
    run.app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"sqlite:////{Path.cwd()}/db.test.sqlite"
    return run.app
