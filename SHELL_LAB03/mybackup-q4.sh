#!/usr/bin/zsh

# A script to copy a single file
mybackup() {

  # Define the backup file
  hosaBackup="/home/hosa/hosabackup.tar.gz"
  
  # Create an empty tar archive (or overwrite if exists)
  sudo touch "$hosaBackup"

  # Loop through all files and directories in /home/hosa
  for file in /home/hosa/*;
  do
    # Check if it's a valid file or directory
    if [ -e "$file" ];
    then
      # Add the file/directory to the tar archive
      sudo tar -rvf "$hosaBackup" -C /home hosa/$(basename "$file") --append
    fi
  done
  
  # Verify the backup file
  echo "Backup completed. Check for the created backup file:"
  ls -lh "$hosaBackup"
}