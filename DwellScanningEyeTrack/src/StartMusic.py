from psychopy import sound

# sound1 = sound.Sound('src/punishment_sound.wav')
# sound1.play()
# params = {}
# params['playlist'] = ['src/punishment_sound.wav','src/reward_sound.wav']
# params['musicIdx'] = 0

def playMusic(sound1,params):

    if sound1.status == 0:
        sound1 = sound.Sound(params['playlist'][params['musicIdx']])
        sound1.play()
        print("playing:" + params['playlist'][params['musicIdx']])
        # params['musicIdx'] += 1
        # if params['musicIdx'] >= len(params['playlist']):
        #     params['musicIdx'] = 0
    elif sound1.status == -1:
        params['musicIdx'] += 1
        if params['musicIdx'] >= len(params['playlist']):
            params['musicIdx'] = 0
        sound1 = sound.Sound(params['playlist'][params['musicIdx']])
        sound1.play()
        print("playing:" + params['playlist'][params['musicIdx']])
    elif sound1.status == 2:
        sound1.play()
    return sound1

def pauseMusic(sound1):
    if sound1.status == 1:
        sound1.pause()
    return sound1

# def resumeMusic(sound1):
#     if sound1.status == 2:
#         sound1.play()

def stopMusic(sound1):
    sound1.stop()
    return sound1

