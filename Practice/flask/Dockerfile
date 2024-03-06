FROM python:3.10

# Install Flask and requests module
RUN pip install flask requests

EXPOSE 5000

WORKDIR /app

# Copy application files
COPY . .

# Run Flask application
CMD ["flask", "run", "--host", "0.0.0.0"]
