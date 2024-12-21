#!/usr/bin/zsh

# A script to copy a single file
mychmod() {
  
  for file in $(ls);
  do
    sudo chmod +x $file
  done
  print "Check the permissions of your DIR:\n"
  ls -lR /home/hosa

}


  # Turned out he need the solution with for loop
  # sudo chmod +x -R /home/hosa