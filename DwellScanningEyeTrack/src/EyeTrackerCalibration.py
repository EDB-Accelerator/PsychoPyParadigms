
# Import standard python libraries
import sys,pylink
from psychopy import visual,core,event

# Import developer-defined functions
sys.path.insert(1, './src')
from psychopy.iohub import launchHubServer
import psychopy.iohub.client

def waitUserSpace():
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

        if c == ['q'] or c == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()

def waitUserSpaceAndC():
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space' and c[0] != 'c'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

        if c == ['q'] or c == ['Q'] or c == ['Esc']:
            print('Q pressed. Forced Exit.')
            core.quit()
    return c[0]

def EyeTrackerCalibration(df,dfRaw,dict,dictRaw,params,tracker,win):
    import time, datetime
    from DictWrite import DictWrite, DictWriteRaw

    c = 'c'
    # tracker.setRecordingState(False)

    # Record status (start)
    dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    startTime = time.time()
    params["TrialCount"] = ""
    dict["Image Displayed"] = "Calibration"
    dictRaw["Event"] = "Calibration started"
    DictWriteRaw(dfRaw, dictRaw, params)

    while c != 'space':
        # Eyetracker Calibration
        r = tracker.runSetupProcedure()
        # win.close()
        win.winHandle.activate()
        win.mouseVisible = False
        message = visual.TextStim(win,
                                  text="Press 'c' to calibrate eyelink again.\n\nPress the spacebar to continue.\n ",
                                  units='norm', wrapWidth=2, color="black")
        message.draw();
        win.flip();
        c = waitUserSpaceAndC()
        # win.close()
    # tracker.setRecordingState(True)

    # Record status
    dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Duration"] = time.time() - startTime
    dictRaw["Event"] = "Calibration completed"
    DictWriteRaw(dfRaw, dictRaw, params)
    DictWrite(df, params, dict)

    return tracker

