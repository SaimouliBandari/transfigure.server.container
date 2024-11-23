# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /transfigure

# Copy requirements and install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Run the application
CMD ["python3", "-m" ,"app.main"]
