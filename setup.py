from setuptools import setup

setup(
    name='example-fastapi-app',
    version='0.0.1',
    author='Manokhin_MS',
    author_email='wingrull@gmail.com',
    description='simple FastApi application',
    install_requires=[
        'fastapi',
        'uvicorn',
        'SQLAlchemy',
        'pytest',
        'requests'
    ],
    scripts=['app/main.py']
)
