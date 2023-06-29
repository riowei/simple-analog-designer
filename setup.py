from setuptools import setup, find_packages

setup(
    name="simple-analog-designer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies in this list
        # For example: 
        # "numpy >= 1.20.0",
        # "scipy >= 1.6.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A lightweight, easy-to-use tool for designing and laying out analog circuits.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/simple-analog-designer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
