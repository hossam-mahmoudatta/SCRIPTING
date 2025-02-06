#!/usr/bin/zsh

myavg() {
  # Prompt user to enter the size of the array
  echo "Enter the size of the array: "
  read size

  # Create an empty array
  declare -a arr

  sum=0


  # Loop to prompt the user to enter each element
  for (( i=0; i<size; i++ ))
  do
      echo "Enter element $((i+1)):"
      read element
      arr+=("$element")
      sum=$((sum+element))
  done

  # Print the array elements
  echo "\nThe array you entered is:\n"
  for element in "${arr[@]}"
  do
      echo "$element"
  done

  # Calculate the average
  avg=$((sum/size))
  print "\nThe Average for the inputs entered is: $avg"
  print "\nDone"
}
