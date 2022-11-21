# This file defines the Docker container that will contain the Flask app.

# From the source image
FROM python:3.9-slim

# Set the default working directory
WORKDIR /app/

# Copy requirements.txt outside the container
# to /app/ inside the container
COPY requirements.txt /app/

# Install required packages
RUN pip install -r ./requirements.txt

# Copy cwd to app
COPY . /app/

# Expose the container's port 3333
EXPOSE 8080

# When the container starts, run this
ENTRYPOINT python ./app.py