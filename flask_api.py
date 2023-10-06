import numpy as np
from flask import Flask, abort, jsonify, request
import pickle as pickle

model_integrador = pickle.load(open(r"D:\pythonavanzado\proyecto_integrador_dmonteon\pca_model_integrador.plk","rb"))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():
    #checking errors section
    data = request.get_json(force=True)
    #convert json to numpy array
    predict_request = [data['sl'],data['sw'],data['pl'],data['pw']]
    predict_request = np.array(predict_request)
    #np array goes to rand forest predictio pops
    y_hat = model_integrador.predict(predict_request)
    #return predic
    output = [y_hat[0]]
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 9000,debug = True)