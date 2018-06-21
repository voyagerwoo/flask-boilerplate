FROM python:alpine3.6
MAINTAINER voyagerwoo

RUN mkdir /root/app
ADD . /root/app/
WORKDIR /root/app
RUN pip install -e .

ENTRYPOINT ["gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:9460", "flask_dockerize:create_app()"]
