'''setup for yt_downloadr'''

from setuptools import setup

setup(
    name='yt_downloadr',
    packages=['yt_downloadr'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_wtf',
    ]
)
