#!/bin/sh
# Tensorflow Linux CPU version for Python
apt-get update && upgrade
apt-get install python-pip python-dev
pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.7.1-cp27-none-linux_x86_64.whl
apt-get install python-virtualenv
virtualenv --system-site-packages ~/tensorflow
source ~/tensorflow/bin/activate  
apt-get install python-numpy swig python-dev
