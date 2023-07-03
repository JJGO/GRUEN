from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="gruen",
    version="0.1",
    description="GRUEN for Evaluating Linguistic Quality of Generated Text",
    author="JJGO",
    install_requires=requirements,
    packages=find_packages(),
)
