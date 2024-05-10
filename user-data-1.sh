#!/bin/bash
sudo yum install -y git python3 python3-pip
cd /home/ec2-user
mkdir flask-hello-world-2024
sudo git clone https://github.com/jh2946/flask-hello-world-2024 flask-hello-world-2024
cd flask-hello-world-2024
sudo pip3 install -r requirements.txt
sudo nohup python3 main.py