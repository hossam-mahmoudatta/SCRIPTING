# ==============================================
# Created By: Hossam Mahmoud
# Date: 2025-02-02
# Filename: Dockerfile
# Description: Dockerfile to run an image to use Ansible on
# Version: 1.0.0
# Last Modified: 2025-02-02 by Hossam
# Copyright (c) 2025 Hossam. All rights reserved.
# TODO: Add future tasks or improvements
# ==============================================

# Use the latest LTS version of Ubuntu
FROM ubuntu:latest

# Update the package list and install Nginx
RUN apt-get update && \
        apt-get install -y ssh sudo && \
        apt-get clean

# Adds a user with the name of hosa-iti
RUN adduser hosa-iti

# Changes the password of the user created
RUN echo "hosa-iti:123" | chpasswd

# Confirms the change of the password
RUN usermod -aG sudo hosa-iti

# Starts the ssh and bash services on the container
ENTRYPOINT service ssh start && bash
