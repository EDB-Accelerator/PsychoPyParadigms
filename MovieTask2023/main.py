from psychopy import visual  # visual must be called first to prevent a bug where the movie doesn't appear.
from psychopy import core, gui, data, event, logging, parallel  # sound
from psychopy.tools.filetools import fromFile, toFile  # saving and loading parameter files
import time as ts, numpy as np  # for timing and array operations
import os, glob  # for monitor size detection, files
import BasicPromptTools
import RatingScales  # for VAS sliding scale
import time
# ====================== #
# ===== PARAMETERS ===== #
# ====================== #
# Save the parameters declared below?
saveParams = False;  # Once params are set & saved, set this to False to simplify for taskmasters
newParamsFilename = 'MovieVasParams_3TA.psydat'

# Declare primary task parameter
params = {
    # Declare stimulus and response parameters
    'preppedKey': 'y',  # key from experimenter that says scanner is prepped and ready
    'triggerKey': '5',  # key from scanner that says scan is starting
    'fixationDur': 300,  # duration of fixation cross to be displayed during structural/clinical scans
    'finalScanDur': 140,  # duration of final scan after the movie
    'tStartup': 300,  # pause time before starting movie
    'movieDur': 331,  # 3 in seconds, so that rest period matches movie length
    'movieSintelFile': 'Sintel_edited.mp4',  # FrancisCropped.mp4', # movie stimlulus
    'movieFile': 'FrancisCropped.mp4',  # FrancisCropped.mp4', # movie stimlulus
    'movieSize': (1280.0, 720.0),  # (W,H) in pixels (640*3,360*3) for Boldscreen
    'restDur': 492,  # 480s of rest minus 8s steady-state (4 TRs) plus 20s for noise cancellation
    # declare prompt files
    'skipPrompts': False,  # go right to the scanner-wait page
    'structuralPromptFile': 'Prompts/ScaryMoviePrompts_structural.txt',
    # Name of text file containing prompts to be shown BEFORE first structural scan
    'restPromptFile': 'Prompts/ScaryMoviePrompts_rest.txt',  # shown AFTER structurals, BEFORE rest
    'moviePromptFile': 'Prompts/ScaryMoviePrompts_movie.txt',  # shown AFTER rest, before movie
    'postMoviePromptFile': 'Prompts/ScaryMoviePrompts_continue.txt',  # shown AFTER movie, BEFORE final scan
    'preFinalPromptFile': 'Prompts/ScaryMoviePrompts_pre_final_rest.txt',  # shown BEFORE final scan
    'finalPromptFile': 'Prompts/ScaryMoviePrompts_end.txt',  # shown AFTER final scan, before final VAS
    'RatingScalePromptFile': 'Prompts/ScaryMoviePrompts_rating_scale.txt',  # prompt for VAS
    # declare VAS question files
    'questionFile': 'Questions/ScaryMovieVasQuestions.txt',  # Name of text file containing Q&As
    'questionDownKey': '4',  # to move slider left
    'questionUpKey': '2',  # to move slider right
    'questionSelectKey': '3',  # to lock in an answer
    'questionSelectAdvances': True,  # will locking in an answer move to the next question?
    'questionDur': 999.0,  # Max time allowed for a question
    'vasStepSize': 0.5,
    # declare experimental flow parameters
    'doRestOne': True,  # don't skip the rest#1 scan section
    'doMovieOne': True,  # don't skip the movie#1 scan section
    'doRestTwo': True,  # don't skip the rest#2 scan section
    'doMovieTwo': True,  # don't skip the movie#2 scan section
    'doRestThree': True,  # don't skip the rest#3 scan section

    # parallel port parameters
    'sendPortEvents': True,  # send event markers to biopac computer via parallel port
    'portAddress': 0xD050,  # 0xD050, #  address of parallel port
    'codePrompt': 1,  # port value for start of prompts # ALTERNATE: int("00000011", 2), # set specific pins in binary
    'codeVas': 2,  # VAS
    'codeWait': 3,  # waiting for experimenter/scanner
    'codeRestOne': 4,
    'codeMovieOne': 5,
    'codeRestTwo': 6,
    'codeMovieTwo': 7,
    'codeRestThree': 8,
    'codeTheEnd': 9,
    # declare display parameters
    'playVideo': True, # check if we want to play video. (False when we want to do quick testing without video)
    'fullScreen': False,  # run in full screen mode?
    'screenToShow': 0,  # display on primary screen (0) or secondary (1)?
    'fixCrossSize': 50,  # size of cross, in pixels
    'fixCrossPos': [0, 0],  # (x,y) pos of fixation cross displayed before each stimulus (for gaze drift correction)
    'screenColor': (-1 - 1 - 1),  # (128,128,128), # all colors in rgb space: (r,g,b) all between - and 1
    'textColor': (1, 1, 1),  # in rgb space: (r,g,b) all between -1 and 1
    'vasScreenColor': (0, 0, 0),  # gray   #(-0.46667, -0.10588, 0.53725), # a neutral blue
    'vasTextColor': (1, 1, 1)  # white
}

# Global Exit
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

# ========================== #
# ===== SET UP LOGGING ===== #
# ========================== #
try:
    scriptName = os.path.basename(__file__)
except NameError:
    scriptName = 'interactive_console'

scriptName = os.path.splitext(scriptName)[0]  # remove extension
expInfo = {
        'SDAN': '1',
        'Session': 1,
        'doRestOne': True,
        'doMovieOne': True,
        'doRestTwo': True,
        'doMovieTwo': True,
        'doRestThree': True,
        'fixationDur': 300,
        'fullScreen': True,
        'playVideo': True,
        'sendPortEvents': True,
        # 'paramsFile': [newParamsFilename, 'Load...']
    }

# present a dialogue to change select params
dlg = gui.DlgFromDict(expInfo, title=scriptName, order=['SDAN', 'Session', 'doRestOne', 'doMovieOne', \
                                                        'doRestTwo', 'doMovieTwo','doRestThree', 'fixationDur','fullScreen','playVideo','sendPortEvents'])
if not dlg.OK:
    core.quit()  # the user hit cancel, so exit

# transfer experimental flow items from expInfo (gui input) to params (logged parameters)
for flowItem in ['doRestOne', 'doMovieOne','doRestTwo', 'doMovieTwo','doRestThree', 'fixationDur','fullScreen','playVideo','sendPortEvents']:
    params[flowItem] = expInfo[flowItem]

print('params = {')
for key in sorted(params.keys()):
    print("   '{}': {}".format(key, params[key]))  # print each value as-is (no quotes)
print('}')

# save experimental info
toFile('%s-lastExpInfo.psydat' % scriptName, expInfo)  # save params to file for next time

# make a log file to save parameter/event  data
dateStr = ts.strftime("%Y_%m_%d_%H%M", ts.localtime())  # add the current time
filename = 'Logs/%s-%s-%d-%s' % (scriptName, expInfo['SDAN'], expInfo['Session'], dateStr)  # log filename
logging.LogFile((filename + '.log'), level=logging.INFO)  # , mode='w') # w=overwrite
logging.log(level=logging.INFO, msg='---START PARAMETERS---')
logging.log(level=logging.INFO, msg='filename: %s' % filename)
logging.log(level=logging.INFO, msg='SDAN: %s' % expInfo['SDAN'])
logging.log(level=logging.INFO, msg='Session: %s' % expInfo['Session'])
logging.log(level=logging.INFO, msg='date: %s' % dateStr)
# log everything in the params struct
for key in sorted(params.keys()):  # in alphabetical order
    logging.log(level=logging.INFO, msg='%s: %s' % (key, params[key]))  # log each parameter

logging.log(level=logging.INFO, msg='---END PARAMETERS---')

# ========================== #
# ===== GET SCREEN RES ===== #
# ========================== #

screenRes = (1024, 768)
print("screenRes = [{},{}]".format(*screenRes))

# ========================== #
# == SET UP PARALLEL PORT == #
# ========================== #

if params['sendPortEvents']:
    port = parallel.ParallelPort(address=params['portAddress'])
    port.setData(0)  # initialize to all zeros
else:
    # print "Parallel port not used."
    print("Parallel port not used.")

# ========================== #
# ===== SET UP STIMULI ===== #
# ========================== #

# Initialize deadline for displaying next frame
tNextFlip = [0.0]  # put in a list to make it mutable (weird quirk of python variables)

# create clocks and window
globalClock = core.Clock()  # to keep track of time
trialClock = core.Clock()  # to keep track of time
win = visual.Window(screenRes, fullscr=params['fullScreen'], allowGUI=False, monitor='testMonitor',
                    screen=params['screenToShow'], units='deg', name='win', color=params['screenColor'])
win.mouseVisible = False
# create fixation cross
fCS = params['fixCrossSize']  # size (for brevity)
fCP = params['fixCrossPos']  # position (for brevity)
lineWidth = int(params['fixCrossSize'] / 3)
fixation = visual.ShapeStim(win, lineColor=params['textColor'], lineWidth=lineWidth, vertices=(
(fCP[0] - fCS / 2, fCP[1]), (fCP[0] + fCS / 2, fCP[1]), (fCP[0], fCP[1]), (fCP[0], fCP[1] + fCS / 2),
(fCP[0], fCP[1] - fCS / 2)), units='pix', closeShape=False, name='fixCross');
# create text stimuli
message1 = visual.TextStim(win, pos=[-.75, +.5], wrapWidth=1.5, color=params['textColor'], alignHoriz='left',
                           name='topMsg', text="aaa", units='norm')
message2 = visual.TextStim(win, pos=[-.75, -.5], wrapWidth=1.5, color=params['textColor'], alignHoriz='left',
                           name='bottomMsg', text="bbb", units='norm')

# get stimulus files
mov = visual.MovieStim3(win, params['movieFile'], size=params['movieSize'],
                        flipVert=False, flipHoriz=False, loop=False, units='pix')
print('orig movie size=%s' % mov.size)
print('duration=%.2fs' % mov.duration)

# get stimulus files
mov2 = visual.MovieStim3(win, params['movieSintelFile'], size=params['movieSize'],
                        flipVert=False, flipHoriz=False, loop=False, units='pix')
print('orig movie size=%s' % mov.size)
print('duration=%.2fs' % mov.duration)


# read questions and answers from text files
[topPrompts_structural, bottomPrompts_structural] = BasicPromptTools.ParsePromptFile(params['structuralPromptFile'])
print('%d prompts loaded from %s' % (len(topPrompts_structural), params['structuralPromptFile']))
[topPrompts_rest, bottomPrompts_rest] = BasicPromptTools.ParsePromptFile(params['restPromptFile'])
print('%d prompts loaded from %s' % (len(topPrompts_rest), params['restPromptFile']))
[topPrompts_movie, bottomPrompts_movie] = BasicPromptTools.ParsePromptFile(params['moviePromptFile'])
print('%d prompts loaded from %s' % (len(topPrompts_movie), params['moviePromptFile']))
[topPrompts_postmovie, bottomPrompts_postmovie] = BasicPromptTools.ParsePromptFile(params['postMoviePromptFile'])
print('%d prompts loaded from %s' % (len(topPrompts_postmovie), params['postMoviePromptFile']))

[topPrompts_prefinal, bottomPrompts_prefinal] = BasicPromptTools.ParsePromptFile(params['preFinalPromptFile'])
print('%d prompts loaded from %s' % (len(topPrompts_prefinal), params['preFinalPromptFile']))

[topPrompts_final, bottomPrompts_final] = BasicPromptTools.ParsePromptFile(params['finalPromptFile'])
print('%d prompts loaded from %s' % (len(topPrompts_final), params['finalPromptFile']))
[topPrompts_rating_scale, bottomPrompts_rating_scale] = BasicPromptTools.ParsePromptFile(
    params['RatingScalePromptFile'])
print('%d prompts loaded from %s' % (len(topPrompts_rating_scale), params['RatingScalePromptFile']))
# load Vas Qs & options
[questions, options, answers] = BasicPromptTools.ParseQuestionFile(params['questionFile'])
print('%d questions loaded from %s' % (len(questions), params['questionFile']))


# ============================ #
# ======= SUBFUNCTIONS ======= #
# ============================ #

# increment time of next window flip
def AddToFlipTime(tIncrement=1.0):
    tNextFlip[0] += tIncrement


# flip window as soon as possible
def SetFlipTimeToNow():
    tNextFlip[0] = globalClock.getTime()


# Send parallel port event
def SetPortData(data):
    if params['sendPortEvents']:
        logging.log(level=logging.EXP, msg='set port %s to %d' % (format(params['portAddress'], '#04x'), data))
        port.setData(data)
    else:
        print('Port event: %d' % data)


# Play movie all the way through
def PlayMovie(movie):
    if movie == "francis":
        # Play the movie until it's done or a key is pressed
        while mov.status != visual.FINISHED:
            mov.draw()
            win.flip()
            keyList = event.getKeys(keyList=['q', 'escape', 'space'])
            # Check for escape characters
            for key in keyList:
                if key in ['q', 'escape']:
                    CoolDown()
                else:  # 'skip' key
                    mov.status = visual.FINISHED  # end the movie early

        pass
    elif movie == "sintel":
        # Play the movie until it's done or a key is pressed
        while mov2.status != visual.FINISHED:
            mov2.draw()
            win.flip()
            keyList = event.getKeys(keyList=['q', 'escape', 'space'])
            # Check for escape characters
            for key in keyList:
                if key in ['q', 'escape']:
                    CoolDown()
                else:  # 'skip' key
                    mov2.status = visual.FINISHED  # end the movie early
        pass



def RunVas(questions, options):
    # Set screen color
    win.color = params['vasScreenColor']

    # Show questions and options
    [rating, decisionTime, choiceHistory] = RatingScales.ShowVAS(questions, options, win,
                                                                 questionDur=params['questionDur'], \
                                                                 upKey=params['questionUpKey'],
                                                                 downKey=params['questionDownKey'],
                                                                 selectKey=params['questionSelectKey'], \
                                                                 isEndedByKeypress=params['questionSelectAdvances'],
                                                                 textColor=params['vasTextColor'], name='Vas',
                                                                 stepSize=params['vasStepSize'])
    # Set screen color back
    win.color = params['screenColor']
    win.flip()  # flip so the color change 'takes' right away

    # Print results
    print('===VAS Responses:===')
    for iQ in range(len(rating)):
        print('Scale #%d: %.1f' % (iQ, rating[iQ]))


# Wait for scanner, then display a fixation cross
def WaitForScanner():
    # wait for experimenter
    message1.setText("Experimenter, is the scanner ready?")
    message2.setText("(Press '%c' when it is.)" % params['preppedKey'].upper())
    message1.draw()
    message2.draw()
    win.logOnFlip(level=logging.EXP, msg='Display WaitingForPrep')
    win.flip()
    keyList = event.waitKeys(keyList=[params['preppedKey'], 'q', 'escape'])
    # Check for escape characters
    for key in keyList:
        if key in ['q', 'escape']:
            CoolDown()

    # wait for scanner
    message1.setText("Waiting for scanner to start...")
    message2.setText("(Press '%c' to override.)" % params['triggerKey'].upper())
    message1.draw()
    message2.draw()
    win.logOnFlip(level=logging.EXP, msg='Display WaitingForScanner')
    win.flip()
    keyList = event.waitKeys(keyList=[params['triggerKey'], 'q', 'escape'])
    SetFlipTimeToNow()

    # Check for escape characters
    for key in keyList:
        if key in ['q', 'escape']:
            CoolDown()


# Handle end of a session
def CoolDown():
    # display cool-down message
    message1.setText("Press 'q' or 'escape' to end the task.")
    win.logOnFlip(level=logging.EXP, msg='Display TheEnd')
    message1.draw()
    win.flip()
    thisKey = event.waitKeys(keyList=['q', 'escape'])

    print("===Exiting Experiment===")

    # exit
    core.quit()


# === SET UP GLOBAL ESCAPE KEY === #
event.globalKeys.clear()
event.globalKeys.add(key='q', modifiers=['ctrl'], func=CoolDown)

# =========================== #
# ======= Resting #1 ======== #
# =========================== #
if params['doRestOne']:
    # Log current section
    logging.log(level=logging.EXP, msg='===== START Rest #1 BLOCK =====')

    # Display prompts
    if not params['skipPrompts']:
        win.callOnFlip(SetPortData, data=params['codePrompt'])
        BasicPromptTools.RunPrompts(topPrompts_structural, bottomPrompts_structural, win, message1, message2,
                                    name='structuralPrompt', ignoreKeys=[params['triggerKey']])

    # Wait for experimenter and scanner
    win.callOnFlip(SetPortData, data=params['codeWait'])
    WaitForScanner()

    # Draw fixation cross
    fixation.draw()
    win.callOnFlip(SetPortData, data=params['codeRestOne'])
    win.logOnFlip(level=logging.EXP, msg='Display Fixation')
    win.flip()

    # Update time of next stim
    AddToFlipTime(params['fixationDur'])  # duration of structural/clinical scans

    # Wait until it's time to continue
    while (globalClock.getTime() < tNextFlip[0]):
        if event.getKeys(keyList=['q', 'escape']):
            CoolDown()

    # Display prompts, pre-movie VAS
    if not params['skipPrompts']:
        win.callOnFlip(SetPortData, data=params['codePrompt'])
        BasicPromptTools.RunPrompts(topPrompts_rating_scale, bottomPrompts_rating_scale, win, message1, message2,
                                    name='rating_scaleMoviePrompt', ignoreKeys=[params['triggerKey']])
    # Display VAS
    win.callOnFlip(SetPortData, data=params['codeVas'])
    RunVas(questions, options)


# =========================== #
# ======= MOVIE #1 ======== #
# =========================== #
if params['doMovieOne']:
    # Log current section
    logging.log(level=logging.EXP, msg='===== START MOVIE #1 BLOCK =====')

    # Wait for experimenter and scanner
    win.callOnFlip(SetPortData, data=params['codeWait'])
    WaitForScanner()

    # Display prompts
    if not params['skipPrompts']:
        win.callOnFlip(SetPortData, data=params['codePrompt'])
        BasicPromptTools.RunPrompts(topPrompts_movie, bottomPrompts_movie, win, message1, message2, name='moviePrompt',
                                    ignoreKeys=[params['triggerKey'], '1', '2', '3', '4'])

    # log experiment start and set up
    win.callOnFlip(SetPortData, data=params['codeMovieOne'])
    win.logOnFlip(level=logging.EXP, msg='Display Movie')
    if params['playVideo']:
        PlayMovie(movie='sintel')

    # Display prompts
    if not params['skipPrompts']:
        win.callOnFlip(SetPortData, data=params['codePrompt'])
        BasicPromptTools.RunPrompts(topPrompts_rating_scale, bottomPrompts_rating_scale, win, message1, message2,
                                    name='rating_scaleMoviePrompt', ignoreKeys=[params['triggerKey']])

    # Display VAS
    win.callOnFlip(SetPortData, data=params['codeVas'])
    RunVas(questions, options)

# =========================== #
# ======= Resting #2 ======== #
# =========================== #
if params['doRestTwo']:
    # Log current section
    logging.log(level=logging.EXP, msg='===== START Rest #2 BLOCK =====')

    # Wait for experimenter and scanner
    win.callOnFlip(SetPortData, data=params['codeWait'])
    WaitForScanner()

    # Draw fixation cross
    fixation.draw()
    win.callOnFlip(SetPortData, data=params['codeRestTwo'])
    win.logOnFlip(level=logging.EXP, msg='Display Fixation')
    win.flip()

    # Update time of next stim
    AddToFlipTime(params['fixationDur'])  # duration of structural/clinical scans

    # Wait until it's time to continue
    while (globalClock.getTime() < tNextFlip[0]):
        if event.getKeys(keyList=['q', 'escape']):
            CoolDown()

    # Display prompts, pre-movie VAS
    if not params['skipPrompts']:
        win.callOnFlip(SetPortData, data=params['codePrompt'])
        BasicPromptTools.RunPrompts(topPrompts_rating_scale, bottomPrompts_rating_scale, win, message1, message2,
                                    name='rating_scaleMoviePrompt', ignoreKeys=[params['triggerKey']])
    # Display VAS
    win.callOnFlip(SetPortData, data=params['codeVas'])
    RunVas(questions, options)

# =========================== #
# ======= MOVIE #2 ======== #
# =========================== #
if params['doMovieTwo']:
    # Log current section
    logging.log(level=logging.EXP, msg='===== START MOVIE #2 BLOCK =====')

    # Wait for experimenter and scanner
    win.callOnFlip(SetPortData, data=params['codeWait'])
    WaitForScanner()

    # Display prompts
    if not params['skipPrompts']:
        win.callOnFlip(SetPortData, data=params['codePrompt'])
        BasicPromptTools.RunPrompts(topPrompts_movie, bottomPrompts_movie, win, message1, message2, name='moviePrompt',
                                    ignoreKeys=[params['triggerKey'], '1', '2', '3', '4'])

    # log experiment start and set up
    win.callOnFlip(SetPortData, data=params['codeMovieTwo'])
    win.logOnFlip(level=logging.EXP, msg='Display Movie')
    if params['playVideo']:
        PlayMovie(movie='francis')

    # Display prompts
    if not params['skipPrompts']:
        win.callOnFlip(SetPortData, data=params['codePrompt'])
        BasicPromptTools.RunPrompts(topPrompts_rating_scale, bottomPrompts_rating_scale, win, message1, message2,
                                    name='rating_scaleMoviePrompt', ignoreKeys=[params['triggerKey']])
    # Display VAS
    win.callOnFlip(SetPortData, data=params['codeVas'])
    RunVas(questions, options)

# =========================== #
# ======= Resting #3 ======== #
# =========================== #
if params['doRestThree']:
    # Log current section
    logging.log(level=logging.EXP, msg='===== START Rest #3 BLOCK =====')

    # Wait for experimenter and scanner
    win.callOnFlip(SetPortData, data=params['codeWait'])
    WaitForScanner()

    # Draw fixation cross
    fixation.draw()
    win.callOnFlip(SetPortData, data=params['codeRestThree'])
    win.logOnFlip(level=logging.EXP, msg='Display Fixation')
    win.flip()

    # Update time of next stim
    AddToFlipTime(params['fixationDur'])  # duration of structural/clinical scans

    # Wait until it's time to continue
    while (globalClock.getTime() < tNextFlip[0]):
        if event.getKeys(keyList=['q', 'escape']):
            CoolDown()

    # Display prompts
    if not params['skipPrompts']:
        win.callOnFlip(SetPortData, data=params['codePrompt'])
        BasicPromptTools.RunPrompts(topPrompts_final, bottomPrompts_final, win, message1, message2, name='finalPrompt',
                                    ignoreKeys=[params['triggerKey']])

    # Display VAS
    win.callOnFlip(SetPortData, data=params['codeVas'])
    RunVas(questions, options)


# exit experiment
win.callOnFlip(SetPortData, data=params['codeTheEnd'])
CoolDown()