from setuptools import setup

setup(
    name='http_quiz',
    packages=['http_quiz'],
    include_package_data=True,
    install_requires=[
        'flask==0.12.2',
        'pytest==3.4.2',
        'pytest-cov==2.5.1',
        'pylint==1.8.4',
        'mypy==0.580',
        'Flask-Testing==0.7.1',
        'flask-sqlalchemy==2.3.2',
        'flask-migrate==2.1.1',
        'flask-jwt==0.3.2',
        'Flask-Mail==0.9.1',
        'Flask-Bcrypt==0.7.1',
        'cerberus==1.2',
        'psycopg2-binary==2.7.4',
        'coveralls==1.3.0',
    ],
)
