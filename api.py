#!/usr/bin/python

import bottle
from bottle import get
# from error import email_handler

from data_model import DataClass


app = bottle.Bottle()
#app.error_handler = email_handler
bottle.debug(True)


@app.get('/error')
def get_error():
    return 1/0


data = DataClass()
app.get('/v1/channels_list')(data.get_channels)



if __name__ == '__main__':
    bottle.run(app=app,
               host='0.0.0.0',
               port=8000)
