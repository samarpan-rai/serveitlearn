#!/usr/bin/env python
import pathlib

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

HERE = pathlib.Path(__file__).parent
INSTALL_REQUIRES = (HERE / "requirements.txt").read_text().splitlines()

setup(
    author="Samarpan Rai",
    author_email="samarpan-rai@live.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="Send a POST request to infer your ML model with FastAPI",
    install_requires=INSTALL_REQUIRES,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"serveitlearn": ["py.typed"]},
    include_package_data=True,
    keywords="serveitlearn",
    name="serveitlearn",
    package_dir={'': "src"},
    packages=find_packages(where="src"),
    setup_requires=[INSTALL_REQUIRES],
    url="https://github.com/samarpan-rai/serveitlearn",
    version="0.1.1",
    zip_safe=False,
)
