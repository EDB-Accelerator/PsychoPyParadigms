# from pygame import mixer  # Load the popular external library
# import pygame,os
# import time
# import random

# def PlayMusicStart(playlist):
#     if len(playlist)==0:
#         print("there is no music in the playlist.")
#         return
#
#     mixer.init()
#     pygame.display.init()
#     running = True
#     idx = 0
#     while running:
#         if mixer.music.get_busy() == 1 and os.path.isfile('a'):
#             mixer.music.pause()
#             os.remove('a')
#             continue
#         if mixer.music.get_busy() == 1 and os.path.isfile('b'):
#             mixer.music.unpause()
#             os.remove('b')
#             continue
#
#         if mixer.music.get_busy() == 0:  # A track has ended
#             mixer.music.load(playlist[idx])  # Q
#             mixer.music.play()
#             idx += 1
#             if idx == len(playlist):
#                 idx = 0
#                 random.shuffle(playlist)
#         time.sleep(0.1)
import os

def PauseMusic():
    if os.path.isfile('a') == False:
        open('a', 'a').close()
        if os.path.isfile('b'):
            os.remove('b')

def UnpauseMusic():
    if os.path.isfile('b') == False:
        open('b', 'a').close()
        if  os.path.isfile('a'):
            os.remove('a')
