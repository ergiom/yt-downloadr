'''Core flask setup'''

from flask import Flask
app = Flask(__name__)
app.config.from_prefixed_env()
app.config['WTF_CSRF_ENABLED'] = False

if not app.secret_key:
    raise RuntimeError("secret key not set")

import yt_downloadr.routes
