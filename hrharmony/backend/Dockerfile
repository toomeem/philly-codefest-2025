# Use Python official image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend
COPY . .

# Expose port and run Flask
EXPOSE 8080
CMD ["python", "app.py"]
