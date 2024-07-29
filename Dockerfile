# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    pkg-config \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the Pipfile and Pipfile.lock first to leverage Docker cache
COPY Pipfile Pipfile.lock ./

# Install the dependencies
RUN pip install pipenv

# Install the dependencies using cache
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code into the container
COPY . .

# Set PIPENV_VERBOSITY to enable debug mode
ENV PIPENV_VERBOSITY=2

# Set PYTHONPATH to include the app directory
ENV PYTHONPATH=/app

# Expose the port that the Flask app runs on
EXPOSE 5001

ENTRYPOINT ["pipenv", "run", "python", "app/app.py"]