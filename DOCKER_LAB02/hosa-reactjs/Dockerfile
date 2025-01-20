# ==============================================
# Created By: Hossam Mahmoud
# Date: 2025-01-19
# Filename: Dockerfile
# Description: Dockerfile to run the React app
# Version: 1.0.0
# Last Modified: 2025-01-19 by Hossam
# Copyright (c) 2025 Hossam. All rights reserved.
# TODO: Add future tasks or improvements
# ==============================================

# Use the latest LTS version of Node.js
FROM node:18-alpine
 
# Set the working directory inside the container
WORKDIR /app
 
# Copy package.json and package-lock.json
COPY package*.json ./
 
# Install dependencies
RUN npm install
 
# Copy the rest of your application files
COPY . .
 
# Expose the port your app runs on
EXPOSE 1997
 
# Define the command to run your app
CMD ["npm", "start"]
