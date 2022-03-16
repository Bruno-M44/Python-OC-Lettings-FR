FROM python:3.8

#créer un répertoire pour le projet
WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    DEBUG=False \
    PORT=8000

ADD . /app

#récup les dépendances
COPY requirements.txt .

#install les dépendances
RUN pip install -r requirements.txt

#copy le code source
COPY . /app
#port
EXPOSE 8000

#run le projet
CMD gunicorn project.wsgi:application --bind 0.0.0.0:$PORT



# FROM python:3.10
# ENV PYTHONUNBUFFERED 1
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /code/
