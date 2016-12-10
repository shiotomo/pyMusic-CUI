#!/usr/bin/python
#!/coding:utf-8

# import
import os
import pygame
import time
import sys
from mutagen.mp3 import MP3

filepath = 'path.txt'
musicdir = 'Music'

# path
if os.path.exists(filepath):
    print "Path file [OK]"
else :
    print "Path file [NO]"
    print "Please make a path.txt file"
    print "Please write absolute path to music in the path.txt"
    exit()

if os.path.exists(filepath):
    print "Music directory [OK]"
else :
    print "Music directory [NO]"
    print "Please make a `Music` directory"
    exit()

path = open('path.txt', 'r')

for musicpath in path:
    print "Music file path =",
    print musicpath

path.close()

musicpath = musicpath.rstrip("\n")

# start
print "-- pyMusic-CUI --"
print "*** MUSIC LIST***"
print ""

# file list
files = os.listdir(musicpath)

for file in files:
    print file

print ""
print "music select"
print "=>",

## select music
select = raw_input()
selectmusic = musicpath + select

audio = MP3(selectmusic)

pygame.mixer.init()
pygame.mixer.music.load(selectmusic)
pygame.mixer.music.play(1)

print "---"+select+"---"
print ""
print "音量:%s" %pygame.mixer.music.get_volume()
#print "音声時間:%s[ms]" %pygame.mixer.music.get_busy()
#print "再生時間:"+audio.info.length

time.sleep(audio.info.length)
pygame.mixer.music.stop()
print "終了"
