# Use the official Nginx image from dockerhub
FROM nginx:latest

# Remove default Nginx config file
RUN rm /etc/nginx/conf.d/default.conf

# Replace the default with our created config file
COPY hosa-nginx.conf /etc/nginx/hosa-nginx.conf

# Copy my created HTML files to Nginx root
COPY html /usr/share/nginx/html

# Expose port 8080
EXPOSE 8080

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
