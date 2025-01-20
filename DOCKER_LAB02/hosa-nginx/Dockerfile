# ==============================================
# Created By: Hossam Mahmoud
# Date: 2025-01-19
# Filename: Dockerfile
# Description: Dockerfile to run nginx
# Version: 1.0.0
# Last Modified: 2025-01-19 by Hossam
# Copyright (c) 2025 Hossam. All rights reserved.
# TODO: Add future tasks or improvements
# ==============================================

# Use the official Nginx image from dockerhub
FROM nginx:latest

# Remove default Nginx config file
RUN rm /etc/nginx/conf.d/default.conf

# Replace the default with our created config file
COPY hosa-nginx.conf /etc/nginx/conf.d/

# Copy my created HTML files to Nginx root
COPY index.html /usr/share/nginx/html/

# Expose port 8080
EXPOSE 8080

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
