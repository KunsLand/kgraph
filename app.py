#!/usr/bin/env python
import os,logging,traceback
from flask import Flask,jsonify

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(dict(os.environ))

if __name__=="__main__":
	port=int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0',port=port)
