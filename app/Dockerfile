FROM python:3.11-slim-buster

WORKDIR /app

RUN pip install flask

COPY . /app

EXPOSE 8080

CMD ["python", "app.py"]