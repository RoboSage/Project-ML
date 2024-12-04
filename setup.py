from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function will read the requirements file and return a list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        # Read all lines from the file
        requirements = file_obj.readlines()

        # Clean up the lines by removing newlines and any unwanted entries
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove the "-e ." entry if it exists
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='Project-ML',
    packages=find_packages(),
    version='0.0.1',
    description='A project for Machine Learning',
    author='Rohit Raj',
    author_email='rohit10.gm@gmail.com',
    install_requires=get_requirements('requirements.txt'),
)
