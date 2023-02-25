# Set the syntax version for this Dockerfile
# This enables the use of a newer syntax version if available
# More info: https://docs.docker.com/engine/reference/builder/#syntax
# syntax=docker/dockerfile:1

# Use the Python 3.11 image as the base image
FROM python:3.11

# Sets the maintainer of the project
MAINTAINER FIRST_NAME LAST_NAME "YOUR_EMAIL@gmail.com"

# Copy the contents of the repository into the container's root directory
COPY . /

# Install the project's dependencies
RUN pip install -e .

# Set the default command to run when the container starts
# In this case, run the "main.py" script using the Python interpreter
CMD [ "python", "src/main.py" ]

