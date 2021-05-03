from psychopy import event,core

def GetKeyPress():
    keys = event.getKeys()
    if keys == ['q'] or keys == ['Q'] or keys == ['Esc']:
        print('Q pressed. Forced Exit.')
        core.quit()
    return keys