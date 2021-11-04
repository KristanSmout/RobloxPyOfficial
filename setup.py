from setuptools import setup
import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(name='robloxpy',
    version='1.0.0',
    description='RobloxPy is an object oriented python wrapper for the roblox API.',
    long_description=README,
    long_description_content_type="text/markdown",
    author='KristanSmout & anytarseir67',
    author_email = '',
    url='https://github.com/KristanSmout/RobloxPyOfficial/tree/1.0',
    packages=['robloxpy'],
    install_requires=requirements,
    )