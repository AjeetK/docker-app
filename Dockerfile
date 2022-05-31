#FROM python:2.7-slim
FROM brunneis/python:2.7.16-ubuntu
MAINTAINER "i.ajeetkhan@gmail.com"
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
expose 5000
ENTRYPOINT [ "python" ]
CMD [ "docker_app.py" ]