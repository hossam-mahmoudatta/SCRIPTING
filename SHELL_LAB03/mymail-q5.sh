#!/usr/bin/zsh

# Will copy now without any arguments
listDIR() {
    if [ $# -lt 1 ];
    then
        ls -l  # Moves to the home DIR
        echo "Current DIR is listed"
    elif [ $# -eq 1 ];
    then
        dir="$1"
        ls -l "$dir"
        echo "You listed $dir !"
    else
        echo "Usage: listDIR [DIR]"
    fi
}