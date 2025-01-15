#!/usr/bin/zsh
#  Created: Hossam Mahmoud

#  This script will create a python enviroment each time you run it!
if [ -d "$1" ] ;
then 
	echo "Environment Already Exist"
else
    cd $1
	python -m venv $1 	
fi 

source $1/bin/activate