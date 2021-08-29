from setuptools import setup

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(name='robloxpy',
    version='1.0.0.a1',
    description='RobloxPy is an object oriented python wrapper for the roblox API.',
    author='KristanSmout & anytarseir67',
    author_email = '',
    url='https://github.com/KristanSmout/RobloxPyOfficial/tree/1.0',
    packages=['robloxpy'],
    install_requires=requirements,
    )