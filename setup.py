
from setuptools import setup, find_packages

setup(
    name="cloud-intelligent-manager",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "numpy>=1.20.0",
    ],
    author="",
    author_email="",
    description="Cloud service implementing FastAPI architecture",
    keywords="cloud-intelligent-manager, python",
    url="",
)
