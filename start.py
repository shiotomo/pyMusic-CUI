#!/usr/bin/python
#coding:utf-8

import os

path = open('path.txt', 'w')

print "Music path = ",
musicpath = raw_input()
path.write(musicpath)
path.close()

os.mkdir("Music")
