#!/bin/bash

chkmail() {

    # Define the username whose mail we want to check
    USER="$USER"  # You can replace 'root' with any other username

    # Define the mail file location
    mailFile="/var/mail/$USER"

    # Check if the mail file exists
    if [ ! -f "$mailFile" ];
    then
        echo "Mail file for $USER does not exist at $mailFile"
        exit 1
    fi

    # Check for new mail every 10 seconds
    while true;
    do
        # Get the number of lines in the mail file (if non-zero, there are new mails)
        mailCount=$(wc -l < "$mailFile")

        # If there are new lines (new mail)
        if [ "$mailCount" -gt 0 ];
        then
            echo "You have new mail for $USER!"
            mail -f "$mailFile"  # This will show the new mail in the mailbox
        else
            echo "No new mail for $USER"
        fi
        # Wait for 10 seconds before checking again
        sleep 10
    done
}