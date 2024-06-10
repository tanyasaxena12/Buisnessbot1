# Use the official Python image from the Docker Hub
FROM --platform=linux/amd64 python:3.9-slim

# Set environment variables
ENV PORT=8080
ENV STREAMLIT_SERVER_PORT=8080

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py", "--server.port", "8080", "--server.headless", "true"]
