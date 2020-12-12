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
            if elem.tag == 'host'
