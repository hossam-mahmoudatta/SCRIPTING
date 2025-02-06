#!/usr/bin/zsh

# This is a menu
while true;
do
    select choice in "ls" "ls -a" "exit"
    do
        case $choice in
        "ls")
                ls

                ;;
            "ls -a")
                ls -a
                ;;
            "exit")
                print "Program will exit now"
                # exit 0
                break 2
                ;;
            *)
                print "No Valid Entry"
                ;;
        esac
    done
done