from setuptools import setup,find_packages
from typing import List


# Declaring variables for setup functions
PROJECT_NAME ="housing-prediction"
VERSION ="0.0.3"
AUTHOR ="chiranjeevi"
DESCRIPTION ="Predicting cost of house"
PACKAGES =find_packages()
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    This function returns list of libraries which are mentioned in requirements.txt
    file
    """
    with open(REQUIREMENT_FILE_NAME) as requriement_file:
        return requriement_file.readlines().pop()

setup(name=PROJECT_NAME,
      version=VERSION,
      author=AUTHOR,
      description=DESCRIPTION,
      packages=PACKAGES,
      install_requires=get_requirements_list())

