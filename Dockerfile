FROM python:2.7

WORKDIR /vol

RUN pip2 install distorm3
RUN pip2 install pycrypto
RUN pip2 install paramiko
RUN pip2 install scp

COPY remote_init.py .
COPY volatility .