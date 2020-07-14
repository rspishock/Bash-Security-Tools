#! /bin/bash

echo Enter system name
read $system

echo Creating environment

mkdir Results; cd Results

# create directories
mkdir Reconnaissance; cd Reconnaissance; mkdir Nmap
cd ../
mkdir Scanning; cd Scanning; mkdir Nessus
cd ../


echo Environment setup complete:

# display tree
tree