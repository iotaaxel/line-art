#!/usr/bin/env python3
"""Setup script for Line-Art"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="line-art",
    version="1.0.0",
    author="iotaaxel",
    description="A beautiful ASCII art line drawing tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iotaaxel/line-art",
    py_modules=["main"],
    scripts=["main.py", "gallery.py", "example.py", "demo.py"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Artistic Software",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.6",
    keywords="ascii art, line drawing, graphics, terminal, cli",
)

