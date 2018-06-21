FROM python:alpine3.6
MAINTAINER voyagerwoo

ADD . /root/
WORKDIR /root/
RUN pip install -e .

ENTRYPOINT ["gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:9460", "app:app"]
