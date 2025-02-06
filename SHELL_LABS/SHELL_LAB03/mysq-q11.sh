#!/usr/bin/zsh


# Function to calculate the square of a number
mysq() {
  # Check if exactly one argument is passed
  if [ $# -eq 1 ];
  then
    value=$1
    square=$((value*value))
    echo "The square of $value is: $square"
  else
    echo "invalid entry"
  fi
}
