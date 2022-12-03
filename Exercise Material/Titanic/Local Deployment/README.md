# How to train and deploy a model locally

# Set-up
`cd Local Deployment`

`pip install -r ./requirements.txt` 

# 1 Run the model training
- Run in your activated conda environment
```
python3 train.py
```
- A model is created using the training data in model/model.pkl
- A corresponding file with the columns that were used for the model is also saved in model/model_columns.pkl

# 2 Start the Flask backend
```
python3 app.py
```

- Flask is now running locally and uses the trained model from step 1
- Currently there is no front-end, so you can submit predictions in 2 ways locally

```
http://0.0.0.0:8080/predict?Age=30&Sex_female=0&Sex_male=1&Sex_nan=0&Embarked_C=0&Embarked_S=0&Embarked_Q=1&Embarked_nan=0
```

This will directly embed the variables in the URL; you can change them accordingly.
Note that the variables are already encoded for categorical features. This, together with a UI would be something for further development.

You could also call the model using CURL, e.g. by pasting this URL in your terminal

```
curl -i "0.0.0.0:8080/predict?Age=30&Sex_female=0&Sex_male=1&Sex_nan=0&Embarked_C=0&Embarked_S=0&Embarked_Q=1&Embarked_nan=0"
```

# 3 Start the Docker container with the app

- First, make sure Docker is running on your local machine (get Docker Desktop here: https://docs.docker.com/get-docker/ and then install and start the application)

- Then, start the container with your model inference application by typing the following commands in your terminal: 

`docker build -t titanic-flask-app:latest .` 

This creates the container. Next, you start the container by running: 

`docker run -p 8080:8080 titanic-flask-app:latest` 

- The ML Flask app is now running in a container

- Now you can correspond with your Docker container app again using

```
curl -i "0.0.0.0:8080/predict?Age=90&Sex_female=0&Sex_male=1&Sex_nan=0&Embarked_C=0&Embarked_S=0&Embarked_Q=1&Embarked_nan=0"
```

from the command line


# Stopping the container

Either stop the container in Docker desktop or view listed containers with and then stop it by it's container ID 
`docker ps` & `docker stop <CONTAINER_ID>`
