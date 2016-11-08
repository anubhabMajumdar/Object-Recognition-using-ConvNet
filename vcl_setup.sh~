#!/bin/bash
sudo apt-get update
sudo apt-get install python-pip python-dev
python -m pip install --upgrade pip
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc2-cp27-none-linux_x86_64.whl
sudo pip install --upgrade $TF_BINARY_URL
pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
sudo apt-get install python-matplotlib
cd Desktop
git clone https://github.ncsu.edu/amajumd/Object-recognition