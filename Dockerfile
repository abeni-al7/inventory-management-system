# Use the official Python image as the base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire project to the working directory
COPY . /code/

# Apply database migrations
RUN python manage.py migrate

# Expose port 8000 for the Django app
EXPOSE 8000

# Start the Django application using Gunicorn
CMD ["gunicorn", "inventory_system.wsgi:application", "--bind", "0.0.0.0:8000"]