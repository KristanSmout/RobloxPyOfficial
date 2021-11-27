from setuptools import setup

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(name='robloxpy',
    version='0.2.21',
    description='RobloxPy is a python API wrapper for roblox. This allows for quick and easy integration of these API\'s into a python project.',
    author='KristanSmout & anytarseir67',
    url='https://github.com/KristanSmout/RobloxPyOfficial/',
    packages=['robloxpy'],
    install_requires=requirements,
    )