#!/usr/bin/zsh

# A script to copy a single file
mybackup() {

  # Define the backup file
  hosaBackupFile="/home/hosa/hosabackup.tar.gz"
  
  # Create an empty tar archive (or overwrite if exists)
  sudo touch "$backupFiles"

  # Loop through all files and directories in /home/hosa
  for file in /home/hosa/*;
  do
    # This will check if its a file or a dir
    if [ -f $file ];
    then
      # this will append files into the overall file
      backupFiles="$backupFiles $file"
    fi
  done

  # Here happens the backup and compression
  sudo tar -czvf "$hosaBackupFile" -C /home $backupFiles
  
  # Verify the backup file
  echo "Backup completed. Check for the created backup file:"
  ls -lh "$hosaBackupFile"
}