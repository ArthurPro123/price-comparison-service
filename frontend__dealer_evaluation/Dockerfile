# Use the official Python 3.11 slim image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy your static files
COPY html /app/html

# Expose port 8000
EXPOSE 8000

# Start a simple Python HTTP server
CMD ["python", "-m", "http.server", "5001", "--directory", "/app/html"]
