#!/usr/bin/zsh

shopt -s extglob;
export LC_COLLATE=C;

# Will copy now without any arguments
mycase2() {
    # Ask for the user's name
    print "Hello!\nWelcome to Hosa's Shell!\n"
    print "Please enter the string you want to check:"

    read inputStr

    print "\nLets check your input now!\n"
    
    case $inputStr in
    # Its working now without doing any patterns!
    # why?
        ([a-z])*)
            echo "\nInputted string is in lowercase."
            ;;
        ([A-Z])*)
            echo "\nInputted string is in uppercase."
            ;;
        ([0-9])*)
            echo "\nInputted string is a number."
            ;;
        *)
            echo "Invalid Entry"
            ;;
    esac
}