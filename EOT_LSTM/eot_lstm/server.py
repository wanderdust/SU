from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask import request
import os
from preprocessing import Preprocessing
from predict import Predict


# Start app
# Change default location of index.html from ./templates to ./static
app = Flask(__name__,
    static_url_path='',
    template_folder='static')

# Activate CORS.
CORS(app, resources={r'/*': {'origins': 'http://localhost:5000'}})

# Global variables
publicPath = '{}/'.format(os.getcwd())


@app.route("/api/predict/", methods = ['GET', 'POST'])
def root():
    print(request.data)
    utterance = request.data.decode("utf-8") 

    # Instantiate the model
    predict = Predict()
    pred_int, pred_str, prob = predict.predict(utterance)

    return jsonify({'pred_int': pred_int, 'pred_str':pred_str, 'confidence': prob})



if __name__ == '__main__':
  app.run() 


"""
RUN THE SERVER --> FLASK_APP=server.py flask run
"""