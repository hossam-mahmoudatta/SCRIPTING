#!/usr/bin/zsh

# This is a menu
select choice in 1 2 3
do
    case $choice in
        1)
            ls
            ;;
        2)
            ls -a
            ;;
        3)
            print "Program will exit now"
            exit
            ;;
        *)
            print "No Valid Entry"
            ;;
    esac
done