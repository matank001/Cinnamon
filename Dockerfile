FROM python:2.7

WORKDIR /vol

RUN pip2 install distorm3
RUN pip2 install pycrypto
RUN pip2 install paramiko
RUN pip2 install scp
RUN pip2 install openpyxl==2.1.2
RUN pip2 install xlrd==1.2.0
RUN pip2 install pandas
RUN pip2 install glob2


COPY remote_init.py .
COPY make_load_unload.sh .
COPY create_profile.sh .

COPY volatility /vol/volatility
COPY src /vol/src

COPY splunk/scripts /vol

run cd volatility
run mkdir profile
run mkdir temp
run chmod 777 profile
run mkdir output
run chmod 777 output
