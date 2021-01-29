import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()
setup(
    name="arg_parser",
    version="2.0.1",
    description="Parse commands from the terminal to simple functions",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/NightKylo/Python-Arg-Parser",
    author="Marius K. / cracksii",
    license="Apache",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["arg_parser"],
    include_package_data=True,
)