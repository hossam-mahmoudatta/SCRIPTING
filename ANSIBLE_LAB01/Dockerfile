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

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install Nginx
RUN apt-get update && \
        apt-get install -y nginx && \
        apt-get clean

# Expose port 80
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
