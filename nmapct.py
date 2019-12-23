#!/usr/bin/env python
#
# nmapcherry - Parse nmap XML output files and insert them into an SQLite database for CherryTree
# Copyright (c) 2019 Daniel Gasper

import sys
import os
import getopt
import xml.dom.minidom
import sqlite3

VERSION = "1.0"
DEFAULT_DB = "./nmapct.ctb"
true = 1
false = 0
verb_flag = false

def myprint(msg):
    global verb_flag
    if verb_flag == true:
        print msg

    return

def usage(name):
    print "usage: %s [options] <nmap output XML file(s)" % name
    print "Options:"
    print "     (-h) --help         This help message"
    print "     (-v) --verbose      Create verbose output"
    print "     (-d) --database     Specify output CherryTree SQLite DB file"
    print "     (-n) --nodb         Do not perform any DB operations (Dry Run)"
    print "     (-V) --version      Print version number and exit"

    return

def main(argv, environ):
    global verb_flag
    nodb_flag = false
    argc = len(argv)

    if argc == 1:
        usage(argv[0])
        sys.exit(0)

    try:
        alist, args = getopt.getopt(argv[1:], "hvd:nV",["help", "verbose", "database=", "nodb", "version"])
    except getopt.GetoptError, msg:
        print "%s: %s\n" % (argv[0],msg)
        usage(argv[0]);
        sys.exit(1)
    
    for(field, val) in alist:
        if field in ("-h", "--help"):
            usage(argv[0])
            sys.exit(0)
        if field in ("-v", "--verbose"):
            verb_flag = true
        if field in ("-d", "--database"):
            db_path = val
        if field in ("-n", "--nodb"):
            nodb_flag = true
        if field in ("-V", "--version"):
            print "nmapcherry v%s by Daniel Gasper" % (VERSION)
            print "Parse nmap XML output files to insert into them into an SQLite DB for CherryTree"
            sys.exit(0)

if __name__ == "__main__":
    main(sys.argv, os.environ)
    sys.exit(0)
