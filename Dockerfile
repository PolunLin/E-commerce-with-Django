FROM python:3.9-slim

RUN apt-get update

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080


ENTRYPOINT [ "/bin/bash", "docker-entrypoint.sh" ]

CMD python manage.py runserver 0.0.0.0:8000
