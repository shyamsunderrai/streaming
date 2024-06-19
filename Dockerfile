# Base image for Python Container
# FROM python:3.10.14-alpine
  FROM python:3.9-slim

# Setting working directory
WORKDIR /app

# Copy application file requirements file to / folder 
COPY app.py /app

# Install the requirements for the package
RUN pip install --upgrade pip
RUN pip install faker Flask 
RUN pip install geopy


# Exposing the port to run the application on
EXPOSE 5000

# Starting point for the application
CMD ["python", "app.py"]

