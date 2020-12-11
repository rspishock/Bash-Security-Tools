# Security Tools
A collection of security and pen testing tools written in Bash and Python

## Tools
### environment.sh
### sweep.sh
### generate_ip.py


##### Tools and technologies used
##### Environment
The script was originally created using VSCode on a Late 2018 MacBook Pro, 32GB RAM, 6 Core Intel i9, with 1TB SSD.


#### environment.sh
A simple script which can be used to set up a directory structure for risk assessments and pentesting.

##### Usage
./environment.sh


#### sweep.sh
A simple script that will ping hosts on a given network twice to determine if they are up.  This script can be used create a list of IPs to utilize with an nmap scan.

#### Usage
./sweep.sh


#### generate_ip.py
A simple script which can be used to generate a list of random IP addresses.  This script is intended to be used to generate a list of decoy IP addresses to be
used to conceal the source of an nmap scan.

#### Usage
./generate-ip.py 