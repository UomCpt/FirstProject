# Use a Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y build-essential

# Copy both main.py and script.py to the container
COPY main.py /app/
COPY script.py /app/
COPY wow.cpp /app/wow.cpp

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]