FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app/

# Run the app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
