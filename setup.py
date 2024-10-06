from distutils.core import setup

setup(
    name="timeutilities",
    version="1.2",
    url="https://github.com/astraldev/timeutilities",
    license="MIT",
    author="astraldev",
    author_email="ekureedem480@gmail.com",
    description="Minimal utilities for time managements and manipulation",
    py_modules=["timeutilities"],
    long_description=str(open("README.md").read()),
    long_description_content_type="text/markdown",
    python_requires=">=3",
)
