#!/bin/bash

# Check if the mail template exists
if [ ! -f "mtemplate" ]; then
  echo "Mail template file 'mtemplate' not found!"
  exit 1
fi

# Get the hostname
hostname=$(hostname)

# Read mail body from the file
mail_body=$(cat mtemplate)

# Get a list of all valid users
users=$(cut -d: -f1 /etc/passwd)

# Define the email subject
subject="System Notification"

# Loop through each user and send the mail
for user in $users; do
  # Check if the user has a valid home directory (to exclude system accounts)
  home_dir=$(getent passwd "$user" | cut -d: -f6)
  if [ -d "$home_dir" ]; then
    email="${user}@${hostname}"
    echo "$mail_body" | mail -s "$subject" "$email"
    echo "Mail sent to $email"
  fi
done
