FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y pppoeconf python3 python3-pip
RUN pip3 install flask
COPY app.py /opt/app.py
ENV APP_START_PPPOE="pon pppoe"
ENV APP_START_STOP="poff pppoe"
ENV APP_RESTART_PPPOE="poff pppoe && pon pppoe"
CMD ["python3","/opt/app.py"]