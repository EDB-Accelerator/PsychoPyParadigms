from pygame import mixer
import time
from psychopy import core

def playSound(mixer,inFile,Duration):
    startTime = time.time()
    mixer.music.load(inFile)
    mixer.music.play(1)
    midTime = time.time()
    # time.sleep(Duration - (midTime-startTime))
    core.wait(Duration - (midTime-startTime))
    # running = True
    #
    # while running:
    #     time.sleep(0.01)
    #     if not mixer.music.get_busy():
    #         running = False
