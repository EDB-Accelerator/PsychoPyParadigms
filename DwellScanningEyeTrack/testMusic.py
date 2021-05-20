from pygame import mixer  # Load the popular external library
import pygame
import glob
import time
import asyncio,threading
import random

def playplaylist(playlist):
    if len(playlist)==0:
        print("there is no music in the playlist.")
        return

    mixer.init()
    pygame.display.init()
    running = True
    idx = 0
    while running:
        if mixer.music.get_busy() == 0:  # A track has ended
            mixer.music.load(playlist[idx])  # Q
            mixer.music.play()
            idx += 1
            if idx == len(playlist):
                idx = 0
                random.shuffle(playlist)
        time.sleep(0.1)

def playplaylist2(playlist):
    if len(playlist) == 0:
        print("there is no music in the playlist.")
        return


    mixer.init()
    # pygame.display.init()
    # mixer.music.load(playlist[0])
    # mixer.music.queue(playlist[1])
    #
    # mixer.music.play()
    # for i in range(1,len(playlist)):
    #     mixer.music.queue(playlist[i])

    for i, song in enumerate(playlist):
        if i == 0:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.queue(song)

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)




    # while running:
    #     if mixer.music.get_busy() == 0:  # A track has ended
    #         mixer.music.load(playlist[idx])  # Q
    #         mixer.music.play()
    #         idx += 1
    #         if idx == len(playlist):
    #             idx = 0
    #             random.shuffle(playlist)
    #     time.sleep(0.1)

    # # Exception handling.
    # if len(playlist)==0:
    #     return
    # if len(playlist)==1:
    #     mixer.music.load(playlist[0])  # Get the first track from the playlist
    #     mixer.music.queue(playlist[0])
    #     mixer.music.set_endevent(pygame.USEREVENT)  # Setup the end track event
    #     mixer.music.play()  # Play the music
    #
    #     running = True
    #     while running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.USEREVENT:  # A track has ended
    #                 mixer.music.queue(playlist[0])  # Q
    #         time.sleep(0.1)
    #
    # else:
    #
    #     mixer.music.load(playlist[0])  # Get the first track from the playlist
    #     mixer.music.queue(playlist[1])  # Queue the 2nd song
    #     mixer.music.set_endevent(pygame.USEREVENT)  # Setup the end track event
    #     mixer.music.play()  # Play the music
    #     idx = 2
    #     running = True
    #     while running:
    #         if mixer.music.get_busy()==0:  # A track has ended
    #             mixer.music.load(playlist[idx])  # Q
    #             mixer.music.play()
    #             idx += 1
    #             if idx == len(playlist):
    #                 idx = 0
    #                 random.shuffle(playlist)
    #
    #         time.sleep(0.1)

    # mixer.music.load(playlist.pop())  # Get the first track from the playlist
    # # mixer.music.queue(playlist.pop())  # Queue the 2nd song
    # # mixer.music.set_endevent(pygame.USEREVENT)  # Setup the end track event
    # mixer.music.play()  # Play the music
    # running = True
    # while running:
    #     print(playlist)
    #     for event in pygame.event.get():
    #         if event.type == pygame.USEREVENT:  # A track has ended
    #             if len(playlist) > 0:  # If there are more tracks in the queue...
    #                 mixer.music.queue(playlist.pop())  # Q
    #     time.sleep(0.1)
def play_toonz(playlist):
    pygame.mixer.init()

    songNumber = 1
    random.shuffle(playlist)
    pygame.mixer.music.load(playlist[songNumber])
    pygame.mixer.music.play(10)

    for num, song in enumerate(playlist):
        if num == songNumber:
            continue
        print(num)
        pygame.mixer.music.queue(song)

# import concurrent.futures

# def foo(bar):
#     print('hello {}'.format(bar))
#     return 'foo'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future = executor.submit(foo, 'world!')
#     return_value = future.result()
#     print(return_value)

from threading import Thread
playlist = glob.glob('./music2/*.mp3')
playplaylist2(playlist)
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future = executor.submit(playplaylist(playlist))
#     return_value = future.result()
#     print(return_value)


# T = Thread(target=playplaylist(playlist)) # create thread
# T.join()
# T.start() # Launch created thread

loop = asyncio.get_event_loop()
t = threading.Thread(target=playplaylist, args=(playlist,))
t.start()

# mixer.music.pause()