#!/usr/bin/zsh

x = 5

# Call s2-q2.sh and pass x as an argument
./s2-q2.sh "$x"

# Export x as an environment variable and call s2.sh
export x
./s2-q2.sh
