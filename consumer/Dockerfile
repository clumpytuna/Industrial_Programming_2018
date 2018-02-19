# Use an official Python runtime as a parent image
FROM python:3.4-slim

# Set the working directory to /app
WORKDIR /consumer

# Copy the current directory contents into the container at /app
ADD . /consumer

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "consumer.py"]
