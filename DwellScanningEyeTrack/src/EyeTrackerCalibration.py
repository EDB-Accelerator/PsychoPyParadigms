
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

def EyeTrackerCalibration(params,tracker,block):
    c = 'c'
    # tracker.setRecordingState(False)

    while c != 'space':
        # Eyetracker Calibration
        # if block==0:
        r = tracker.runSetupProcedure()
        # win.close()
        win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')
        win.mouseVisible = False
        message = visual.TextStim(win,
                                  text="Press 'c' to calibrate eyelink again.\n\nPress the spacebar to continue.\n ",
                                  units='norm', wrapWidth=2, color="black")
        message.draw();
        win.flip();
        c = waitUserSpaceAndC()
        block = 0
        win.close()
    # tracker.setRecordingState(True)

    return tracker

