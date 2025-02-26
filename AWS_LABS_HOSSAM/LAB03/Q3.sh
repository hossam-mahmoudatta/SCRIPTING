#!/bin/bash

sudo apt install apache2 unzip  -y # Installing Apache and Unzip Utilities
sudo systemctl start apache2 # Starting the Apache Service
sudo systemctl enable apache2 # Enabling the Apache Service for reboot

# Installing AWSCLI
sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo unzip awscliv2.zip
sudo ./aws/install

# Assign a Bucket Name
BUCKET_NAME="hosa-bucket-01"

# Copy or Download a file from the bucket to the EC2 Instance
aws s3 cp s3://$BUCKET_NAME/index.html /var/www/html/index.html

#Restart the Apache Server
sudo systemctl restart apache2