# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="python_translate",
    version="1.0.0",
    author="Adam Zieliński",
    author_email="adam@sf2.guru",
    packages=["python_translate"],
    include_package_data=True,
    url="http://pypi.python.org/pypi/python_translate_v100/",

    license="LICENSE",
    description="Non-gettext translations for python.",

    # Dependent packages (distributions)
    install_requires=[
        "PyYAML==3.11",
        "codegen==1.0"
    ],
)