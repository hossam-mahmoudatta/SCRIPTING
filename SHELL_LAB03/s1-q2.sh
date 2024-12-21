#!/usr/bin/zsh

x=5

# Call s2-q2.sh and pass x as an argument
./s2-q2.sh "$x"

echo "End of Method 1 Execution\n"

# Export x as an environment variable
export x
./s2-q2.sh

echo "End of Method 2 Execution\n"
