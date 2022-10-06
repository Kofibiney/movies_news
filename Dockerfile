FROM python:3.10.6-slim-buster

WORKDIR /usr/src/app


COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

# Expose port
EXPOSE 8080

CMD ["python", "manage.py", "runserver"]


