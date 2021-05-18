from pygame import mixer  # Load the popular external library
import pygame
import glob
import time
import asyncio,threading


def playy(musicList):
   mixer.init()
   mixer.music.load(musicList[1])
   mixer.music.play()
   # return mixer

def playMusicList(playlist):
    mixer.init()
    pygame.display.init()
    mixer.music.load(playlist.pop())  # Get the first track from the playlist
    mixer.music.queue(playlist.pop())  # Queue the 2nd song
    mixer.music.set_endevent(pygame.USEREVENT)  # Setup the end track event
    mixer.music.play()  # Play the music
    running = True
    while running:
        print(playlist)
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:  # A track has ended
                if len(playlist) > 0:  # If there are more tracks in the queue...
                    mixer.music.queue(playlist.pop())  # Q
        time.sleep(0.1)


# import concurrent.futures

# def foo(bar):
#     print('hello {}'.format(bar))
#     return 'foo'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future = executor.submit(foo, 'world!')
#     return_value = future.result()
#     print(return_value)

from threading import Thread
musicList = glob.glob('./music/*.mp3')
musicList += musicList

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future = executor.submit(playMusicList(musicList))
#     return_value = future.result()
#     print(return_value)


# T = Thread(target=playMusicList(musicList)) # create thread
# T.join()
# T.start() # Launch created thread

loop = asyncio.get_event_loop()
t = threading.Thread(target=playMusicList, args=(musicList,))
t.start()

mixer.music.pause()