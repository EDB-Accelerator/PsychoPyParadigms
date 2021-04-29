# Filename: picture.py

# This is a basic example, which shows how connect to and disconnect from
# the tracker, how to open and close data file, how to start/stop recording,
# and the standard messages for integration with the Data Viewer software.
# Four pictures will be shown one-by-one and each trial terminates upon a
# keypress response or until 3 secs have elapsed.

# Revision history
# 1/13/2020: orginal version for internal review

from __future__ import division
from __future__ import print_function

import pylink
import os
import random
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from psychopy import visual, core, event, monitors
from PIL import Image

# shoule we use the Psychopy GUI module to collect subject information
# set useGUI to False only when running the script from a command line
useGUI = True

# STEP 1: get subject info
expInfo = {'ID': '00', 'Name': 'TEST'}
if useGUI:
    from psychopy import gui

    dlg = gui.DlgFromDict(dictionary=expInfo, title="Picture example", order=['ID', 'Name'])
    if not dlg.OK:
        core.quit()  # user pressed cancel
else:
    expInfo['ID'] = input('Participant ID (1-99): ')
    expInfo['Name'] = input('Participant Initials (e.g., WZ): ')

# SETP 2: open a connection to the tracker
# replace the IP address with None will open a simulated connection
tk = pylink.EyeLink('100.1.1.1')

# STEP 3: Open an EDF data file on the Host and write a file header
# The file name should not exceeds 8 characters
dataFileName = expInfo['ID'] + '_' + expInfo['Name'] + '.EDF'
tk.openDataFile(dataFileName)
# add personalized data file header (preamble text)
tk.sendCommand("add_file_preamble_text 'SR Picture example'")

# STEP 4: Open a window for stimulus presentation, and configure options for
# calibration/validation and drift-correction (target size, color, etc.)
scnWidth, scnHeight = (1440, 900)

# we need to set monitor parameters to use the different PsychoPy screen "units"
mon = monitors.Monitor('myMonitor', width=53.0, distance=70.0)
mon.setSizePix((scnWidth, scnHeight))

# open a window; set winType='pyglet' to prevent text display issues in PsychoPy2
win = visual.Window((scnWidth, scnHeight), fullscr=True, monitor=mon,
                    winType='pyglet', units='pix', allowStencil=True)

# set up a custom graphics envrionment (EyeLinkCoreGraphicsPsychopy) for calibration
genv = EyeLinkCoreGraphicsPsychoPy(tk, win)

# set background and foreground colors, (-1,-1,-1)=black, (1,1,1)=white
# genv.backgroundColor = (0,0,0)
# genv.foregroundColor = (-1,-1,-1)

# play feedback beeps during calibration/validation, disabled by default
# genv.enableBeep = True

# calibration target size
genv.targetSize = 32

# Configure the calibration target, could be a 'circle',
# a movie clip ('movie'), a 'picture', or a 'spiral', the default is a circle
genv.calTarget = 'circle'

# provide a movie clip if genv.calTarget = 'movie'
# genv.movieTargetFile = 'videos' + os.sep + 'animated_target.avi'

# provide a picture if genv.calTarget = 'picture'
# genv.pictureTargetFile = 'images' + os.sep + 'panda.jpg'

pylink.openGraphicsEx(genv)

# STEP 5: Set up the tracker
# put the tracker in idle mode before we change its parameters
tk.setOfflineMode()
pylink.pumpDelay(100)

# IMPORTANT: send screen resolution to the tracker
# see Eyelink Installation Guide, Section 8.4: Customizing Your PHYSICAL.INI Settings
tk.sendCommand("screen_pixel_coords = 0 0 %d %d" % (scnWidth - 1, scnHeight - 1))

# save screen resolution in EDF data, so Data Viewer can correctly load experimental graphics
# see Data Viewer User Manual, Section 7: Protocol for EyeLink Data to Viewer Integration
tk.sendMessage("DISPLAY_COORDS = 0 0 %d %d" % (scnWidth - 1, scnHeight - 1))

# sampling rate, 250, 500, 1000, or 2000; this command is not supported for EyeLInk II/I trackers
# tk.sendCommand("sample_rate 1000")

# detect eye events based on "GAZE" (or "HREF") data
tk.sendCommand("recording_parse_type = GAZE")

# Saccade detection thresholds: 0-> standard/coginitve, 1-> sensitive/psychophysiological
# see Eyelink User Manual, Section 4.3: EyeLink Parser Configuration
tk.sendCommand("select_parser_configuration 0")

# choose a calibration type, H3, HV3, HV5, HV13 (HV = horiztonal/vertical),
# tk.setCalibrationType('HV9') also works, see the Pylink manual
tk.sendCommand("calibration_type = HV9")

# proportion of the screen covered by calibration/validation targets
# OPTIONAL -- useful for cases where the monitor extends beyond the trackable range or
# part of the monitor is occuluded, e.g., in some MRI labs
# tk.sendCommand("calibration_area_proportion 0.85 0.83")
# tk.sendCommand("validation_area_proportion  0.85 0.83")

# Set a gamepad button to accept calibration/drift check target
# OPTIONAL -- You need a supported gamepad/button box that is connected to the Host PC
# tk.sendCommand("button_function 5 'accept_target_fixation'")

# tracker hardware, 1-EyeLink I, 2-EyeLink II, 3-Newer models (1000/1000Plus/Portable DUO)
hardware_ver = tk.getTrackerVersion()

# tracking software version
software_ver = 0
if hardware_ver == 3:
    tvstr = tk.getTrackerVersionString()
    vindex = tvstr.find("EYELINK CL")
    software_ver = float(tvstr.split()[-1])

# sample and event data saved in EDF data file
# see sectin 4.6 of the EyeLink user manual, software version > 4 adds remote tracking (and thus HTARGET)
tk.sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT")
if software_ver >= 4:
    tk.sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,HTARGET,INPUT")
else:
    tk.sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,INPUT")

# sample and event data available over the link
tk.sendCommand("link_event_filter = LEFT,RIGHT,FIXATION,FIXUPDATE,SACCADE,BLINK,BUTTON,INPUT")
if software_ver >= 4:
    tk.sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,HTARGET,INPUT")
else:
    tk.sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,INPUT")

# STEP 6:  Show task instructions and calibrate the tracker
msg = visual.TextStim(win, text='Press ENTER twice to calibrate the tracker\n' +
                                'In the task, press any key to end a trial')
msg.draw()
win.flip()
event.waitKeys()

# set up the camera and calibrate the tracker
tk.doTrackerSetup()

# STEP 7: Run the experimental trials
# store the parameters of all trials in a list, [trial_id, image]
trials = [[1, 'bonEcho.png'],
          [2, 'trainStation.png'],
          [3, 'biking.png'],
          [4, 'oldMontreal.png']]


# For clarity, create a helper function to group the code that will be repeated on each trial
def runTrial(trial_pars, trial_index):
    """ Helper function specifying the events that will occur in a single trial

    trial_pars - a list containing trial parameters, e.g., [3, 'biking.png']
    trial_index - record the order of trial presentation in the task
    """

    # unpacking the trial paramters
    trial_id, pic = trial_pars

    # load the image to display, here we stretch the image to fill full screen
    img = visual.ImageStim(win, image='images' + os.sep + pic)

    # put the tracker in idle mode before we transfer the backdrop image
    tk.setOfflineMode()
    pylink.pumpDelay(100)

    # backdrop image on the Host screen
    # OPTIONAL -- this is SLOW and may cause timing problems for some tasks
    im = Image.open('images' + os.sep + pic)  # open image with the PIL Image moduel
    w, h = im.size
    pixels = im.load()
    # use the list comprehension trick to convert all image pixels into a <pixel> format
    # supported by the Host PC, pixels = [line1, ...lineH], line = [pix1,...pixW], pix=(R,G,B)
    pixels_2transfer = [[pixels[i, j] for i in range(w)] for j in range(h)]
    tk.sendCommand('clear_screen 0')  # clear the host screen
    # call the bitmapBackdrop() command to show backdrop image on the Host
    # arguments: width, height, pixel, crop_x, crop_y, crop_width, crop_height, x, y on Host, option
    # tk.bitmapBackdrop(w, h, pixels_2transfer, 0, 0, w, h, 0, 0, pylink.BX_MAXCONTRAST)
    tk.bitmapSaveAndBackdrop(w, h, pixels_2transfer, 0, 0, w, h, 'tmp_img', 'images',
                             pylink.SV_NOREPLACE, 0, 0, pylink.BX_MAXCONTRAST)

    # send the standard "TRIALID" message to mark the start of a trial
    # see Data Viewer User Manual, Section 7: Protocol for EyeLink Data to Viewer Integration
    tk.sendMessage('TRIALID %d' % trial_index)

    # record_status_message : show some info on the Host PC - OPTIONAL
    # here we show how many trial has been tested
    tk.sendCommand("record_status_message 'TRIAL number %s'" % trial_index)

    # drift check
    # the doDriftCorrect() function requires target position in integers
    # the last two arguments: draw_target (1-default, 0-user draw the target then call this function)
    #                         allow_setup (1-press ESCAPE to recalibrate, 0-not allowed)
    try:
        err = tk.doDriftCorrect(int(scnWidth / 2), int(scnHeight / 2), 1, 1)
    except:
        tk.doTrackerSetup()

    # put the tracker in idle mode before we start recording
    tk.setOfflineMode()
    pylink.pumpDelay(100)

    # start recording
    # arguments: sample_to_file, events_to_file, sample_over_link, event_over_link (1-yes, 0-no)
    err = tk.startRecording(1, 1, 1, 1)
    pylink.pumpDelay(100)  # wait for 100 ms to cache some samples

    # show the image
    img.draw()
    win.flip()
    # send over a message to mark the onset of the image
    tk.sendMessage('image_onset')

    # send over a message to specify where the image is stored relative to the EDF data file
    # see Data Viewer User Manual, Section 7: Protocol for EyeLink Data to Viewer Integration
    bgImage = '..' + os.sep + 'images' + os.sep + pic
    tk.sendMessage('!V IMGLOAD CENTER %s %d %d' % (bgImage, int(scnWidth / 2), int(scnHeight / 2)))

    # store interest area info in the EDF data file, if needed
    # here we set a rectangular IA, just to illustrate how the IA messages look like
    # format: !V IAREA RECTANGLE <id> <left> <top> <right> <bottom> [label string]
    # see Data Viewer User Manual, Section 7: Protocol for EyeLink Data to Viewer Integration
    tk.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, 100, 100, 400, 400, 'example_IA'))

    RT = -1  # log the response time, RT = -1 if a trial times out
    # show the image for 3 secs or until a key is pressed
    onsetTime = core.getTime()
    while True:
        # break out if 3 secs have elapsed
        if core.getTime() - onsetTime >= 3.0:
            # send over a message to log time out
            tk.sendMessage('time_out')
            break

        # check if any key has been pressed
        if event.getKeys():
            # send over a message to log the key press
            tk.sendMessage('key_pressed')
            RT = core.getTime() - onsetTime
            break

    # clear the screen
    win.color = [0, 0, 0]
    win.flip()
    tk.sendMessage('blank_screen')

    # stop recording
    tk.stopRecording()
    # clear the host display, this command is needed if you have backdrop image on the Host
    tk.sendCommand('clear_screen 0')

    # store trial variables to record in the EDF data file
    # see Data Viewer User Manual, Section 7: Protocol for EyeLink Data to Viewer Integration
    tk.sendMessage('!V TRIAL_VAR trial_id %s' % trial_id)
    tk.sendMessage('!V TRIAL_VAR image %s' % pic)
    tk.sendMessage('!V TRIAL_VAR RT %s' % RT)

    # send over the standard 'TRIAL_RESULT' message to mark the end of trial
    # see Data Viewer User Manual, Section 7: Protocol for EyeLink Data to Viewer Integration
    tk.sendMessage('TRIAL_RESULT 0')


# run a block of 4 trials
testList = trials[:]  # construct the trial list
random.shuffle(testList)  # randomize the trial list
for trial_index, trial_pars in enumerate(testList):
    runTrial(trial_pars, trial_index + 1)

# STEP 8: close the EDF data file and put the tracker in idle mode
tk.setOfflineMode()
pylink.pumpDelay(100)
tk.closeDataFile()

# STEP 9: download EDF file to Display PC and put it in local folder ('edfData')
msg = 'EDF data is transfering from EyeLink Host PC...'
edfTransfer = visual.TextStim(win, text=msg, color='white')
edfTransfer.draw()
win.flip()
pylink.pumpDelay(500)

# make sure the 'edfData' folder is there, create one if not
dataFolder = os.getcwd() + '/edfData/'
if not os.path.exists(dataFolder):
    os.makedirs(dataFolder)
tk.receiveDataFile(dataFileName, 'edfData' + os.sep + dataFileName)

# STEP 10: close the connection to tracker
tk.close()

# STEP 11: make sure everything is closed down
core.quit()
