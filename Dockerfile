# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Copie o arquivo model.pkl para o diretório de trabalho no contêiner
COPY model.pkl .
COPY scaler.pkl .

# Install dependencies
RUN pip install -r requirements.txt

# Install uvicorn
RUN pip install uvicorn

# Copy the application code into the container
COPY app/ /app

# Expose the port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
