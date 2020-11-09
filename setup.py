from setuptools import setup
setup(install_requires=[i.strip() for i in open("requirements.txt").readlines()])