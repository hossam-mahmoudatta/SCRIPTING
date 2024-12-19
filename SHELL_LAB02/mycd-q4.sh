#!/usr/bin/zsh

# Will copy now without any arguments
chaHomeDIR() {
    if [ $# -lt 1 ];
    then
        cd ~  # Moves to the home DIR
        echo "You are now at the home directory"
    elif [ $# -eq 1 ];
    then
        destination="$1"
        cd "$destination"
        echo "You are now @ $destination"
    else
        echo "Usage: chaHomeDIR [DIR]"
    fi
}

