@echo off

REM Function to check if Docker is installed
:check_docker
docker --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Docker is not installed. Please install Docker.
    exit /b 1
)
exit /b 0

REM Check if Docker is available
call :check_docker

REM Define the image name
set IMAGE_NAME=sentiment_sense

REM Step 1: Build the Docker image
echo Building the Docker image...
docker build -t %IMAGE_NAME% .

REM Check if the image was built successfully
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to build the Docker image.
    exit /b 1
)

REM Step 2: Run the Docker container
echo Running the Docker container...
docker run -d -p 5001:5001 --name sentiment_sense_container %IMAGE_NAME%

REM Check if the container is running
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to run the Docker container.
    exit /b 1
)

echo Docker container is running and accessible at http://localhost:5001