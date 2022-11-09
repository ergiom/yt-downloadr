'''setup for yt_downloadr'''

from setuptools import setup, find_packages

setup(
    name='yt_downloadr',
    version='0.1.0',
    author="Pawel Osuch",
    description="Simple yt-dlp based webapp",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_wtf',
    ]
)
