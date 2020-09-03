__version__ = "0.1.0"

import os

from flask import Flask


def create_app(config=os.environ["APP_CONFIG"]):
    app = Flask(__name__)
    app.config.from_object(config)

    return app
