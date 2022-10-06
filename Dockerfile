FROM python:3.10.6-slim-buster

WORKDIR C:\Users\user\Pictures\movies_news


COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

# Expose port
EXPOSE 8080

CMD ["python", "manage.py", "runserver"]


