import pandas as pd
import numpy as np
from flask import Flask, abort, jsonify, request
from flask_cors import cross_origin
from sklearn.externals import joblib
from json import dumps

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
@cross_origin()
def make_predict():
    """
     JSON should look like this

    {"firstName":"John",
    "lastName":"Snow",
    "knows":"nothing"}
    """

    # get data, xform to a dict of  pandas series
    data = request.get_json(force=True)

    # this is just a silly example
    firstName = data['firstName']
    lastName = data['lastName']
    knows = data['knows']

    results_dict = dict()
    results_dict['response'] = "Hello " + firstName + " " + lastName + ". I hear that you know " + knows

    # return the json
    return jsonify(results=results_dict)
    
if __name__ == '__main__':
    app.run(port=7000, host='0.0.0.0', debug=True)
    
    