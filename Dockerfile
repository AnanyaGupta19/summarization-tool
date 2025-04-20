# Base image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy app and requirements
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "main_code.py", "--server.port=8501", "--server.enableCORS=false"]
