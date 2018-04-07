from setuptools import setup

setup(
    name='rest_test',
    packages=['rest_test'],
    include_package_data=True,
    install_requires=[
        'flask==0.12.2',
        'requests==2.18.4',
        'pytest==3.4.2',
        'Flask-Testing==0.7.1',
        'flask-sqlalchemy==2.3.2',
        'flask-migrate==2.1.1',
        'flask-security==3.0.0',
        'psycopg2==2.7.4',
        'alembic==0.9.9',
    ],
)