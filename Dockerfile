# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-alpine3.17

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache gcc musl-dev python3-dev

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /django_app
COPY ./DjangoPractice /django_app

RUN python manage.py collectstatic

# Creates a non-root user with an explicit UID and adds permission to access the /django_app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /django_app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "config.wsgi"]
