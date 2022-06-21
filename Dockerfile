FROM ubuntu:18.04
COPY app.py /opt/app.py
RUN apt-get update
RUN apt-get install -y pppoeconf python3 python3-pip
RUN pip3 install flask
CMD ['python3','/opt/app.py']