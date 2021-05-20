from pygame import mixer  # Load the popular external library
import pygame
import glob
import time
import os.path
import asyncio,threading
import random
playlist = glob.glob('./music/*.mp3')

def playplaylist(playlist):
    if len(playlist)==0:
        print("there is no music in the playlist.")
        return

    if os.path.isfile('a'):
        os.remove('a')
    if os.path.isfile('b'):
        os.remove('b')
    if os.path.isfile('c'):
        os.remove('c')

    mixer.init()
    pygame.display.init()
    running = True
    idx = 0
    while running:
        if mixer.music.get_busy() == 1 and os.path.isfile('a'):
            mixer.music.pause()
            os.remove('a')
            continue
        if mixer.music.get_busy() == 1 and os.path.isfile('b'):
            mixer.music.unpause()
            os.remove('b')
            continue

        if mixer.music.get_busy() == 0:  # A track has ended
            mixer.music.load(playlist[idx])  # Q
            mixer.music.play()
            idx += 1
            if idx == len(playlist):
                idx = 0
                random.shuffle(playlist)

        if os.path.isfile('c'):
            os.remove('c')
            mixer.music.pause()
            return

        time.sleep(0.1)



playplaylist(playlist)

# open('b', 'a').close()