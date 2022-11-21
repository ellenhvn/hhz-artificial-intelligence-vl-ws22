# How to train and deploy a model locally

# Set-up
`cd Local Deployment`

`pip install -r ./requirements.txt` 

# 1 Run the model training
- A model is created using the training data
- A corresponding file with the columns that were used for the model is also saved

# 2 Start the Flask backend
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
- The ML Flask app is now running in a container

`docker build -t titanic-flask-app:latest .` 

`docker run -p 8080:8080 titanic-flask-app:latest` 

- Now you can correspond with your Docker container app again using

```
curl -i "0.0.0.0:8080/predict?Age=90&Sex_female=0&Sex_male=1&Sex_nan=0&Embarked_C=0&Embarked_S=0&Embarked_Q=1&Embarked_nan=0"
```

from the command line


# Stopping the container

Either stop the container in Docker desktop or
`docker ps` & `docker stop <CONTAINER_ID>`