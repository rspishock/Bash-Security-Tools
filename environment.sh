#! /bin/bash

echo Enter system name
read $system

echo Creating environment

# update apt
sudo apt-get update

if pip3 -V
then
    # collect list of outdated python packages
    pip list --outdated

    # upgrade pip
    # pip install --upgrade

    echo "pip updated"
else echo "pip not found."
fi;


mkdir Results; cd Results

# create directories
mkdir Reconnaissance; cd Reconnaissance; mkdir Nmap
cd ../
mkdir Scanning; cd Scanning; mkdir Nessus
cd ../


echo Environment setup complete:

# display tree
tree