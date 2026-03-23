# Use the latest stable 3.14 version
ARG PYTHON_VERSION=3.12-slim

FROM python:${PYTHON_VERSION}

# Optimize Python for Docker
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install psycopg2 dependencies (system-level)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /code

# Copy and install Python dependencies
# Using /tmp for requirements helps keep the final image clean
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Copy application code
COPY . /code

# Django-specific settings
ENV SECRET_KEY="x4PORD7oBXmL82dnH14wKj3QAgGj2WSEJMtIDcuXMVrwxLmV9B"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Run with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "Core.wsgi"]

