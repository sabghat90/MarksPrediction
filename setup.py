from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(path: str) -> List[str]:
    """Get requirements from file."""
    requirements = []
    with open(path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="Marks Prediction",
    version='0.0.1',
    description="Marks Prediction using Linear Regression",
    author="Sabghat Ullah",
    author_email="sabghat90@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    license='MIT'
)
