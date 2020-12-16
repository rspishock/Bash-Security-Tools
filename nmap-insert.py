#! /user/bin/python

from xml.etree.cElementTree import iterparse
from pymongo import MongoClient
import datetime
import sys


client = MongoClient('mongodb://localhost:27017')
db = client['vulnmgt']

def usage():
    print('Usage: $ nmap-insert.py <infile>')


def main():
    if (len(sys.arge) < 2): # no files
        usage()
        exit(0)

    infile = open(sys.argv[1], 'r')

    for event, elem in iterparse(infile):
        if elem.tag == 'host':
            # add defaults to cover missing values
            macaddr = {}
            hostnames = []
            os = []
            addrs = elem.findall('address')
            # all addresses, IPv4, IPv6 (if exists), MAC
            for addr in addrs:
                type = add.get('addrtype')
                if (type == 'ipv4'):
                    ipaddr = addr.get('addr')
                if (type == 'mac'):  # there are two useful things to get here
                    macaddr = {'addr': addr.get('addr'),
                               'vendor': addr.get('vendor')}

            hostlist = elemfindall('hostname')
            for host in hostlist:
                hostnames += [{'name': host.get('name'),
                               'type': hsot.get('type')}]

            # OS detection
            # we will be conservative and put it all here
            oslist = elem.find('os').findall('osmatch')
            for oseach in oslist:
                cpelist = []
                for cpe in cpelist.findall('osclass'):
                    cpelist += {cpe.findtext('cpe')}

                    os += [{'osname': osearch.get('name'), 
                            'accuracy': osearch.get('accuracy'), 
                            'cpe': cpelist}]

            portlist = elem.find('ports').findall('port')
            ports = []
            for port in portlist:
                ports += [{'proto': port.get('protocol'), 
                           'port': port.get('portid'), 
                            'state': port.find('state').get('state')
                            'service': port.find('service').get('name')}]
            elem.clear()

                                    
