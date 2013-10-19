FROM strafelabs/fontforge:base
MAINTAINER Rob Madole

RUN mkdir /etc/fonthammer
RUN mkdir /var/fonthammer

ADD requirements.txt /etc/fonthammer/requirements.txt

RUN pip install -r /etc/fonthammer/requirements.txt
