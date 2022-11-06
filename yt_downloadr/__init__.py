'''Core flask setup'''

from flask import Flask
app = Flask(__name__)

import yt_downloadr.routes
