#!/usr/bin/zsh

# A script to copy a single file
mybackup() {
  
  for file in $(ls /home/$user);
  do
    sudo tar -czvf hosabackup.tar.gz $file
  done

  print "Check the permissions of your DIR:\n"
  ll /home/hosa

}