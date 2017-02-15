#!/usr/bin/env python
#coding:utf-8
#author:nothing
import zipfile
import optparse
from threading import Thread
def extractFile(zFile,password):
    try:
        zFile.extractFile(pwd=password)
        print '[+] Found Password :' + password
        exit(0)
    except:
        pass


def main():
    parser = optparse.OptionParser("usage%prog "+ "-f <zipfile> -d <dict>")
    parser.add_option('-f', dest='zname',type='string',help='specify zip file')
    parser.add_option('-f', dest='dname', type='string', help='specify dict file')
    (options, args) = parser.parse_args()
    if (options.zname is None) or (options.dname is None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile,args=(zFile,password))
