from setuptools import setup

setup(
    name='rest_test',
    packages=['rest_test'],
    include_package_data=True,
    install_requires=[
        'flask==0.12.2',
        'requests==2.18.4',
        'pytest==3.4.2',
        'pytest-cov==2.5.1',
        'pylint==1.8.4',
        'mypy==0.580',
        'Flask-Testing==0.7.1',
        'flask-injector==0.10.1',
        'flask-sqlalchemy==2.3.2',
        'flask-migrate==2.1.1',
        'flask-security==3.0.0',
        'flask-jwt==0.3.2',
        'psycopg2==2.7.4',
    ],
)