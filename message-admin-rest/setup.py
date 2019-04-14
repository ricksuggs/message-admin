from setuptools import setup

setup(
    name="message-admin-rest",
    packages=["api"],
    install_requires=[
        "flask",
        "flask-restful",
        "flask-sqlalchemy",
        "sqlalchemy-utils",
        "marshmallow-sqlalchemy",
        "flask_marshmallow"
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest_mockito", "pytest-flask"],
)
