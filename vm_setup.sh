#! /bin/bash

echo "Now setting up a Vulnerability Management system environment."

echo "Installing Python3 and pip"
# install Python3 and pip
apt-get install python3
apt-get install python3-pip

echo "Installing Git"
# install Git
apt-get install git

# install OpenVAS packages
add-apt-repository ppa:mrazavi/openvas

apt-get update

echo "Installing OpenVAS9"
# install OpenVAS9
apt-get install openvas9

# update OpenVAS
greenbone-nvt-sync
greenbone-scapdata-sync
greenbone-certdata-sync
service openvas-scanner restart
service openvas-manager restart
openvasmd --rebuild --progress

# cloning cve-search
git clone https://github/cve-search/cve-search.git
cd cve-search; pip3 install -r requirements.txt


echo "Envrionment complete."