# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy all local files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
