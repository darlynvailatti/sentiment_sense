#!/bin/bash

# Function to check if Docker is installed
check_docker() {
    if ! command -v docker &> /dev/null
    then
        echo "Docker is not installed. Please install Docker."
        exit 1
    fi
}

# Check if Docker is available
check_docker

# Define the image name
IMAGE_NAME="sentiment_sense"
CONTAINER_NAME="sentiment_sense_container"
PORT=5001

# Step 1: Build the Docker image
echo "Building the Docker image..."
docker build -t $IMAGE_NAME .

# Check if the image was built successfully
if [ $? -ne 0 ]; then
    echo "Failed to build the Docker image."
    exit 1
fi

# Step 2: Run the Docker container
echo "Running the Docker container..."
docker container rm $CONTAINER_NAME
docker run -p $PORT:$PORT --name $CONTAINER_NAME $IMAGE_NAME

# Check if the container is running
if [ $? -ne 0 ]; then
    echo "Failed to run the Docker container."
    exit 1
fi