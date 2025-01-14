#!/usr/bin/env bash
# Bash script for your web servers for the deployment of web_static

#Nginx Installation
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Creating Repos 
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Creating Symbolic link & Changing Ownership
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

# Serving the content & starting the server
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
