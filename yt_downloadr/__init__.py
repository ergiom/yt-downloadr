'''Core flask setup'''

from flask import Flask
app = Flask(__name__)
app.config['DOWNLOAD_DIR'] = './downloads'
app.config.from_prefixed_env()

if not app.secret_key:
    raise RuntimeError("secret key not set")

import yt_downloadr.routes
