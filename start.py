#!/usr/bin/python
#coding:utf-8

import os
import commands

path = open('path.txt', 'w')

print "Music path = ",
musicpath = commands.getoutput("pwd")
musicpath = musicpath + "/Music/"
print musicpath
path.write(musicpath)
path.close()

os.mkdir("Music")
