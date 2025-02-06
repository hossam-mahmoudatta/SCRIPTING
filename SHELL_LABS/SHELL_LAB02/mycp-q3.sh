#!/usr/bin/zsh

# A script to copy a single file
copy_single_file() {
  if [ $# -eq 2 ]; then
    cp "$1" "$2"  # Copy the 1st file to the 2nd file
    echo "File $1 copied into $2"
  else
    echo "Error: make sure syntax is mycp <source_file> <destination_file>"
  fi
}



# A script to copy multiple files to a directory
copy_multiple_files() {
  # Check if at least two arguments are passed
  if [ $# -ge 2 ];
  then
    # The last argument should be the destination directory
    destination="${!#}"
    
    # Check if the destination is a directory
    if [ -d "$destination" ];
    then
      # Loop through all the files except the last argument (destination)
      for file in "$@";
      do
        # Skip the last argument (destination)
        if [ "$file" != "$destination" ]; then
          # Check if the file exists
          if [ -f "$file" ]; then
            cp "$file" "$destination"   # Copy the file to the destination
            echo "File $file copied to $destination"
          else
            echo "Error: file $file invalid."
          fi
        fi
      done
    else
      echo "Error: dest $destination is invalid."
    fi
  else
    echo "Error: make sure syntax is mycp <file1> <file2> ... <destination_directory>"
  fi
}

# Check the number of arguments
if [ $# -eq 2 ]; then
  copy_single_file "$@"
elif [ $# -ge 2 ]; then
  copy_multiple_files "$@"
else
  echo "Error: make sure syntax is mycp <source_file> <destination_file> or mycp <file1> <file2> ... <destination_directory>"
fi
