#!/usr/bin/zsh

# Will copy now without any arguments
listDIRX() {
    if [ $# -lt 1 ];
    then
        ls # Moves to the home DIR
        echo "Current DIR is listed"
    elif [ $# -eq 1 ];
    then
        case "$1" in
            -l)
                ls -l
                echo "\nCurrent DIR longlist is listed"
                ;;
            -a)
                ls -a
                echo "\nCurrent DIR longlist is listed"
                ;;
            -d)
                ls -d
                echo "\nCurrent DIR dir is listed"
                ;;
            -i)
                ls -i
                echo "\nCurrent DIR inode"
                ;;
            -R)
                ls -R
                echo "\nCurrent DIR recursive"
                ;;
            *)
                dir="$1"
                ls -l "$dir"
                echo "You listed $dir !"
                ;;
        esac

    elif [ $# -eq 2 ];
    then
        dir="$2"
        case "$1" in
            -l)
                ls -l "$dir"
                echo "\nCurrent DIR longlist is listed"
                ;;
            -a)
                ls -a "$dir"
                echo "\nCurrent DIR longlist is listed"
                ;;
            -d)
                ls -d "$dir"
                echo "\nCurrent DIR dir is listed"
                ;;
            -i)
                ls -i "$dir"
                echo "\nCurrent DIR inode"
                ;;
            -R)
                ls -R "$dir"
                echo "\nCurrent DIR recursive"
                ;;
            *)
                dir="$1"
                ls -l "$dir"
                echo "You listed $dir !"
                ;;
        esac
    else
        echo "Usage: listDIR [DIR]"
    fi
}