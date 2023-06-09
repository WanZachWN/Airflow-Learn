FROM apache/airflow:2.6.1

# Update permissions for apt directories
USER root
RUN chown -R airflow: /var/lib/apt/lists

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        libfreetype6-dev \
        libpng-dev

# Switch back to the airflow user
USER airflow


COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt