from setuptools import setup
import pathlib
import os

here = pathlib.Path(__file__).parent
os.chdir(here)

setup(
  name="timeutilities",
  version="1.1",
  license="GNU GPL 3",
  url="http://astraldev.github.io/timeutilities",
  description="Time handling and manipulation",
  long_description=str(open('README.md').read()),
  long_description_content_type="text/markdown",
  author="AstralDev",
  author_email="ekureedem480@gmail.com",
  python_requires='>=3',
  install_requires=["niceprint"],
  py_modules=["timeutilities"]
)
