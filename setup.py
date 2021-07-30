from setuptools import setup

setup(
    name='my_sklearn_pkg_test',
    version='0.0.1',
    packages=['my_sklearn_pkg'], # nom du dossier qui contient le init
    scripts = ['scripts/display']
)