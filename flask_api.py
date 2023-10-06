import numpy as np
from flask import Flask, abort, jsonify, request
import cPickle as pickle

model_integrador = pickle.load(open(".pkl","rb"))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():
    #checking errors section
    data = request.get_json(force=True)
    #convert json to numpy array
    predict_request = [data['sl'],data['sw'],data['pl'],data['pw']]
    predict_request = np.array(predict_request)
    #np array goes to rand forest predictio pops
    y_hat = my_random_forest.predict(predict_request)
    #return predic
    output 0 [y_hat[0]]
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 9000,debug = True)