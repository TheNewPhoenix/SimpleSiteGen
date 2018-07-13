from setuptools import setup, find_packages

with open('README.rst') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

setup(
    name='simplesite',
    version='0.1.0',
    description='Simple static site generator',
    long_description=readme,
    author='Jacob Doll',
    author_email='99jdoll@gmail.com',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points = {
        'console_scripts': [
            'simplesite = simplesite.cli:main',
        ]
    }
)