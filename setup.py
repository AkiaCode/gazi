import setuptools

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gazi",
    version="0.1.5",
    author="Catry",
    description="A lightweight, class-based, easy-to-use ASGI framework",
    license="MIT",
    requirements=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akiacode/gazi",
    project_urls={
        "Bug Tracker": "https://github.com/akiacode/gazi/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=["tests", "examples"]),
    python_requires=">=3.6",
)
