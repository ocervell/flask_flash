#!/usr/bin/env python
from flask_flash import Flash
from resources import User, Index
import logging

log = logging.getLogger('flask_flash')
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

flash = Flash(
    resources=[
        User,
        Index
    ])

if __name__ == '__main__':
    flash.manager.run()
