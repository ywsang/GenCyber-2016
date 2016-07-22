# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 09:39:13 2016

@author: student
"""
import hashlib
#add the hash library

def md5(fname):
    hash_md5 = hashlib.md5()
    #prepare to hash
    with open(fname, "rb") as f:
        #open a file
        for chunk in iter(lambda: f.read(4096), b""):
            #for each 4096 byte chunk of the file
            hash_md5.update(chunk)
            #do the hash
    return hash_md5.hexdigest()

print(md5("the_wall1.png"))
print(md5("the_wall4.png"))
print(md5("the_wall6.png"))
print(md5("the_wall18.png"))