# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Install git and cleanup in one layer for efficiency
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# If .env does not exist, copy the .env.example file to .env
# This command ensures there's always an .env file if .env.example exists
RUN if [ ! -f .env ]; then cp .env.example .env; fi

# Non-root user setup: create a user 'camoo' and switch to it
RUN adduser --disabled-password --gecos "" camoo
USER camoo

# Expose the port your app will listen on (default for many web apps is 8080)
EXPOSE 5001

# Define the command to run your application
CMD ["python", "app.py"]