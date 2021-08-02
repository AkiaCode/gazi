import setuptools

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gaji",
    version="0.0.0",
    author="Catry",
    description="class-based web framework",
    license="MIT",
    requirements=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akiacode/gaji",
    project_urls={
        "Bug Tracker": "https://github.com/akiacode/gaji/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires=">=3.6",
)
