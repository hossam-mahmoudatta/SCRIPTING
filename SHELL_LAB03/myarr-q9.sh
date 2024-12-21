#!/usr/bin/zsh

# Will copy now without any arguments
myarr() {
    if [ -d "$1" ];
    then
        echo "$1 is a directory.\n"
        echo "And its permissions are:\n"
        ll "$1" | awk '{print $1}'

    elif [ -f "$1" ];
    then
        echo "$1 is a file.\n"
        echo "And its permissions are:\n"
        ll "$1" | awk '{print $1}'

    else
        echo "$1 does not exist or is not a regular file/directory."
    fi
}