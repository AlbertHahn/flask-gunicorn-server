FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "-c", "./gunicorn/gunicorn.conf.py" ,"main:app"]