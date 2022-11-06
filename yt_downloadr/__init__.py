'''
    Exceptions
    ----------
    YtDownloadrError
        Core exception for yt_downloadr application
'''

from flask import Flask
app = Flask(__name__)

import yt_downloadr.routes


class YtDownloadrError(RuntimeError):
    '''Base YtDownloadrError'''
