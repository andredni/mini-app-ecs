from python:3.14.0a2-slim-bookworm

RUN mkdir -p /app
COPY app.py requirements.txt /app

RUN pip install -r /app/requirements.txt

CMD python /app/app.py