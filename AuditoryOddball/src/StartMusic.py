from pygame import mixer
import time

def playSound(mixer,inFile):

    mixer.music.load(inFile)
    mixer.music.play(1)
    running = True

    while running:
        time.sleep(0.01)
        if not mixer.music.get_busy():
            running = False
