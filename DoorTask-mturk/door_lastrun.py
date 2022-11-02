#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Mon Oct 31 11:54:54 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2021.1.4')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

timer = core.Clock()
widthBank = []
heightBank = []
size_diff = 1/65
for level1 in range(0,101):
    width = 1024 * (0.1 + pow(level1,1.7) * size_diff*0.05)
    height = 768 * (0.1 + pow(level1,1.7) * size_diff*0.05)
    widthBank.append(width)
    heightBank.append(height)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'door'  # from the Builder filename that created this script
expInfo = {'sdan': '', 'session': '001', 'version': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['sdan'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jimmy/github/door/door_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1024,768], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "titleScreen"
titleScreenClock = core.Clock()
key_resp = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='img/title.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(1024, 768),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
import random
def randomGet(start,end):
    return random.uniform(start, end)



# Initialize components for Routine "vasPre"
vasPreClock = core.Clock()
vasPreCount = 0
vasQuestionText = "How anxious do you feel right now?"
vasLabelText1 = 'Not anxious'
vasLabelText2 = 'Very anxious'
slider_2 = visual.Slider(win=win, name='slider_2',
    size=(1.0, 0.1), pos=(0, -0.3), units=None,
    labels=None, ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Yellow', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
vas_question_pre = visual.TextStim(win=win, name='vas_question_pre',
    text='',
    font='Open Sans',
    units='norm', pos=(0, 0.3), height=0.12, wrapWidth=2.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
vas_label1_pre = visual.TextStim(win=win, name='vas_label1_pre',
    text='',
    font='Open Sans',
    units='pix', pos=(-380, -170), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
vas_label2_pre = visual.TextStim(win=win, name='vas_label2_pre',
    text='',
    font='Open Sans',
    units='pix', pos=(380, -170), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_15 = keyboard.Keyboard()

# Initialize components for Routine "vasPreRecord"
vasPreRecordClock = core.Clock()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
count = 0
imgFile = 'instruction/Slide' + str(count) + '.jpg'

key_resp_2 = keyboard.Keyboard()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1024, 768),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "practice"
practiceClock = core.Clock()
key_resp_3 = keyboard.Keyboard()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
level = 50
width = widthBank[level]
height = heightBank[level]
img = visual.ImageStim(win=win, image="img/practice_door.jpg", units="pix", size=(width, height))



# Initialize components for Routine "practiceAnticipation"
practiceAnticipationClock = core.Clock()
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "practiceAward"
practiceAwardClock = core.Clock()
imgAward = visual.ImageStim(
    win=win,
    name='imgAward', units='pix', 
    image='img/practice_outcome.jpg', mask=None,
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "practiceITI"
practiceITIClock = core.Clock()
imageITI = visual.ImageStim(
    win=win,
    name='imageITI', units='pix', 
    image='img/iti.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(1024, 768),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "fortuneWheel"
fortuneWheelClock = core.Clock()
trialsCount = 0
fortuneVideo = 'video/18.mp4'
fortuneWheelResultImg = 'img/fortuneResult18.jpg'

# Initialize components for Routine "fortuneWheelResult"
fortuneWheelResultClock = core.Clock()
key_resp_5 = keyboard.Keyboard()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1024, 768),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "doorImgShuffle"
doorImgShuffleClock = core.Clock()
level = 50
width = widthBank[level]
height = heightBank[level]

doorOpenChanceMap = [0.007, 0.008, 0.009, 0.011, 0.012, 0.014, 0.016, 0.018, 0.02 ,
       0.023, 0.026, 0.029, 0.032, 0.036, 0.04 , 0.045, 0.049, 0.055,
       0.061, 0.067, 0.074, 0.081, 0.089, 0.097, 0.106, 0.115, 0.125,
       0.136, 0.147, 0.159, 0.171, 0.184, 0.198, 0.212, 0.227, 0.242,
       0.258, 0.274, 0.291, 0.309, 0.326, 0.345, 0.363, 0.382, 0.401,
       0.421, 0.44 , 0.46 , 0.48 , 0.5  , 0.52 , 0.54 , 0.56 , 0.579,
       0.599, 0.618, 0.637, 0.655, 0.674, 0.691, 0.709, 0.726, 0.742,
       0.758, 0.773, 0.788, 0.802, 0.816, 0.829, 0.841, 0.853, 0.864,
       0.875, 0.885, 0.894, 0.903, 0.911, 0.919, 0.926, 0.933, 0.939,
       0.945, 0.951, 0.955, 0.96 , 0.964, 0.968, 0.971, 0.974, 0.977,
       0.98 , 0.982, 0.984, 0.986, 0.988, 0.989, 0.991, 0.992, 0.993,
       0.994, 1.   ]
 
if expInfo['version'] == 1:
    imgDir = 'img/doors1/'
    imgList = ['img/doors1/p6r3.jpg', 'img/doors1/p4r1.jpg', 'img/doors1/p2r7.jpg', 'img/doors1/p2r6.jpg', 'img/doors1/p6r2.jpg', 'img/doors1/p4r2.jpg', 'img/doors1/p2r4.jpg', 'img/doors1/p2r5.jpg', 'img/doors1/p4r3.jpg', 'img/doors1/p6r1.jpg', 'img/doors1/p6r5.jpg', 'img/doors1/p4r7.jpg', 'img/doors1/p2r1.jpg', 'img/doors1/p4r6.jpg', 'img/doors1/p6r4.jpg', 'img/doors1/p6r6.jpg', 'img/doors1/p4r4.jpg', 'img/doors1/p2r2.jpg', 'img/doors1/p2r3.jpg', 'img/doors1/p4r5.jpg', 'img/doors1/p6r7.jpg', 'img/doors1/p1r6.jpg', 'img/doors1/p3r4.jpg', 'img/doors1/p5r2.jpg', 'img/doors1/p7r1.jpg', 'img/doors1/p5r3.jpg', 'img/doors1/p3r5.jpg', 'img/doors1/p1r7.jpg', 'img/doors1/p1r5.jpg', 'img/doors1/p3r7.jpg', 'img/doors1/p5r1.jpg', 'img/doors1/p7r3.jpg', 'img/doors1/p7r2.jpg', 'img/doors1/p3r6.jpg', 'img/doors1/p1r4.jpg', 'img/doors1/p3r2.jpg', 'img/doors1/p5r4.jpg', 'img/doors1/p7r6.jpg', 'img/doors1/p7r7.jpg', 'img/doors1/p5r5.jpg', 'img/doors1/p3r3.jpg', 'img/doors1/p1r1.jpg', 'img/doors1/p1r3.jpg', 'img/doors1/p3r1.jpg', 'img/doors1/p5r7.jpg', 'img/doors1/p7r5.jpg', 'img/doors1/p7r4.jpg', 'img/doors1/p5r6.jpg', 'img/doors1/p1r2.jpg']
    pList = ['6', '4', '2', '2', '6', '4', '2', '2', '4', '6', '6', '4', '2', '4', '6', '6', '4', '2', '2', '4', '6', '1', '3', '5', '7', '5', '3', '1', '1', '3', '5', '7', '7', '3', '1', '3', '5', '7', '7', '5', '3', '1', '1', '3', '5', '7', '7', '5', '1']
    rList = ['3', '1', '7', '6', '2', '2', '4', '5', '3', '1', '5', '7', '1', '6', '4', '6', '4', '2', '3', '5', '7', '6', '4', '2', '1', '3', '5', '7', '5', '7', '1', '3', '2', '6', '4', '2', '4', '6', '7', '5', '3', '1', '3', '1', '7', '5', '4', '6', '2']
else:
    imgDir = 'img/doors2/'
    imgList = ['img/doors2/p6r3.jpg', 'img/doors2/p4r1.jpg', 'img/doors2/p2r7.jpg', 'img/doors2/p2r6.jpg', 'img/doors2/p6r2.jpg', 'img/doors2/p4r2.jpg', 'img/doors2/p2r4.jpg', 'img/doors2/p2r5.jpg', 'img/doors2/p4r3.jpg', 'img/doors2/p6r1.jpg', 'img/doors2/p6r5.jpg', 'img/doors2/p4r7.jpg', 'img/doors2/p2r1.jpg', 'img/doors2/p4r6.jpg', 'img/doors2/p6r4.jpg', 'img/doors2/p6r6.jpg', 'img/doors2/p4r4.jpg', 'img/doors2/p2r2.jpg', 'img/doors2/p2r3.jpg', 'img/doors2/p4r5.jpg', 'img/doors2/p6r7.jpg', 'img/doors2/p1r6.jpg', 'img/doors2/p3r4.jpg', 'img/doors2/p5r2.jpg', 'img/doors2/p7r1.jpg', 'img/doors2/p5r3.jpg', 'img/doors2/p3r5.jpg', 'img/doors2/p1r7.jpg', 'img/doors2/p1r5.jpg', 'img/doors2/p3r7.jpg', 'img/doors2/p5r1.jpg', 'img/doors2/p7r3.jpg', 'img/doors2/p7r2.jpg', 'img/doors2/p3r6.jpg', 'img/doors2/p1r4.jpg', 'img/doors2/p3r2.jpg', 'img/doors2/p5r4.jpg', 'img/doors2/p7r6.jpg', 'img/doors2/p7r7.jpg', 'img/doors2/p5r5.jpg', 'img/doors2/p3r3.jpg', 'img/doors2/p1r1.jpg', 'img/doors2/p1r3.jpg', 'img/doors2/p3r1.jpg', 'img/doors2/p5r7.jpg', 'img/doors2/p7r5.jpg', 'img/doors2/p7r4.jpg', 'img/doors2/p5r6.jpg', 'img/doors2/p1r2.jpg']
    pList = ['6', '4', '2', '2', '6', '4', '2', '2', '4', '6', '6', '4', '2', '4', '6', '6', '4', '2', '2', '4', '6', '1', '3', '5', '7', '5', '3', '1', '1', '3', '5', '7', '7', '3', '1', '3', '5', '7', '7', '5', '3', '1', '1', '3', '5', '7', '7', '5', '1']
    rList = ['3', '1', '7', '6', '2', '2', '4', '5', '3', '1', '5', '7', '1', '6', '4', '6', '4', '2', '3', '5', '7', '6', '4', '2', '1', '3', '5', '7', '5', '7', '1', '3', '2', '6', '4', '2', '4', '6', '7', '5', '3', '1', '3', '1', '7', '5', '4', '6', '2']


def shuffle(array):
    import random
    random.shuffle(array)


# Initialize components for Routine "doorStartScreen"
doorStartScreenClock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', units='pix', 
    image='img/start_main_game.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(1024,768),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "doorInit"
doorInitClock = core.Clock()

# Initialize components for Routine "door"
doorClock = core.Clock()
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
key_resp_7 = keyboard.Keyboard()
level = 50
width = widthBank[level]
height = heightBank[level]
imgDoor = visual.ImageStim(win=win, image="img/doors1/p1r1.jpg", units="pix", size=(width, height))


# Initialize components for Routine "doorAnticipation"
doorAnticipationClock = core.Clock()
key_resp_10 = keyboard.Keyboard()

awardImg = "./img/outcomes/1_punishment.jpg"
rewardVSpunishment = "punishment"

# Initialize components for Routine "award"
awardClock = core.Clock()
image_door_award = visual.ImageStim(
    win=win,
    name='image_door_award', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
sound_1 = sound.Sound('A', secs=2.0, stereo=False, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)

# Initialize components for Routine "noAward"
noAwardClock = core.Clock()

# Initialize components for Routine "iti"
itiClock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='img/iti.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "restScreen"
restScreenClock = core.Clock()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', units='pix', 
    image='img/rest.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(1024,768),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "vas"
vasClock = core.Clock()
slider = visual.Slider(win=win, name='slider',
    size=(1.0, 0.1), pos=(0, -0.3), units=None,
    labels=None, ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Yellow', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=0, readOnly=False)
vas_question = visual.TextStim(win=win, name='vas_question',
    text='',
    font='Open Sans',
    units='norm', pos=(0, 0.3), height=0.12, wrapWidth=3.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
vas_label1 = visual.TextStim(win=win, name='vas_label1',
    text='',
    font='Open Sans',
    units='pix', pos=(-380, -170), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
vas_label2 = visual.TextStim(win=win, name='vas_label2',
    text='',
    font='Open Sans',
    units='pix', pos=(380, -170), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_14 = keyboard.Keyboard()

# Initialize components for Routine "vasRecord"
vasRecordClock = core.Clock()

# Initialize components for Routine "afterVAS"
afterVASClock = core.Clock()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', units='pix', 
    image='img/after_VAS.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(1024,768),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "finalReward"
finalRewardClock = core.Clock()
image_8 = visual.ImageStim(
    win=win,
    name='image_8', units='pix', 
    image='img/finalReward.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(1024,768),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_13 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_12 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_12')
thisExp.addLoop(trials_12)  # add the loop to the experiment
thisTrial_12 = trials_12.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
if thisTrial_12 != None:
    for paramName in thisTrial_12:
        exec('{} = thisTrial_12[paramName]'.format(paramName))

for thisTrial_12 in trials_12:
    currentLoop = trials_12
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
    if thisTrial_12 != None:
        for paramName in thisTrial_12:
            exec('{} = thisTrial_12[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "titleScreen"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    titleScreenComponents = [key_resp, image]
    for thisComponent in titleScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    titleScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "titleScreen"-------
    while continueRoutine:
        # get current time
        t = titleScreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=titleScreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in titleScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "titleScreen"-------
    for thisComponent in titleScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_12.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_12.addData('key_resp.rt', key_resp.rt)
    trials_12.addData('sdan','')
    trials_12.addData('session','')
    trials_12.addData('version','')
    trials_12.addData('date','')
    trials_12.addData('section','title screen displayed')
    trials_12.addData('displayed','')
    trials_12.addData('vas_label','')
    trials_12.addData('vas_response','')
    trials_12.addData('door(r)','')
    trials_12.addData('door(p)','')
    trials_12.addData('door_locked_level','')
    trials_12.addData('award type','')
    trials_12.addData('award','')
    trials_12.addData('door duration (sec)','')
    trials_12.addData('door anticipation time (sec)','')
    trials_12.addData('award displayed duration (sec)','')
    trials_12.addData('iti duration (sec)','')
    
    # the Routine "titleScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_12'


# set up handler to look after randomisation of conditions etc
trials_1 = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_1')
thisExp.addLoop(trials_1)  # add the loop to the experiment
thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
if thisTrial_1 != None:
    for paramName in thisTrial_1:
        exec('{} = thisTrial_1[paramName]'.format(paramName))

for thisTrial_1 in trials_1:
    currentLoop = trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            exec('{} = thisTrial_1[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_13 = data.TrialHandler(nReps=1000.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_13')
    thisExp.addLoop(trials_13)  # add the loop to the experiment
    thisTrial_13 = trials_13.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
    if thisTrial_13 != None:
        for paramName in thisTrial_13:
            exec('{} = thisTrial_13[paramName]'.format(paramName))
    
    for thisTrial_13 in trials_13:
        currentLoop = trials_13
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
        if thisTrial_13 != None:
            for paramName in thisTrial_13:
                exec('{} = thisTrial_13[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "vasPre"-------
        continueRoutine = True
        # update component parameters for each repeat
        #print(vasPreCount)
        sliderStarted = False
        slider_2.reset()
        vas_question_pre.setText(vasQuestionText)
        vas_label1_pre.setText(vasLabelText1)
        vas_label2_pre.setText(vasLabelText2)
        key_resp_15.keys = []
        key_resp_15.rt = []
        _key_resp_15_allKeys = []
        # keep track of which components have finished
        vasPreComponents = [slider_2, vas_question_pre, vas_label1_pre, vas_label2_pre, key_resp_15]
        for thisComponent in vasPreComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        vasPreClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "vasPre"-------
        while continueRoutine:
            # get current time
            t = vasPreClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=vasPreClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if slider_2.markerPos:
                sliderStarted = True
            
            # *slider_2* updates
            if slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_2.frameNStart = frameN  # exact frame index
                slider_2.tStart = t  # local t and not account for scr refresh
                slider_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
                slider_2.setAutoDraw(True)
            
            # *vas_question_pre* updates
            if vas_question_pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vas_question_pre.frameNStart = frameN  # exact frame index
                vas_question_pre.tStart = t  # local t and not account for scr refresh
                vas_question_pre.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vas_question_pre, 'tStartRefresh')  # time at next scr refresh
                vas_question_pre.setAutoDraw(True)
            
            # *vas_label1_pre* updates
            if vas_label1_pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vas_label1_pre.frameNStart = frameN  # exact frame index
                vas_label1_pre.tStart = t  # local t and not account for scr refresh
                vas_label1_pre.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vas_label1_pre, 'tStartRefresh')  # time at next scr refresh
                vas_label1_pre.setAutoDraw(True)
            
            # *vas_label2_pre* updates
            if vas_label2_pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vas_label2_pre.frameNStart = frameN  # exact frame index
                vas_label2_pre.tStart = t  # local t and not account for scr refresh
                vas_label2_pre.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vas_label2_pre, 'tStartRefresh')  # time at next scr refresh
                vas_label2_pre.setAutoDraw(True)
            
            # *key_resp_15* updates
            waitOnFlip = False
            if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_15.frameNStart = frameN  # exact frame index
                key_resp_15.tStart = t  # local t and not account for scr refresh
                key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
                key_resp_15.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_15.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_15_allKeys.extend(theseKeys)
                if len(_key_resp_15_allKeys):
                    key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
                    key_resp_15.rt = _key_resp_15_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in vasPreComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "vasPre"-------
        for thisComponent in vasPreComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #print(slider_2.getRating())
        #if slider_2.getRating() != None and slider_2.getRating() != '':
        if sliderStarted:
            trials_13.finished= True
        #if slider_2.status != NOT_STARTED:
            
        trials_13.addData('slider_2.response', slider_2.getRating())
        trials_13.addData('slider_2.rt', slider_2.getRT())
        # check responses
        if key_resp_15.keys in ['', [], None]:  # No response was made
            key_resp_15.keys = None
        trials_13.addData('key_resp_15.keys',key_resp_15.keys)
        if key_resp_15.keys != None:  # we had a response
            trials_13.addData('key_resp_15.rt', key_resp_15.rt)
        trials_13.addData('key_resp_15.started', key_resp_15.tStartRefresh)
        trials_13.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
        # the Routine "vasPre" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1000.0 repeats of 'trials_13'
    
    
    # ------Prepare to start Routine "vasPreRecord"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    vasPreRecordComponents = []
    for thisComponent in vasPreRecordComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    vasPreRecordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "vasPreRecord"-------
    while continueRoutine:
        # get current time
        t = vasPreRecordClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=vasPreRecordClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vasPreRecordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "vasPreRecord"-------
    for thisComponent in vasPreRecordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_1.addData('displayed', vasQuestionText)
    trials_1.addData('vas_response',slider_2.getRating())
    trials_1.addData('vas_label', vasLabelText1 + ',' + vasLabelText2)
    trials_1.addData('section','VAS')
    if vasPreCount == 0:
        vasLabelText1= 'Not at all'
        vasLabelText2  = 'Very much'
        vasQuestionText = "How much do you feel like taking part in the task?"
    if vasPreCount == 1:
        vasLabelText1 = 'Not at all tired'
        vasLabelText2  = 'Very tired'
        vasQuestionText = "How tired are you right now?"
    if vasPreCount == 2:
        vasLabelText1= 'Worst mood ever'
        vasLabelText2 = 'Best mood ever'
        vasQuestionText = "Think about your mood right now. \nHow would you describe it?"
    vasPreCount +=1
    # the Routine "vasPreRecord" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'trials_1'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=10000.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    imgFile = 'instruction/Slide' + str(count) + '.jpg'
    
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    image_2.setImage(imgFile)
    # keep track of which components have finished
    instructionComponents = [key_resp_2, image_2]
    for thisComponent in instructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instruction"-------
    while continueRoutine:
        # get current time
        t = instructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space', 'r', 'y', 'n'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruction"-------
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('section','Instruction (page:' + str(count)+')')
    trials_2.addData('displayed',imgFile)
    if count == 0:
        if (key_resp_2.keys) == 'y' or (key_resp_2.keys) == 'Y':
            count += 1
        elif (key_resp_2.keys) == 'n' or (key_resp_2.keys) == 'N':
            trials_2.finished=True
    elif count==16:
        if (key_resp_2.keys) == 'r' or (key_resp_2.keys) == 'R':
            count=1
        else:
            trials_2.finished=True
    else:
        if key_resp_2.keys == 'space':
            count+=1       
          
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10000.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    img.setAutoDraw(False);
    width = widthBank[level]
    height = heightBank[level]
    img.size = [width,height]
    #img.size = (1024,768)
    level = 50
    img.setAutoDraw(True);
    
    practiceTrialStartTime = timer.getTime()
    #print(timer.getTime())
    # keep track of which components have finished
    practiceComponents = [key_resp_3, mouse]
    for thisComponent in practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice"-------
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        #print("left:")
        #print(mouse.getPressed()[0])
        #print("right:")
        #print(mouse.getPressed()[2])
        #print(str(mouse.getPressed()[0])+','+str(mouse.getPressed()[2]))
        #if mouse.getPressed()[0] == 1:
        #    level += 1
        #    level = min(100,level)
        #if mouse.getPressed()[2] == 1:
        #    level -= 1
        #    level = max(0,level)
        #print(level)
        
        if timer.getTime() - practiceTrialStartTime > 10:
        #    trials.finished=True
            finalWidth = width
            finalHeight = height
            continueRoutine = False
        
        if mouse.getPressed()[0] == 1:
            level += 1
            level = min(100,level)
        elif mouse.getPressed()[2] == 1:
            level -= 1
            level = max(0,level)
        #print(level)
        img.setAutoDraw(False);
        #img.setSize((img.size[0]*level/50,img.size[1]*level/50))
        width = widthBank[level]
        height = heightBank[level]
        #img.size = (1024*level/50,768*level/50)
        img.size = [width,height]
        img.setAutoDraw(True);
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_3.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_3.addData('key_resp_3.rt', key_resp_3.rt)
    # store data for trials_3 (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    trials_3.addData('mouse.x', x)
    trials_3.addData('mouse.y', y)
    trials_3.addData('mouse.leftButton', buttons[0])
    trials_3.addData('mouse.midButton', buttons[1])
    trials_3.addData('mouse.rightButton', buttons[2])
    trials_3.addData('door locked level', level)
    trials_3.addData('door duration (sec)',str(timer.getTime() - practiceTrialStartTime))
    trials_3.addData('displayed',"img/practice_door.jpg")
    width = widthBank[level]
    height = heightBank[level]
    
    randomDuration = randomGet(1.5, 3.5)
    randomAnticipation = randomGet(2, 4)
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practiceAnticipation"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    routineStartTime = timer.getTime() 
    # keep track of which components have finished
    practiceAnticipationComponents = [key_resp_9]
    for thisComponent in practiceAnticipationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceAnticipationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceAnticipation"-------
    while continueRoutine:
        # get current time
        t = practiceAnticipationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceAnticipationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['qq'], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
        if timer.getTime() - routineStartTime > randomAnticipation:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceAnticipationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceAnticipation"-------
    for thisComponent in practiceAnticipationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    trials_3.addData('door anticipation time (sec)',str(timer.getTime() - routineStartTime))
    
    # the Routine "practiceAnticipation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practiceAward"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    imgAward.setPos((0, -height * 0.028))
    imgAward.setSize((width* 0.235, height* 0.464))
    routineStartTime = timer.getTime() 
    
    # keep track of which components have finished
    practiceAwardComponents = [imgAward]
    for thisComponent in practiceAwardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceAwardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceAward"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceAwardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceAwardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imgAward* updates
        if imgAward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imgAward.frameNStart = frameN  # exact frame index
            imgAward.tStart = t  # local t and not account for scr refresh
            imgAward.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imgAward, 'tStartRefresh')  # time at next scr refresh
            imgAward.setAutoDraw(True)
        if imgAward.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imgAward.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imgAward.tStop = t  # not accounting for scr refresh
                imgAward.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imgAward, 'tStopRefresh')  # time at next scr refresh
                imgAward.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceAwardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceAward"-------
    for thisComponent in practiceAwardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('award displayed duration (sec)',str(timer.getTime() - routineStartTime))
    
    
    # ------Prepare to start Routine "practiceITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    img.setAutoDraw(False)
    imgAward.setAutoDraw(False)
    routineStartTime = timer.getTime() 
    # keep track of which components have finished
    practiceITIComponents = [imageITI]
    for thisComponent in practiceITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceITI"-------
    while continueRoutine:
        # get current time
        t = practiceITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageITI* updates
        if imageITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageITI.frameNStart = frameN  # exact frame index
            imageITI.tStart = t  # local t and not account for scr refresh
            imageITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageITI, 'tStartRefresh')  # time at next scr refresh
            imageITI.setAutoDraw(True)
        if imageITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageITI.tStartRefresh + randomDuration-frameTolerance:
                # keep track of stop time/frame for later
                imageITI.tStop = t  # not accounting for scr refresh
                imageITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageITI, 'tStopRefresh')  # time at next scr refresh
                imageITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceITI"-------
    for thisComponent in practiceITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('iti duration (sec)',str(timer.getTime() - routineStartTime))
    trials_3.addData('section','Practice')
    # the Routine "practiceITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_5 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_5')
    thisExp.addLoop(trials_5)  # add the loop to the experiment
    thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    for thisTrial_5 in trials_5:
        currentLoop = trials_5
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                exec('{} = thisTrial_5[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fortuneWheel"-------
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        movie = visual.MovieStim3(
            win=win, name='movie',units='pix', 
            noAudio = False,
            filename=fortuneVideo,
            ori=0.0, pos=(0, 0), opacity=None,
            loop=False,
            size=(366,457),
            depth=0.0,
            )
        # keep track of which components have finished
        fortuneWheelComponents = [movie]
        for thisComponent in fortuneWheelComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fortuneWheelClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fortuneWheel"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fortuneWheelClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fortuneWheelClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *movie* updates
            if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                movie.frameNStart = frameN  # exact frame index
                movie.tStart = t  # local t and not account for scr refresh
                movie.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
                movie.setAutoDraw(True)
            if movie.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > movie.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    movie.tStop = t  # not accounting for scr refresh
                    movie.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(movie, 'tStopRefresh')  # time at next scr refresh
                    movie.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fortuneWheelComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fortuneWheel"-------
        for thisComponent in fortuneWheelComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        movie.stop()
        if trialsCount == 0:
            fortuneVideo = 'video/16.mp4'
        elif trialsCount == 1:
            fortuneVideo = 'video/16b.mp4'
        trials_5.addData('section','Playing Fortune Wheel')
        trials_5.addData('displayed',fortuneVideo)
        
        
        if trialsCount == 0:
            fortuneWheelResultImg = 'img/fortuneResult18.jpg'
        elif trialsCount == 1:
            fortuneWheelResultImg = 'img/fortuneResult16.jpg'
        elif trialsCount == 2:
            fortuneWheelResultImg = 'img/fortuneResult16.jpg'
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_5'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_7 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_7')
    thisExp.addLoop(trials_7)  # add the loop to the experiment
    thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7:
            exec('{} = thisTrial_7[paramName]'.format(paramName))
    
    for thisTrial_7 in trials_7:
        currentLoop = trials_7
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
        if thisTrial_7 != None:
            for paramName in thisTrial_7:
                exec('{} = thisTrial_7[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fortuneWheelResult"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        image_3.setImage(fortuneWheelResultImg)
        # keep track of which components have finished
        fortuneWheelResultComponents = [key_resp_5, image_3]
        for thisComponent in fortuneWheelResultComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fortuneWheelResultClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fortuneWheelResult"-------
        while continueRoutine:
            # get current time
            t = fortuneWheelResultClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fortuneWheelResultClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fortuneWheelResultComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fortuneWheelResult"-------
        for thisComponent in fortuneWheelResultComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials_7.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials_7.addData('key_resp_5.rt', key_resp_5.rt)
        trials_7.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        trials_7.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        trials_7.addData('image_3.started', image_3.tStartRefresh)
        trials_7.addData('image_3.stopped', image_3.tStopRefresh)
        trials_7.addData('section','Fortune Wheel Result displayed')
        trials_7.addData('displayed',fortuneWheelResultImg)
        # the Routine "fortuneWheelResult" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_7'
    
    
    # ------Prepare to start Routine "doorImgShuffle"-------
    continueRoutine = True
    # update component parameters for each repeat
    imgOrder = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    shuffle(imgOrder)
    #continueRoutine = False
    # keep track of which components have finished
    doorImgShuffleComponents = []
    for thisComponent in doorImgShuffleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    doorImgShuffleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "doorImgShuffle"-------
    while continueRoutine:
        # get current time
        t = doorImgShuffleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=doorImgShuffleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in doorImgShuffleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "doorImgShuffle"-------
    for thisComponent in doorImgShuffleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials4Count = 0
    # the Routine "doorImgShuffle" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_8 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_8')
    thisExp.addLoop(trials_8)  # add the loop to the experiment
    thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8:
            exec('{} = thisTrial_8[paramName]'.format(paramName))
    
    for thisTrial_8 in trials_8:
        currentLoop = trials_8
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
        if thisTrial_8 != None:
            for paramName in thisTrial_8:
                exec('{} = thisTrial_8[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "doorStartScreen"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        # keep track of which components have finished
        doorStartScreenComponents = [image_4, key_resp_8]
        for thisComponent in doorStartScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        doorStartScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "doorStartScreen"-------
        while continueRoutine:
            # get current time
            t = doorStartScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=doorStartScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_4* updates
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                image_4.setAutoDraw(True)
            
            # *key_resp_8* updates
            waitOnFlip = False
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                    key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in doorStartScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "doorStartScreen"-------
        for thisComponent in doorStartScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
        trials_8.addData('key_resp_8.keys',key_resp_8.keys)
        if key_resp_8.keys != None:  # we had a response
            trials_8.addData('key_resp_8.rt', key_resp_8.rt)
        trials_8.addData('section','Doorgame Start Screen Displayed')
        trials_8.addData('displayed','img/start_main_game.jpg')
        # the Routine "doorStartScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_8'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "doorInit"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        doorInitComponents = []
        for thisComponent in doorInitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        doorInitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "doorInit"-------
        while continueRoutine:
            # get current time
            t = doorInitClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=doorInitClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in doorInitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "doorInit"-------
        for thisComponent in doorInitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        doorImgIdx = imgOrder[trials4Count]
        doorImg = imgList[doorImgIdx]
        p = pList[doorImgIdx]
        r = rList[doorImgIdx]
        #imgList = ['./img/doors1/p6r3.jpg', './img/doors1/p4r1.jpg', './img/doors1/p2r7.jpg', './img/doors1/p2r6.jpg', './img/doors1/p6r2.jpg', './img/doors1/p4r2.jpg', './img/doors1/p2r4.jpg', './img/doors1/p2r5.jpg', './img/doors1/p4r3.jpg', './img/doors1/p6r1.jpg', './img/doors1/p6r5.jpg', './img/doors1/p4r7.jpg', './img/doors1/p2r1.jpg', './img/doors1/p4r6.jpg', './img/doors1/p6r4.jpg', './img/doors1/p6r6.jpg', './img/doors1/p4r4.jpg', './img/doors1/p2r2.jpg', './img/doors1/p2r3.jpg', './img/doors1/p4r5.jpg', './img/doors1/p6r7.jpg', './img/doors1/p1r6.jpg', './img/doors1/p3r4.jpg', './img/doors1/p5r2.jpg', './img/doors1/p7r1.jpg', './img/doors1/p5r3.jpg', './img/doors1/p3r5.jpg', './img/doors1/p1r7.jpg', './img/doors1/p1r5.jpg', './img/doors1/p3r7.jpg', './img/doors1/p5r1.jpg', './img/doors1/p7r3.jpg', './img/doors1/p7r2.jpg', './img/doors1/p3r6.jpg', './img/doors1/p1r4.jpg', './img/doors1/p3r2.jpg', './img/doors1/p5r4.jpg', './img/doors1/p7r6.jpg', './img/doors1/p7r7.jpg', './img/doors1/p5r5.jpg', './img/doors1/p3r3.jpg', './img/doors1/p1r1.jpg', './img/doors1/p1r3.jpg', './img/doors1/p3r1.jpg', './img/doors1/p5r7.jpg', './img/doors1/p7r5.jpg', './img/doors1/p7r4.jpg', './img/doors1/p5r6.jpg', './img/doors1/p1r2.jpg']
        #    pList = ['6', '4', '2', '2', '6', '4', '2', '2', '4', '6', '6', '4', '2', '4', '6', '6', '4', '2', '2', '4', '6', '1', '3', '5', '7', '5', '3', '1', '1', '3', '5', '7', '7', '3', '1', '3', '5', '7', '7', '5', '3', '1', '1', '3', '5', '7', '7', '5', '1']
        #    rList = ['3', '1', '7', '6', '2', '2', '4', '5', '3', '1', '5', '7', '1', '6', '4', '6', '4', '2', '3', '5', '7', '6', '4', '2', '1', '3', '5', '7', '5', '7', '1', '3', '2', '6', '4', '2', '4', '6', '7', '5', '3', '1', '3', '1', '7', '5', '4', '6', '2']
        #
        randomDuration = randomGet(1.5, 3.5)
        randomAnticipation = randomGet(2, 4)
        
        trials_4.addData('displayed',doorImg)
        trials_4.addData('door(r)',r)
        trials_4.addData('door(p)',p)
        # the Routine "doorInit" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "door"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_2
        gotValidClick = False  # until a click is received
        key_resp_7.keys = []
        key_resp_7.rt = []
        _key_resp_7_allKeys = []
        level = 50
        width = widthBank[level]
        height = heightBank[level]
        imgDoor = visual.ImageStim(win=win, image=doorImg, units="pix", size=(width, height))
        imgDoor.setAutoDraw(False);
        img.size = [width,height]
        imgDoor.setAutoDraw(True);
        
        doorTrialStartTime = timer.getTime()
        #print(timer.getTime())
        # keep track of which components have finished
        doorComponents = [mouse_2, key_resp_7]
        for thisComponent in doorComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        doorClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "door"-------
        while continueRoutine:
            # get current time
            t = doorClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=doorClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_7* updates
            waitOnFlip = False
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            if timer.getTime() - doorTrialStartTime > 10:
                finalWidth = width
                finalHeight = height
                continueRoutine = False
            
            if mouse.getPressed()[0] == 1:
                level += 1
                level = min(100,level)
            elif mouse.getPressed()[2] == 1:
                level -= 1
                level = max(0,level)
            
            img.setAutoDraw(False);
            width = widthBank[level]
            height = heightBank[level]
            imgDoor.size = [width,height]
            imgDoor.setAutoDraw(True);
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in doorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "door"-------
        for thisComponent in doorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials_4 (TrialHandler)
        x, y = mouse_2.getPos()
        buttons = mouse_2.getPressed()
        trials_4.addData('mouse_2.x', x)
        trials_4.addData('mouse_2.y', y)
        trials_4.addData('mouse_2.leftButton', buttons[0])
        trials_4.addData('mouse_2.midButton', buttons[1])
        trials_4.addData('mouse_2.rightButton', buttons[2])
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        trials_4.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            trials_4.addData('key_resp_7.rt', key_resp_7.rt)
        trials_4.addData('door locked level', level)
        trials_4.addData('door duration (sec)',str(timer.getTime() - doorTrialStartTime))
        
        width = widthBank[level]
        height = heightBank[level]
        
        randomDuration = randomGet(1.5, 3.5)
        # the Routine "door" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "doorAnticipation"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_10.keys = []
        key_resp_10.rt = []
        _key_resp_10_allKeys = []
        routineStartTime = timer.getTime() 
        
        doorOpenChance = doorOpenChanceMap[level]
        randomNum = randomGet(0,1)
        door_opened = False
        soundFile = 'sound/reward.wav'
        
        if randomNum > doorOpenChance:
            door_opened = False
            trials_4.addData('award type','door not opened')
            trials_4.addData('award','0')
        else:
            door_opened = True
        if randomGet(0,1) > 0.5:
            rewardVSpunishment = "punishment"
            awardImg = "img/outcomes/" + p + "_punishment.jpg"
            soundFile = 'sound/punishment.wav'
            trials_4.addData('award type',"punishment")
            trials_4.addData('award','-'+p)
        else:
            rewardVSpunishment = "reward"
            awardImg = "img/outcomes/" + r + "_reward.jpg"
            trials_4.addData('award type',"reward")
            trials_4.addData('award','+'+r)
        # keep track of which components have finished
        doorAnticipationComponents = [key_resp_10]
        for thisComponent in doorAnticipationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        doorAnticipationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "doorAnticipation"-------
        while continueRoutine:
            # get current time
            t = doorAnticipationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=doorAnticipationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_10* updates
            waitOnFlip = False
            if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_10.frameNStart = frameN  # exact frame index
                key_resp_10.tStart = t  # local t and not account for scr refresh
                key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                key_resp_10.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_10.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_10.getKeys(keyList=['qq'], waitRelease=False)
                _key_resp_10_allKeys.extend(theseKeys)
                if len(_key_resp_10_allKeys):
                    key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                    key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            if timer.getTime() - routineStartTime > randomAnticipation:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in doorAnticipationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "doorAnticipation"-------
        for thisComponent in doorAnticipationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_10.keys in ['', [], None]:  # No response was made
            key_resp_10.keys = None
        trials_4.addData('key_resp_10.keys',key_resp_10.keys)
        if key_resp_10.keys != None:  # we had a response
            trials_4.addData('key_resp_10.rt', key_resp_10.rt)
        trials_4.addData('door anticipation time (sec)',str(timer.getTime() - routineStartTime))
        
        # the Routine "doorAnticipation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "award"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        image_door_award.setPos((0, -height * 0.028))
        image_door_award.setSize((width * 0.235, height * 0.464))
        image_door_award.setImage(awardImg)
        #print(door_opened)
        #print(awardImg)
        if door_opened == True:
            routineStartTime = timer.getTime() 
        #    print(continueRoutine)
        else:
            continueRoutine = False
        
        
        sound_1.setSound(soundFile, secs=2.0, hamming=True)
        sound_1.setVolume(1.0, log=False)
        # keep track of which components have finished
        awardComponents = [image_door_award, sound_1]
        for thisComponent in awardComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        awardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "award"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = awardClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=awardClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_door_award* updates
            if image_door_award.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_door_award.frameNStart = frameN  # exact frame index
                image_door_award.tStart = t  # local t and not account for scr refresh
                image_door_award.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_door_award, 'tStartRefresh')  # time at next scr refresh
                image_door_award.setAutoDraw(True)
            if image_door_award.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_door_award.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_door_award.tStop = t  # not accounting for scr refresh
                    image_door_award.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_door_award, 'tStopRefresh')  # time at next scr refresh
                    image_door_award.setAutoDraw(False)
            # start/stop sound_1
            if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                sound_1.play(when=win)  # sync with win flip
            if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_1.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_1.tStop = t  # not accounting for scr refresh
                    sound_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                    sound_1.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in awardComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "award"-------
        for thisComponent in awardComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if door_opened == True:
            trials_4.addData(awardImg + ' displayed duration (sec)',str(timer.getTime() - routineStartTime))
        
        sound_1.stop()  # ensure sound has stopped at end of routine
        
        # ------Prepare to start Routine "noAward"-------
        continueRoutine = True
        # update component parameters for each repeat
        if door_opened == False:
            routineStartTime = timer.getTime() 
        else:
            continueRoutine = True
        
        # keep track of which components have finished
        noAwardComponents = []
        for thisComponent in noAwardComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        noAwardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "noAward"-------
        while continueRoutine:
            # get current time
            t = noAwardClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=noAwardClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if timer.getTime() - routineStartTime > 2:
               continueRoutine = True
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in noAwardComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "noAward"-------
        for thisComponent in noAwardComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if door_opened == False:
            trials_4.addData('award (not displayed) displayed duration (sec)',str(timer.getTime() - routineStartTime))
        
        # the Routine "noAward" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "iti"-------
        continueRoutine = True
        # update component parameters for each repeat
        imgDoor.setAutoDraw(False)
        image_door_award.setAutoDraw(False)
        routineStartTime = timer.getTime() 
        # keep track of which components have finished
        itiComponents = [image_5]
        for thisComponent in itiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        itiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "iti"-------
        while continueRoutine:
            # get current time
            t = itiClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=itiClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_5* updates
            if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_5.frameNStart = frameN  # exact frame index
                image_5.tStart = t  # local t and not account for scr refresh
                image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                image_5.setAutoDraw(True)
            if image_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_5.tStartRefresh + randomDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    image_5.tStop = t  # not accounting for scr refresh
                    image_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
                    image_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "iti"-------
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_4.addData('section','Door Game (playing main game)')
        trials4Count += 1
        trials_4.addData('iti duration (sec)',str(timer.getTime() - routineStartTime))
        
        # the Routine "iti" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'trials_4'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_9 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_9')
    thisExp.addLoop(trials_9)  # add the loop to the experiment
    thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
    if thisTrial_9 != None:
        for paramName in thisTrial_9:
            exec('{} = thisTrial_9[paramName]'.format(paramName))
    
    for thisTrial_9 in trials_9:
        currentLoop = trials_9
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
        if thisTrial_9 != None:
            for paramName in thisTrial_9:
                exec('{} = thisTrial_9[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "restScreen"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_11.keys = []
        key_resp_11.rt = []
        _key_resp_11_allKeys = []
        # keep track of which components have finished
        restScreenComponents = [image_6, key_resp_11]
        for thisComponent in restScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        restScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "restScreen"-------
        while continueRoutine:
            # get current time
            t = restScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=restScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_6* updates
            if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_6.frameNStart = frameN  # exact frame index
                image_6.tStart = t  # local t and not account for scr refresh
                image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                image_6.setAutoDraw(True)
            
            # *key_resp_11* updates
            waitOnFlip = False
            if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_11.frameNStart = frameN  # exact frame index
                key_resp_11.tStart = t  # local t and not account for scr refresh
                key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
                key_resp_11.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_11.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_11_allKeys.extend(theseKeys)
                if len(_key_resp_11_allKeys):
                    key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                    key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in restScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "restScreen"-------
        for thisComponent in restScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_11.keys in ['', [], None]:  # No response was made
            key_resp_11.keys = None
        trials_9.addData('key_resp_11.keys',key_resp_11.keys)
        if key_resp_11.keys != None:  # we had a response
            trials_9.addData('key_resp_11.rt', key_resp_11.rt)
        trials_9.addData('section','Rest Screen Displayed')
        trials_9.addData('displayed','img/rest.jpg')
        vasPreCount = 0
        vasQuestionText = "How anxious do you feel right now?"
        vasLabelText1 = 'Not anxious'
        vasLabelText2 = 'Very anxious'
        # the Routine "restScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_9'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_6 = data.TrialHandler(nReps=4.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_6')
    thisExp.addLoop(trials_6)  # add the loop to the experiment
    thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    for thisTrial_6 in trials_6:
        currentLoop = trials_6
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
        if thisTrial_6 != None:
            for paramName in thisTrial_6:
                exec('{} = thisTrial_6[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials_14 = data.TrialHandler(nReps=1000.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_14')
        thisExp.addLoop(trials_14)  # add the loop to the experiment
        thisTrial_14 = trials_14.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
        if thisTrial_14 != None:
            for paramName in thisTrial_14:
                exec('{} = thisTrial_14[paramName]'.format(paramName))
        
        for thisTrial_14 in trials_14:
            currentLoop = trials_14
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
            if thisTrial_14 != None:
                for paramName in thisTrial_14:
                    exec('{} = thisTrial_14[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "vas"-------
            continueRoutine = True
            # update component parameters for each repeat
            slider.reset()
            vas_question.setText(vasQuestionText)
            #print(vasPreCount,vasQuestionText)
            #i
            sliderStarted = False
            vas_label1.setText(vasLabelText1)
            vas_label2.setText(vasLabelText2)
            key_resp_14.keys = []
            key_resp_14.rt = []
            _key_resp_14_allKeys = []
            # keep track of which components have finished
            vasComponents = [slider, vas_question, vas_label1, vas_label2, key_resp_14]
            for thisComponent in vasComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            vasClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "vas"-------
            while continueRoutine:
                # get current time
                t = vasClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=vasClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *slider* updates
                if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    slider.frameNStart = frameN  # exact frame index
                    slider.tStart = t  # local t and not account for scr refresh
                    slider.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                    slider.setAutoDraw(True)
                
                # *vas_question* updates
                if vas_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vas_question.frameNStart = frameN  # exact frame index
                    vas_question.tStart = t  # local t and not account for scr refresh
                    vas_question.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vas_question, 'tStartRefresh')  # time at next scr refresh
                    vas_question.setAutoDraw(True)
                if slider.markerPos:
                    sliderStarted = True
                
                # *vas_label1* updates
                if vas_label1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vas_label1.frameNStart = frameN  # exact frame index
                    vas_label1.tStart = t  # local t and not account for scr refresh
                    vas_label1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vas_label1, 'tStartRefresh')  # time at next scr refresh
                    vas_label1.setAutoDraw(True)
                
                # *vas_label2* updates
                if vas_label2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vas_label2.frameNStart = frameN  # exact frame index
                    vas_label2.tStart = t  # local t and not account for scr refresh
                    vas_label2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vas_label2, 'tStartRefresh')  # time at next scr refresh
                    vas_label2.setAutoDraw(True)
                
                # *key_resp_14* updates
                waitOnFlip = False
                if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_14.frameNStart = frameN  # exact frame index
                    key_resp_14.tStart = t  # local t and not account for scr refresh
                    key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
                    key_resp_14.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_14.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
                    _key_resp_14_allKeys.extend(theseKeys)
                    if len(_key_resp_14_allKeys):
                        key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                        key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in vasComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "vas"-------
            for thisComponent in vasComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_14.addData('slider.response', slider.getRating())
            #print(slider_2.getRating())
            #if slider.getRating() != None and slider.getRating() != '':
            if sliderStarted:
                trials_14.finished= True
                
            #if slider.status != NOT_STARTED:
            #    trials_14.finished= True
            
            
            # check responses
            if key_resp_14.keys in ['', [], None]:  # No response was made
                key_resp_14.keys = None
            trials_14.addData('key_resp_14.keys',key_resp_14.keys)
            if key_resp_14.keys != None:  # we had a response
                trials_14.addData('key_resp_14.rt', key_resp_14.rt)
            # the Routine "vas" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1000.0 repeats of 'trials_14'
        
        
        # ------Prepare to start Routine "vasRecord"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        vasRecordComponents = []
        for thisComponent in vasRecordComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        vasRecordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "vasRecord"-------
        while continueRoutine:
            # get current time
            t = vasRecordClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=vasRecordClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in vasRecordComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "vasRecord"-------
        for thisComponent in vasRecordComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_6.addData('displayed', vasQuestionText)
        trials_6.addData('vas_response',slider.getRating())
        trials_6.addData('vas_label', vasLabelText1 + ',' + vasLabelText2)
        trials_6.addData('section','VAS')
        if vasPreCount == 0:
            vasLabelText1= 'Not at all'
            vasLabelText2  = 'Very much'
            vasQuestionText = "How much do you feel like taking part in the task?"
        elif vasPreCount == 1:
            vasLabelText1 = 'Not at all tired'
            vasLabelText2  = 'Very tired'
            vasQuestionText = "How tired are you right now?"
        elif vasPreCount == 2:
            vasLabelText1= 'Worst mood ever'
            vasLabelText2 = 'Best mood ever'
            vasQuestionText = "Think about your mood right now. \nHow would you describe it?"
        vasPreCount +=1
        
        # the Routine "vasRecord" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 4.0 repeats of 'trials_6'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_10 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_10')
    thisExp.addLoop(trials_10)  # add the loop to the experiment
    thisTrial_10 = trials_10.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
    if thisTrial_10 != None:
        for paramName in thisTrial_10:
            exec('{} = thisTrial_10[paramName]'.format(paramName))
    
    for thisTrial_10 in trials_10:
        currentLoop = trials_10
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
        if thisTrial_10 != None:
            for paramName in thisTrial_10:
                exec('{} = thisTrial_10[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "afterVAS"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_12.keys = []
        key_resp_12.rt = []
        _key_resp_12_allKeys = []
        if trialsCount==2:
            continueRoutine = False
        # keep track of which components have finished
        afterVASComponents = [image_7, key_resp_12]
        for thisComponent in afterVASComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        afterVASClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "afterVAS"-------
        while continueRoutine:
            # get current time
            t = afterVASClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=afterVASClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_7* updates
            if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                image_7.setAutoDraw(True)
            
            # *key_resp_12* updates
            waitOnFlip = False
            if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_12.frameNStart = frameN  # exact frame index
                key_resp_12.tStart = t  # local t and not account for scr refresh
                key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                key_resp_12.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_12.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_12_allKeys.extend(theseKeys)
                if len(_key_resp_12_allKeys):
                    key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                    key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in afterVASComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "afterVAS"-------
        for thisComponent in afterVASComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_12.keys in ['', [], None]:  # No response was made
            key_resp_12.keys = None
        trials_10.addData('key_resp_12.keys',key_resp_12.keys)
        if key_resp_12.keys != None:  # we had a response
            trials_10.addData('key_resp_12.rt', key_resp_12.rt)
        trialsCount+=1
        trials_10.addData('section','after-VAS screen displayed')
        trials_10.addData('displayed','img/after_VAS.jpg')
        
        # the Routine "afterVAS" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_10'
    
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_11 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_11')
thisExp.addLoop(trials_11)  # add the loop to the experiment
thisTrial_11 = trials_11.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
if thisTrial_11 != None:
    for paramName in thisTrial_11:
        exec('{} = thisTrial_11[paramName]'.format(paramName))

for thisTrial_11 in trials_11:
    currentLoop = trials_11
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
    if thisTrial_11 != None:
        for paramName in thisTrial_11:
            exec('{} = thisTrial_11[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "finalReward"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_13.keys = []
    key_resp_13.rt = []
    _key_resp_13_allKeys = []
    # keep track of which components have finished
    finalRewardComponents = [image_8, key_resp_13]
    for thisComponent in finalRewardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    finalRewardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "finalReward"-------
    while continueRoutine:
        # get current time
        t = finalRewardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=finalRewardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_8* updates
        if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_8.frameNStart = frameN  # exact frame index
            image_8.tStart = t  # local t and not account for scr refresh
            image_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
            image_8.setAutoDraw(True)
        
        # *key_resp_13* updates
        waitOnFlip = False
        if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_13.frameNStart = frameN  # exact frame index
            key_resp_13.tStart = t  # local t and not account for scr refresh
            key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
            key_resp_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_13.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_13_allKeys.extend(theseKeys)
            if len(_key_resp_13_allKeys):
                key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in finalRewardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "finalReward"-------
    for thisComponent in finalRewardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_13.keys in ['', [], None]:  # No response was made
        key_resp_13.keys = None
    trials_11.addData('key_resp_13.keys',key_resp_13.keys)
    if key_resp_13.keys != None:  # we had a response
        trials_11.addData('key_resp_13.rt', key_resp_13.rt)
    trials_11.addData('section','final-reward screen displayed')
    trials_11.addData('displayed','img/finalReward.jpg')
    # the Routine "finalReward" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_11'

level = 50

level = 50


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
