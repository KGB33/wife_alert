__version__ = "0.1.0"

import os
import asyncio

from flask import Flask
from flask_bootstrap import Bootstrap
from redis import Redis
import rq


queue = rq.Queue("flashing_LED", connection=Redis.from_url("redis://"))


def create_app(config=os.environ["APP_CONFIG"]):
    app = Flask(__name__)
    app.config.from_object(config)

    Bootstrap(app)

    with app.app_context():
        from . import routes

    return app
