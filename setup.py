import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybomberman", # Replace with your own username
    version="0.0.2",
    author="pybomberman Staff",
    author_email="author@example.com",
    description="Bomberman game and framework implementation in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pybomberman/pybomberman",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
