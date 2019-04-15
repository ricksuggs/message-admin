Message Admin REST

This project was created with Ubuntu 18.04.2 / Python 3.7.3 and has not been tested with any other versions.

Run the following commands in order to start the api:
- Install virtual environment: `python -m venv .venv`
- Activate virtual environment: `source .venv/bin/activate`
- Install dependencies: `pip3 install --editable .`
- Build project: `python setup.py develop`
- Run tests: `python setup.py pytest`
- Run REST api: `python api/run.py`