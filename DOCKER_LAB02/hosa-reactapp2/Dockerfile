# ==============================================
# Created By: Hossam Mahmoud
# Date: 2025-01-19
# Filename: Dockerfile
# Description: Multistage Dockerfile to run the React app
# Version: 1.0.0
# Last Modified: 2025-01-19 by Hossam
# Copyright (c) 2025 Hossam. All rights reserved.
# TODO: Add future tasks or improvements
# ==============================================


############ Build Stage ###########
# Use the latest LTS version of Node.js
FROM node:18-alpine AS build
 
# Set the working directory inside the container
WORKDIR /app
 
# Copy package.json and package-lock.json
COPY package*.json ./
 
# Install dependencies
RUN npm install
 
# Copy the rest of your application files
COPY . .

# Build the react app
RUN npm run build
 

########### Production Stage ###########
# Deploy the app using Nginx
FROM nginx:alpine

# Copy built React app from the build stage to Nginx's serving directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 3000
EXPOSE 3000

# Start Nginx
CMD ["nginx", "-g", "daemon off;", "-p", "3000"]