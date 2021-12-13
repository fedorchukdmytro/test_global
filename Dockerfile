FROM ubuntu:18.04

WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get install -y iperf3
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip3 install pytest

CMD ['pytest']