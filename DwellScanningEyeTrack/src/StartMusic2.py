from pygame import mixer  # Load the popular external library
import pygame
import glob
import time
import os.path
import asyncio,threading
import random
import sys
sys.path.insert(1, './src')
from MusicControl import PauseMusic
# playlist = glob.glob('./music/*.mp3')
import glob

import pandas as pd
df = pd.read_csv('.tmp/userMusicSelection.csv')
playlist = df['fileName'].tolist()

def playplaylist(playlist):
    if len(playlist)==0:
        print("there is no music in the playlist.")
        return

    if os.path.isfile('.tmp/a'):
        os.remove('.tmp/a')
    if os.path.isfile('.tmp/b'):
        os.remove('.tmp/b')
    if os.path.isfile('.tmp/c'):
        os.remove('.tmp/c')

    mixer.init()
    pygame.display.init()
    random.shuffle(playlist)
    running = True
    idx = 0

    while os.path.isfile('.tmp/b') == False:
        time.sleep(0.1)

    # while running:
    #     if mixer.music.get_busy() == 1 and os.path.isfile('.tmp/a'):
    #         mixer.music.pause()
    #         os.remove('.tmp/a')
    #         continue
    #     if mixer.music.get_busy() == 1 and os.path.isfile('.tmp/b'):
    #         mixer.music.unpause()
    #         os.remove('.tmp/b')
    #         continue
    #
    #     if mixer.music.get_busy() == 0:  # A track has ended
    #         mixer.music.load(playlist[idx])  # Q
    #         mixer.music.play()
    #         idx += 1
    #         if idx == len(playlist):
    #             idx = 0
    #             random.shuffle(playlist)
    #
    #     if os.path.isfile('.tmp/c'):
    #         os.remove('.tmp/c')
    #         mixer.music.pause()
    #         return
    while running:
        if mixer.music.get_busy() == 1 and os.path.isfile('.tmp/a'):
            mixer.music.pause()
            os.remove('.tmp/a')
            continue
        elif mixer.music.get_busy() == 1 and os.path.isfile('.tmp/b'):
            mixer.music.unpause()
            os.remove('.tmp/b')
            continue
        elif os.path.isfile('.tmp/c'):
            os.remove('.tmp/c')
            mixer.music.pause()
            mixer.music.stop()
            return

        # Remove trigger files.
        if os.path.isfile('.tmp/a'):
            os.remove('.tmp/a')
        if os.path.isfile('.tmp/b'):
            os.remove('.tmp/b')
        if os.path.isfile('.tmp/c'):
            os.remove('.tmp/c')


        if mixer.music.get_busy() == 0:  # A track has ended
            mixer.music.load(playlist[idx])  # Q
            mixer.music.play()
            idx += 1
            if idx == len(playlist):
                idx = 0
                random.shuffle(playlist)

        time.sleep(0.1)

# fileList = ['.tmp/a','.tmp/b','.tmp/c']
# for F in fileList:
#     if os.path.isfile(F):
#         os.remove(F)

playplaylist(playlist)
