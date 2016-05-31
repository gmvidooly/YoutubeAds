import sys, os, bottle

#sys.path = ['/home/vishnu/Workspace/YouTubeAd/YoutubeAdsApi/']

sys.path.insert(0,"/home/vishnu/Workspace/YouTubeAd/YoutubeAdsApi/")
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

#import api         # This loads the REST framework that you have implemented as apiserver.py (The file that handles get/post requests)
from data_model import DataClass

# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
#application = bottle.default_app()
#app = bottle.Bottle()

#from api import app as application

#data = DataClass()
#app.get('/channels_list')(data.get_channels)

#bottle.run(app, host='0.0.0.0', port=80)

import bottle
from bottle import route , get
#import hello
application = bottle.default_app()

@route('/hello')
def hello():
    return "Hello World!"

data = DataClass()
#@route('/channels_list')
#def channels_list():
#    return data.get_channels
application.get('/channels_list')(data.get_channels)
