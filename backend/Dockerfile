FROM python:3.9

ENV PYTHONBUFFERED=1
ENV PYTHONDOWNWRITEBYTECODE=1

WORKDIR /django_site

COPY ./requirements.txt /django_site/requirements.txt

RUN pip install -r /django_site/requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input