# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# 定义构建参数
ARG LOGS_BUCKET_NAME

# 在构建过程中使用构建参数
RUN gcloud builds submit --config=cloudbuild.yaml --project=python-news-crawler --substitutions=_LOGS_BUCKET_NAME=${LOGS_BUCKET_NAME}

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app