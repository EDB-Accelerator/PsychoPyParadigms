import sys
# sys.path.insert(1, './src')

# Door Game Session Module.

def waitUserSpaceAndC():
    from psychopy import core, event
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space' and c[0] != 'c'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

        if c == ['q'] or c == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()
    return c[0]

def waitUserSpace():
    from psychopy import core,event
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

        if c == ['q'] or c == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()

def eyeTrkInit(sp):
    import pylink as pl
    el = pl.EyeLink()
    el.sendCommand("screen_pixel_coords = 0 0 %d %d" % sp)
    el.sendMessage("DISPLAY_COORDS  0 0 %d %d" % sp)
    el.sendCommand("select_parser_configuration 0")
    el.sendCommand("scene_camera_gazemap = NO")
    el.sendCommand("pupil_size_diameter = %s" % ("YES"))
    return (el)

# el = eyeTrkInit((1920,1080))
# eyeTrkCalib(el, (1920,1080), 32)

def eyeTrkCalib(el, sp, cd):
    import pylink as pl
    pl.openGraphics(sp, cd)
    pl.setCalibrationColors((255, 255, 255), (0, 0, 0))
    pl.setTargetSize(int(sp[0] / 70), int(sp[1] / 300))
    pl.setCalibrationSounds("", "", "")
    pl.setDriftCorrectSounds("", "off", "off")
    el.doTrackerSetup()
    pl.closeGraphics()
    # el.setOfflineMode()

def EyeTrackerCalibration():
    import sys
    import pickle
    sys_backup = sys.path[:]

    sys.path.insert(1, './lib')
    # sys.path.insert(1,'C:\Program Files\PsychoPy3\Lib\site-packages\psychopy')

    from psychopy import visual, core, event
    from iohub import launchHubServer

    win = visual.Window((1024, 768), monitor="testMonitor", color="black", winType='pyglet')

    message = visual.TextStim(win,
                              text="Eyetracker Calibration will start.  \n\nPress the spacebar when you are ready.",
                              units='norm', wrapWidth=2)
    message.draw();
    win.flip();
    waitUserSpace()

    iohub_config = {'eyetracker.hw.sr_research.eyelink.EyeTracker':
                        {'name': 'tracker',
                         'model_name': 'EYELINK 1000 DESKTOP',
                         'runtime_settings': {'sampling_rate': 500,
                                              'track_eyes': 'LEFT'}
                         }
                    }
    import subprocess


    # Eyetracker Calibration.

    # p = subprocess.Popen('C:\Program Files\PsychoPy3\python.exe CalibrationSub.py')
    # p.wait()

    # Import developer-defined functions

    import psychopy.iohub.client

    try:
        io = launchHubServer(**iohub_config)
    except:
        q = psychopy.iohub.client.ioHubConnection.getActiveConnection().quit()
        io = launchHubServer(**iohub_config)
    # tracker = pylink.EyeLink('100.1.1.1')

    # tracker.sendMessage()
    # Get the eye tracker device.
    tracker = io.devices.tracker
    screenResolution = [1024, 768]
    tracker.sendCommand("screen_pixel_coords = 0 0 %d %d" % (screenResolution[0] - 1, screenResolution[1] - 1))
    tracker.sendMessage("DISPLAY_COORDS = 0 0 %d %d" % (screenResolution[0] - 1, screenResolution[1] - 1))

    # Eyetracker Calibration.
    c = 'c'
    while c != 'space':
        r = tracker.runSetupProcedure()

        # win.close()
        win.winHandle.activate()
        message = visual.TextStim(win,
                                  text="Calibration is completed.\n\nPress the spacebar when you are ready to keep playing.\n\n Press 'c' to do calibration again.",
                                  units='norm', wrapWidth=2)
        message.draw();
        win.flip();
        c = waitUserSpaceAndC()

    win.close()
    # Eyelink start recording
    tracker.setRecordingState(True)
    return tracker

# from psychopy import visual
# win = visual.Window((1024, 768), monitor="testMonitor", color="black", winType='pyglet')
# EyeTrackerCalibration(win,[1024,768])

def eyeLinkFinishRecording(tracker,outEDF):
    import pylink
    tracker.sendMessage('TRIAL_RESULT 0')
    tracker.setRecordingState(False)
    # open a connection to the tracker and download the result file.
    trackerIO = pylink.EyeLink('100.1.1.1')
    trackerIO.receiveDataFile("et_data.EDF", outEDF)
    return tracker


# win.getMovieFrame()  # Defaults to front buffer, I.e. what's on screen now.
# win.saveMovieFrames(imgScreenShot)
# shutil.copyfile(imgScreenShot, imgScreenShot2)