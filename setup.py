from setuptools import setup

setup(
    name='rest_test',
    packages=['rest_test'],
    include_package_data=True,
    install_requires=[
        'flask',
        'requests',
        'pytest',
    ],
)