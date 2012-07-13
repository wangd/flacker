# -*- coding: utf-8 -*-
"""
    flacker
    ~~~~~~~

    A BitTorrent tracker written in Python with Flask.

    :copyright: 2012 by Christoph Heer <Christoph.Heer@googlemail.com
    :license: BSD, see LICENSE for more details.
"""

import os

from flask import Flask
from .redis import redis

from .tracker import tracker
from .frontend import frontend

def create_app(config=None):
    app = Flask("flacker")
    if config is not None:
        app.config.from_pyfile(os.path.join(os.getcwd(), config))
    elif 'FLACKER_CONFIG' in os.environ:
        app.config.from_envvar('FLACKER_CONFIG')
    
    redis.init_app(app)
    app.register_blueprint(tracker)
    app.register_blueprint(frontend)

    return app