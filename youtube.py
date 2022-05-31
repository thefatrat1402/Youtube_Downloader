#!/bin/python3

import subprocess

link = input("Youtube video link: ")
print("1.360p")
print("2.480p")
print("3.720p")
print("4.1080p")
quality = input(": ")

if quality == "1":
    subprocess.run(['youtube-dl', '-f', '134+140', link])
elif quality == "2":
    subprocess.run(['youtube-dl', '-f', '135+140', link])
elif quality == "3":
    subprocess.run(['youtube-dl', '-f', '136+140', link])
elif quality == "4":
    subprocess.run(['youtube-dl', '-f', '137+140', link])

