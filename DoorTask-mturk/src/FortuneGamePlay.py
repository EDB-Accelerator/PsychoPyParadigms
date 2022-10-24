import sys
sys.path.insert(1, './src')

import datetime,os
import subprocess as subp
from psychopy import visual,core
from Helper import waitUserSpace, tableWrite
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import time
from numpy.random import random, randint, normal, shuffle, choice as randchoice
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
import psychopy.iohub as io
from psychopy.hardware import keyboard

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
from Helper import tableWrite,get_keypress,triggerGo,waitUserSpace
def FortuneGamePlay(Df, win,params,SectionName,gameResult):
    # Ensure that relative paths start from the same directory as this script
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)
    # Store info about the experiment session
    psychopyVersion = '2022.2.4'
    expName = 'untitled'  # from the Builder filename that created this script
    expInfo = {
        'participant': f"{randint(0, 999999):06.0f}",
        'session': '001',
    }
    # --- Show participant info dialog --
    # dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    # if dlg.OK == False:
    #     core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName
    expInfo['psychopyVersion'] = psychopyVersion

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
                                     extraInfo=expInfo, runtimeInfo=None,
                                     originPath='/Users/jimmy/Downloads/untitled_lastrun.py',
                                     savePickle=True, saveWideText=True,
                                     dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename + '.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    frameTolerance = 0.001  # how close to onset before 'same' frame

    # Start Code - component code to be run after the window creation

    # --- Setup the Window ---
    # win = visual.Window(
    #     size=(1024, 768), fullscr=False, screen=0,
    #     winType='pyglet', allowStencil=False,
    #     monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    #     blendMode='avg', useFBO=True,
    #     units='height')
    win.mouseVisible = False
    # store frame rate of monitor if we can measure it
    expInfo['frameRate'] = win.getActualFrameRate()
    if expInfo['frameRate'] != None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    # --- Setup input devices ---
    ioConfig = {}

    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')

    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None

    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')

    # --- Initialize components for Routine "trial" ---
    movie = visual.MovieStim(
        win, name='movie',
        filename='/Users/jimmy/github/PsychoPyParadigms/DoorTask-mturk/video/18.mp4', movieLib='ffpyplayer',
        loop=False, volume=1.0,
        pos=(0, 0), size=(488,610), units='pix',
        ori=0.0, anchor='center', opacity=None, contrast=1.0,
    )

    message = visual.TextStim(win, text="Press the spacebar when you are ready to play the Wheel of Fortune", wrapWidth=2)

    # movie.draw()
    # message.draw()
    # win.flip()
    # waitUserSpace(Df, params)
    # message = visual.TextStim(win, text="good", wrapWidth=2)
    # message.flip()
    # win.flip()

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine

    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    trialComponents = [movie]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

    # --- Run Routine "trial" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *movie* updates
        if movie.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            movie.frameNStart = frameN  # exact frame index
            movie.tStart = t  # local t and not account for scr refresh
            movie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'movie.started')
            movie.setAutoDraw(True)
            movie.play()
        if movie.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > movie.tStartRefresh + 5 - frameTolerance:
                # keep track of stop time/frame for later
                movie.tStop = t  # not accounting for scr refresh
                movie.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'movie.stopped')
                movie.setAutoDraw(False)
                movie.stop()

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    movie.stop()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)

    # --- End experiment ---
    # Flip one final time so any remaining win.callOnFlip()
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()

    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)
    logging.flush()
    # make sure everything is closed down
    if eyetracker:
        eyetracker.setConnectionState(False)
    thisExp.abort()  # or data files will save again on exit
    win.close()
    core.quit()

# def FortuneGamePlay(Df, win,params,SectionName,gameResult):
#     Dict = {
#         "Subject": params['subjectID'],
#         "Session": params["Session"],
#         "Version": params["Version"],
#         "Section": SectionName,
#         "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S"),
#     }
#
#     img1 = visual.ImageStim(win=win, image="./img/changeme.jpg", units="pix", opacity=1,size=(1024, 768))
#     img1.draw();win.flip()
#     win.mouseVisible = False
#     # waitUserSpace(Df, params)
#
#     # Wait for User input.
#     while (JoystickInput())['buttons_text'] == ' ':  # while presenting stimuli
#         time.sleep(0.001)
#         img1.draw();
#         win.flip()
#     while (JoystickInput())['buttons_text'] != ' ':  # while presenting stimuli
#         time.sleep(0.001)
#
#     win.mouseVisible = True
#     win.close()
#     if gameResult == 18:
#         subp.check_call("runFortuneWheel18.bat "+os.getcwd(), shell=True)
#         win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
#         message = visual.TextStim(win,
#                                   text="You have won $18.\n\nClick when you are ready to keep playing.",
#                                   units='norm', wrapWidth=2)
#     elif gameResult == 16:
#         subp.check_call("runFortuneWheel16.bat "+os.getcwd(), shell=True)
#         win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
#         message = visual.TextStim(win,
#                                   text="You have won $16.\n\nClick when you are ready to keep playing.",
#                                   units='norm', wrapWidth=2)
#     message.draw()
#     win.flip()
#     win.mouseVisible = False
#     # waitUserSpace(Df, params)
#
#     # Wait for User input.
#     while (JoystickInput())['buttons_text'] == ' ':  # while presenting stimuli
#         time.sleep(0.001)
#         message.draw();
#         win.flip()
#     while (JoystickInput())['buttons_text'] != ' ':  # while presenting stimuli
#         time.sleep(0.001)
#
#     return tableWrite(Df, params,Dict),win
