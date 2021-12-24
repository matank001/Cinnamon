FROM python:2.7

WORKDIR /vol

RUN pip2 install distorm3
RUN pip2 install pycrypto

COPY volatility .