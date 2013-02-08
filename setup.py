from setuptools import setup

setup(
    name="virgo",
    version="0.1.3",
    author="hit9",
    author_email="nz2324@126.com",
    description=("Tiny Python ORM for MySQL"),
    license="BSD",
    keywords="ORM MySQL Python tiny database virgo",
    url="https://virgo.readthedocs.org/",
    py_modules=['virgo'],
    install_requires = ['MySQL-python'],
)
