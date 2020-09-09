#! /bin/bash

echo Enter system name
read $system

echo Creating environment

# update apt
sudo apt-get update

# collect list of outdated python packages
pip list --outdated

# upgrade pip
pip install --upgrade


mkdir Results; cd Results

# create directories
mkdir Reconnaissance; cd Reconnaissance; mkdir Nmap
cd ../
mkdir Scanning; cd Scanning; mkdir Nessus
cd ../


echo Environment setup complete:

# display tree
tree