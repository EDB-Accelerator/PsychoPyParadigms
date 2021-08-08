
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

def EyeTrackerIntialization(params,win):
    # win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')
    win.mouseVisible = False
    message = visual.TextStim(win,
                              text="Eyetracker Calibration will start.  \n\nPress the space bar when you are ready.",
                              units='norm', wrapWidth=2, color="black")
    message.draw();
    win.flip();
    waitUserSpace()

    iohub_config = {'eyetracker.hw.sr_research.eyelink.EyeTracker':
                        {'name': 'tracker',
                         'model_name': 'EYELINK 1000 DESKTOP',
                         'runtime_settings': {'sampling_rate': 500,
                                              # 'track_eyes': 'RIGHT'}
                                              'track_eyes': params['eyeSelection']}
                         }
                    }
    # Start new ioHub server.
    try:
        io = launchHubServer(**iohub_config)
    except:
        q = psychopy.iohub.client.ioHubConnection.getActiveConnection().quit()
        io = launchHubServer(**iohub_config)
    # Get the eye tracker device.
    tracker = io.devices.tracker
    tracker.sendCommand("screen_pixel_coords = 0 0 %d %d" % (params['screenSize'][0] - 1, params['screenSize'][1] - 1))

    # save screen resolution in EDF data, so Data Viewer can correctly load experimental graphics
    # see Data Viewer User Manual, Section 7: Protocol for EyeLink Data to Viewer Integration
    tracker.sendMessage("DISPLAY_COORDS = 0 0 %d %d" % (params['screenSize'][0] - 1, params['screenSize'][1] - 1))

    # win.close()
    return win,io,tracker

