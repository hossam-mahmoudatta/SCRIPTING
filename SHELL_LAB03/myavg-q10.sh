#!/usr/bin/zsh

# Method 1: Get x from the argument
if [ $# -ge 1 ];
then
  echo "Method 1: Value of x from argument is $1\n"
else
  echo "Method 1: Failed! No argument passed\n"
fi

# Method 2: Get x from the environment variable
if [ -n "$x" ];
then
  echo "Method 2: Value of x from environment variable is $x\n"
else
  echo "Method 2: x was not set in the environment\n"
fi
