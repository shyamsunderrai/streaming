# Base image for Python Container
# FROM python:3.10.14-alpine
  FROM python:3.9-slim

# Setting working directory
WORKDIR /app

# Copy application file requirements file to / folder 
COPY cp-consumer.py /app
COPY requirements.txt /app

# Install the requirements for the package
RUN pip install --upgrade pip
RUN pip install -U -r requirements.txt


# Starting point for the application
CMD ["python", "cp-consumer.py"]

