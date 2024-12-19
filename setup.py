from setuptools import setup, find_packages

setup(
    name="rtdvscodetheme",
    version="0.0.0",
    description="Python library for a visual studio code high contrast looking read the docs theme",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Unlisted_dev",
    #author_email="your_email@example.com",
    url="https://github.com/Unlisted27/basicrpg",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
     ],
    install_requires=[
        "pygments>=2.0",
    ],
    python_requires=">=3.6",
)