FROM ubuntu:14.04
MAINTAINER Vishal Lall "vishallall@live.com"
RUN apt-get update && apt-get install -y \
	python \
	build-essential \
	python-dev \
	python-pip \
	python-numpy \	
	git \
	wget \	

WORKDIR /home
RUN git clone https://github.com/vlall/visorflow
RUN pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.7.1-cp27-none-linux_x86_64.whl
RUN pip install -r /home/visorflow/requirements.txt
