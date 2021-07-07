from psychopy import sound

# params['sound1'] = sound.Sound('src/punishment_sound.wav')
# params['sound1'].play()
# params = {}
# params['playlist'] = ['src/punishment_sound.wav','src/punishment_sound.wav']
# params['musicIdx'] = 0

def playMusic(params):

    if params['sound1'].status == 0:
        params['sound1'] = sound.Sound(params['playlist'][params['musicIdx']])
        params['sound1'].play()
        print("playing:" + params['playlist'][params['musicIdx']])
    elif params['sound1'].status == -1:
        params['musicIdx'] += 1
        if params['musicIdx'] >= len(params['playlist']):
            params['musicIdx'] = 0
        params['sound1'] = sound.Sound(params['playlist'][params['musicIdx']])
        params['sound1'].play()
        print("playing:" + params['playlist'][params['musicIdx']])
    elif params['sound1'].status == 2:
        params['sound1'].play()
    return params['sound1']

def pauseMusic(params):
    if params['sound1'].status == 1:
        params['sound1'].pause()
    return params['sound1']

# def resumeMusic(params['sound1']):
#     if params['sound1'].status == 2:
#         params['sound1'].play()

def stopMusic(params):
    params['sound1'].stop()
    return params['sound1']

