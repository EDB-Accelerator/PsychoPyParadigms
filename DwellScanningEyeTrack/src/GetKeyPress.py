from psychopy import event,core
from MusicControl import StopMusic
def GetKeyPress():
    keys = event.getKeys()
    if keys == ['q'] or keys == ['Q'] or keys == ['Esc']:
        print('Q pressed. Forced Exit.')
        StopMusic()
        core.quit()
    return keys