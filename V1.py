from sys import argv

import bottle
from bottle import *
bottle.debug(True)

@route("/")
def index():
    return """
    <h1>Verkefni 1</h1>
    <a href="/about">About</a>
    <a href="/bio">Bio</a>
    <a href="/pic">Pictures</a>
"""

@route("/about")
def siggi():
    return "Hér er sögn um mig"

@route("/bio")
def siggi():
    return "Hér er Biograph um mig"

@route("/pic")
def siggi():
    return "Hér er ljósmynd af mér"

#run(host="localhost", port=8080, debug=True)

bottle.run(host="0.0.0.0",port=argv[1])
