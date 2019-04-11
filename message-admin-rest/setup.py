from setuptools import setup

setup(
    name="message-admin-rest",
    packages=["api"],
    install_requires=[
        "flask==0.12",
        "eve==0.7.10",
        "eve-sqlalchemy==0.7.0",
        "itsdangerous==0.24",
        "werkzeug==0.11.15",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest_mockito"],
)
