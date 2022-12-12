#1/bin/bash
echo "starting script"

apt list --upgradable
sudo apt update
sudo apt-get update
sudo apt install python3
sudo apt-get install -y python3-pip
sudo apt update
sudo apt install pip3
sudo pip3 install flask
pip3 install -r requirements.txt
sudo apt update
sudo pip3 install boto3
ls
