# Use official Python base image
FROM python:3.11-slim

# Install OpenJDK and curl
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    curl \
    && apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy all project files to the container
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by the FastAPI server
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "Endpoint_Java:app", "--host", "0.0.0.0", "--port", "8000"]
