"""
Model inference in Flask

Based on https://github.com/amirziai/sklearnflask/ & https://github.com/chrisalbon/sklearn-flask-docker
"""


import os
import joblib
from flask import Flask, jsonify, request

model_directory = str(os.getcwd()) + '/model'
model_file_name = '%s/model.pkl' % model_directory
model_columns_file_name = '%s/model_columns.pkl' % model_directory


app = Flask(__name__)

model_columns = joblib.load(model_columns_file_name)
trained_model = joblib.load(model_file_name)
                

# Create an API end point
@app.route('/predict', methods=['GET'])
def get_prediction(trained_model=trained_model):
    # Age
    age = int(request.args.get('Age'))
    # Sex
    sex_f = request.args.get('Sex_female')
    sex_m = request.args.get('Sex_male')
    sex_nan = request.args.get('Sex_nan')
    # Embarked
    embarked_c = request.args.get('Embarked_C')
    embarked_q = request.args.get('Embarked_Q')
    embarked_s = request.args.get('Embarked_S')
    embarked_nan = request.args.get('Embarked_nan')

    # The features of the observation to predict
    features = [age, sex_f, sex_m, sex_nan, 
                embarked_c, embarked_q, embarked_s, embarked_nan]

    # Predict the class using the model
    predicted_class = trained_model.predict([features])

    # Return a json object containing the features and prediction
    return jsonify(feature_names=model_columns,features=features, predicted_class=predicted_class.tolist())  

if __name__ == '__main__':
    try:
        clf = joblib.load(model_file_name)
        print('model loaded')
        model_columns = joblib.load(model_columns_file_name)
        print('model columns loaded')
        print(model_columns)

    except Exception as e:
        print('No model here')
        print('Train first')
        print(str(e))
        clf = None

    app.run(port=8080, host='0.0.0.0')
