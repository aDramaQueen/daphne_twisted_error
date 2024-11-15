# Dockerfile
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /daphne-app

# Copy the entire project, except ignored files (@see ".dockerignore")
COPY . /daphne-app/

# Create necessary directories & install dependencies
RUN mkdir -p /run/daphne \
    && mkdir -p /var/log/daphne \
    && pip install --no-cache-dir -r requirements.txt

# DB migrations
RUN python manage.py makemigrations \
    && python manage.py migrate
