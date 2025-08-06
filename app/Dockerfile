FROM python:3.13.5-slim

# Working directory
WORKDIR /app

# Copy requirements 
COPY requirements.txt .

# Upgrade pip and install all requirements
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy everything to the docker image
COPY . .
