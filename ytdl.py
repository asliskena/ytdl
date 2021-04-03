#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Powered by youtube-dl
# coded by ahmad
import sys, os

os.system ('clear')
banner = ("""       _         _                     _                 _
 _   _| |_    __| | _____      ___ __ | | ___   __ _  __| | ___ _ __
| | | | __|  / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
| |_| | |_  | (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |
 \__, |\__|  \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|
 |___/ """)

print (banner)

print ("\n ======================= Simple yt downloader ======================")

choose = True
while choose:
    print ("""
    [1]. Mkv files
    [2]. Mp4 files
    [3]. Mp3 files
    [4]. Webm files""")
    choose = input("\nChoose your want : ")
    if choose =="1":
        print("\n[ MKV files ]")
        urlmkv = input("Input youtube url : ")
        os.system("youtube-dl --format 'bestvideo+bestaudio[ext=m4a]/bestvideo+bestaudio/best' -o 'result/%(title)s.%(ext)s' --merge-output-format mkv "+urlmkv)
        print ("\n\nDownload success! \nResult file > result/yourvideo.mkv")
        sys.exit()
    elif choose =="2":
        print("\n[ MP4 files ]")
        urlmp4 = input("Input youtube url : ")
        os.system("youtube-dl --format 'bestvideo+bestaudio[ext=m4a]/bestvideo+bestaudio/best' -o 'result/%(title)s.%(ext)s' --merge-output-format mp4 "+urlmp4)
        print ("\n\nDownload success! \nResult file > result/yourvideo.mp4")
        sys.exit()
    elif choose =="3":
        print("\n[ MP3 files ]")
        urlmp3 = input("Input youtube url : ")
        os.system("youtube-dl -x --audio-format mp3 -o 'result/%(title)s.%(ext)s' "+urlmp3)
        print ("\n\nDownload success! \nResult file > result/yourmusic.mp3")
        sys.exit()
    elif choose =="4":
        print("\n[ WEBM / M4A files ]")
        urlwebm = input("Input youtube url : ")
        os.system("youtube-dl -f bestaudio -o 'result/%(title)s.%(ext)s' "+urlwebm)
        print ("\n\nDownload success! \nResult file > result/yourfiles.m4a")
        sys.exit()
    elif choose !="":
        print ("\nWrong input :)")

# for contact : ahmad@hypecodex.id
# thanks for all :)
