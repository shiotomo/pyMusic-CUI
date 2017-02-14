#!/usr/bin/python
#coding:utf-8

# import
import os
import pygame
import time
import sys
from mutagen.mp3 import MP3

# path_import
def pathimport():
    filepath = 'path.txt'
    return filepath


def music_import():
    musicdir = 'Music'
    return musicdir


def filepath():
    path = open('path.txt', 'r')

    for musicpath in path:
        # print "Music file path =",
        # print musicpath
        musicpath

    path.close()

    musicpath = musicpath.rstrip("\n")

    return musicpath


def musiclist():
    print "-- pyMusic-CUI --"
    print "*** MUSIC LIST ***"
    print ""

    files = os.listdir(filepath())

    for file in files:
        print file


def music_select():
    print ""
    print "music select"
    print "=>",

    select = raw_input()
    selectmusic = filepath() + select

    return selectmusic


musiclist()
audio = music_select()
audio_len = MP3(audio)
pygame.mixer.init()
pygame.mixer.music.load(audio)
pygame.mixer.music.play(1)

print "--- play music ---"

time.sleep(audio_len.info.length)
pygame.mixer.music.stop()

print "---end---"
