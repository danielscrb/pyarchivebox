from setuptools import setup, find_packages

setup(
    name="pyarchivebox",
    version="0.0.1",
    description="A simpler way to interact with your archivebox server via python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/danielscrb/pyarchivebox",
    author="danielscrb",
    author_email="danielscrb@casasc.org",
    license="MIT-Modified",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "requests>=2.32.3",
        "selectolax>=0.3.27"
    ],
    python_requires=">=3.10"
)