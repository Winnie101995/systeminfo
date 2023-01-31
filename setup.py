from setuptools import setup, find_packages

setup(
    name='systeminfo',
    version='0.0.1',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.10"'
    ],

    packages=find_packages(include=['systeminfo, systeminfo.*'])
)
