#!/usr/bin/env python
import os
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name="ibl-ai-chatgpt-langchain",
    version="1.0.0",
    description="ChatGPT LLM for langchain by IBL",
    author="IBL",
    author_email="info@ibleducation.com",
    url="https://github.com/ibleducation/ibl-ai-chatgpt-langchain",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    install_requires=[
        "langchain",
        "python-dotenv",
        "chatgptpy",
        "pydantic",
                      ],
)
