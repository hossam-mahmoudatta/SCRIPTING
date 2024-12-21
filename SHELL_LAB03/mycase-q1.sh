#!/usr/bin/zsh
export LC_COLLATE=C;

# Will copy now without any arguments
mycase() {
    # Ask for the user's name
    print "Hello!\nWelcome to Hosa's Shell!\n"
    print "Please enter the character you want to check:"

    read inputChar

    print "\nLets check your input now!\n"
    
    case "$inputChar" in
        +([a-z]))
            echo "\nInputted character is a lowercase letter."
            ;;
        +([A-Z]))
            echo "\nInputted character is an uppercase letter."
            ;;
        +([0-9]))
            echo "\nInputted character is a number."
            ;;
        *)
            echo "Nothing was entered"
            ;;
    esac
}