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
    ],
)