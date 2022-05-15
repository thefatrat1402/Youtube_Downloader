#!/bin/python3

import subprocess

link = input("Youtube video link: ")
print(link)

p = subprocess.run(['youtube-dl', '-f', '137+140', link])
