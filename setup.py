"""
    author: siddhi.bajracharya
    email: siddhikiran.bajracharya@gmail.com
"""

from setuptools import setup, find_packages

setup(
    name='medical_image_converter',
    version='0.0.1',
    description='Converts medical image (.ima) to .jpg',
    author='siddhi.bajracharya',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'pydicom',
        'concurrent.futures'
    ],
    python_requires='>=3.6',
)

