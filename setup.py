"""
The setup.py file is an essential part of packaging and distribution Python projects.
It is used by setuptools to define the configuration of your project, such as its metadata, dependencies and more ...
"""

from setuptools import find_packages, setup
from typing import List



def get_requirements()->List[str]:
    """

    :return: This function return list of requirements
    """
    requirement_list:List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()     # read lines from the file
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':       # ignore empty lines and -e .
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file not found!")

    return requirement_list

# help us to escape to import hell

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Darius Bahna",
    packages=find_packages(),
    requires=get_requirements(),
)

print(get_requirements())