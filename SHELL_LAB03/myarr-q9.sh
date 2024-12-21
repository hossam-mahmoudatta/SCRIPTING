#!/usr/bin/zsh

# Prompt user to enter the size of the array
echo "Enter the size of the array: "
read size

# Create an empty array
declare -a arr

# Loop to prompt the user to enter each element
for (( i=0; i<size; i++ ))
do
    echo "Enter element $((i+1)):"
    read element
    arr+=("$element")
done

# Print the array elements
echo "The array you entered is: "
for element in "${arr[@]}"
do
    echo "$element"
done
