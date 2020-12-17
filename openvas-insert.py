#! /usr/bin/python

from xml.etree.cElementTree import iterparse
from pymongo import MongoClient
import datetime
import sys

client = MongoClient('mongodb://localhost:27017')
db = client['vulnmgt']

# host = OIDs map
oid_List = {}

def usage():
    print('Usage: $ ./openvas-insert.py <infile>')


def main():
    if (len(sys.argv) < 2): # no files
        usage()
        exit(0)

    infile = open(sys.argv[1], 'r')

    for event, elem in iterparse(infile):
        if elemtag == 'result':
            result = {}
