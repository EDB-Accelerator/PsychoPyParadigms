import sys
sys.path.insert(1, './src')

from psychopy import core, visual, event, sound,gui
from Helper import waitUserSpace,displayVAS,tableWrite,get_keypress,waitUserInput,triggerGo,displayText
from JoystickInput import JoystickInput
import random, re, datetime, glob, time, platform
import pylink
import numpy as np
import pandas as pd
# from psychopy.hardware import joystick
from WaitEyeGazed import WaitEyeGazed
from ELIdxRecord import ELIdxRecord
from EyeTrackerCalibration import EyeTrackerCalibration
from psychopy.iohub import launchHubServer

def DoorGamePlay(Df, DfTR,win, params, iterNum, port,SectionName):

    params["idxTR"] = 0

    width = params["screenSize"][0]
    height = params["screenSize"][1]
    params['subTrialCounter'] = 0

    if SectionName == "TaskRun1":
        img1 = visual.ImageStim(win=win, image="./instruction/start_main_game.jpg", units="pix", opacity=1,size=(width, height))
        img1.draw();
        win.flip()

        # Wait for User input.
        while (JoystickInput())['buttons_text'] == ' ':  # while presenting stimuli
            time.sleep(0.001)
            img1.draw();
            win.flip()
        while (JoystickInput())['buttons_text'] != ' ':  # while presenting stimuli
            time.sleep(0.001)

    # Eyetracker start recording
    if params['EyeTrackerSupport']:

        message = visual.TextStim(win,
                                  text="Eyetracker Calibration will start.  \n\nPress the spacebar when you are ready.",
                                  units='norm', wrapWidth=2)
        message.draw();
        win.flip();
        waitUserSpace(Df, params)

        iohub_config = {'eyetracker.hw.sr_research.eyelink.EyeTracker':
                            {'name': 'tracker',
                             'model_name': 'EYELINK 1000 DESKTOP',
                             'runtime_settings': {'sampling_rate': 500,
                                                  'track_eyes': 'RIGHT'}
                             }
                        }
        # Start new ioHub server.
        import psychopy.iohub.client

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

        # Eyetracker Calibration.
        tracker = EyeTrackerCalibration(tracker)

        # Eyetracker start recording
        tracker.setRecordingState(True)
        ELstartTime = time.time()

    width = params["screenSize"][0]
    height = params["screenSize"][1]

    # Read Door Open Chance file provided by Rany.
    doorOpenChanceMap = np.squeeze((pd.read_csv('./input/doorOpenChance.csv',header=None)).values)
    imgList = glob.glob(params['imageDir'] + params['imageSuffix'])
    totalCoin = 0

    if JoystickInput() == -1:
        print("There is no available Joystick.")
        exit()

    # Shuffle image. # https://pynative.com/python-random-shuffle/

    if params['EyeTrackerSupport']:
        DfTR = ELIdxRecord(DfTR, params, SectionName, time.time()-ELstartTime,"", "After Calibration Before Door Practice Game")
        tracker.sendMessage('TRIAL_RESULT 0')

    aoiTimeStart = time.time() * 1000
    for i in range(iterNum):

        # EDF labeling (start)
        if params['EyeTrackerSupport']:
            tracker.sendMessage('TRIALID %d' % params["idxTR"])
            ELstartTime = time.time()

        params['subTrialCounter'] += 1
        Dict = {
            "ExperimentName" : params['expName'],
            "Subject" : params['subjectID'],
            "Session" : params["Session"],
            "Version" : params["Version"],
            "Section" : SectionName,
            "Subtrial" : params['subTrialCounter'],
            "SessionStartDateTime" : datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
        }

        # Pick up random image.
        # randN = random.randint(0, len(imgList) - 1)
        if i % 49 == 0:
            random.shuffle(imgList)
        imgFile = imgList[i % 49]

        if platform.system() =='Windows':
            p, r = re.findall(r'\d+', imgFile.split('\\')[-1])
        else:
            p, r = re.findall(r'\d+', imgFile.split('/')[-1])

        Dict["Punishment_magnitude"] = p
        Dict["Reward_magnitude"] = r

        # Display the image.
        c = ['']
        level = Dict["Distance_start"] = params["DistanceStart"]
        width = params['width_bank'][level]
        height = params['height_bank'][level]
        img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
        img1.draw();win.flip();

        startTime = time.time()
        Dict["Distance_max"] = Dict["Distance_min"] = params["DistanceStart"]
        Dict["Distance_lock"] = 0
        MaxTime = params['DistanceLockWaitTime'] * 1000

        # Initial screen
        width = params['width_bank'][level]
        height = params['height_bank'][level]
        img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
        triggerGo(port, params, r, p, 1) # Trigger: Door onset (conflict)
        count = 0
        joy = JoystickInput()
        position = (0, 0)
        while count < 3:  # while presenting stimuli
            # If waiting time is longer than 10 sec, exit this loop.
            Dict["DoorAction_RT"] = (time.time() - startTime) * 1000
            if Dict["DoorAction_RT"] > MaxTime:
                c[0] = "timeisUp"
                break
            # if (sum(joy.getAllButtons()) != 0):
            if joy['buttons_text'] != ' ':
                count += 1
                if count >= 2:
                    Dict["Distance_lock"] = 1
                    break

            # joyUserInput = joy.getY()
            joy = JoystickInput()
            joyUserInput = joy['y']

            if joyUserInput < -0.5 and level < 100:
                level += 2
                level = min(100,level)
            elif joyUserInput < -0.1 and level < 100:
                level += 1
                level = min(100,level)
            elif joyUserInput > 0.5 and level > 0:
                level -= 2
                level = max(0,level)
            elif joyUserInput > 0.1 and level > 0:
                level -= 1
                level = max(0, level)

            width = params['width_bank'][level]
            height = params['height_bank'][level]
            # preInput = joyUserInput
            Dict["Distance_max"] = max(Dict["Distance_max"], level)
            Dict["Distance_min"] = min(Dict["Distance_min"], level)

            img1.size = (width, height)
            img1.draw();win.flip()
            get_keypress(Df,params)

            if params['EyeTrackerSupport']:

                positionTmp = position
                position = tracker.getPosition()
                if position is None:
                    position = positionTmp

                aoiTimeEnd = time.time() * 1000
                # Door
                tracker.sendMessage('!V IAREA %d %d RECTANGLE %d %d %d %d %d %s' % (0,int(aoiTimeStart-aoiTimeEnd),
                                                                              1, 512 - width * 105 / 1024,
                                                                              390 - height * 160 / 780,
                                                                              512 + width * 105 / 1024,
                                                                              390 + height * 200 / 780,
                                                                              'DOOR'))
                # Reward
                tracker.sendMessage('!V IAREA %d %d RECTANGLE %d %d %d %d %d %s' % (0,int(aoiTimeStart-aoiTimeEnd),
                                                                                1, 512 - width * 190 / 1024,
                                                                              390 - height * 155 / 780,
                                                                              512 - width * 130 / 1024,
                                                                              390 + height * 200 / 780,
                                                                              'Reward Bar (Green bar)'))

                # Punishment bar
                tracker.sendMessage('!V IAREA %d %d RECTANGLE %d %d %d %d %d %s' % (0,int(aoiTimeStart-aoiTimeEnd),
                                                                                1, 512 + width * 190 / 1024,
                                                                              390 - height * 155 / 780,
                                                                              512 + width * 130 / 1024,
                                                                              390 + height * 200 / 780,
                                                                              'Punishment Bar (Red bar)'))

                aoiTimeStart = aoiTimeEnd


        triggerGo(port, params, r, p, 2) # Trigger: Joystick lock (start anticipation)
        Dict["DistanceFromDoor_SubTrial"] = level

        if params['EyeTrackerSupport']:
            tracker.sendMessage('TRIAL_RESULT 0')
            DfTR = ELIdxRecord(DfTR, params,SectionName,time.time()-ELstartTime,i, "Playing Door Game (Before lock).")
            tracker.sendMessage('TRIALID %d' % params["idxTR"])
            tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (imgFile, 1024/2, 780 / 2, width, height))
            # Door
            tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, 512-width*105/1024,
                                                                                390-height*160/780,
                                                                                512+width*105/1024,
                                                                                390+height*200/780,
                                                                                'DOOR'))
            # Reward
            tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, 512-width*190/1024,
                                                                                390-height*155/780,
                                                                                512-width*130/1024,
                                                                                390+height*200/780,
                                                                                'Reward Bar (Green bar)'))

            # Punishment bar
            tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, 512+width*190/1024,
                                                                                390-height*155/780,
                                                                                512+width*130/1024,
                                                                                390+height*200/780,
                                                                                'Punishment Bar (Red bar)'))

            ELstartTime = time.time()

        # Door Anticipation time
        Dict["Door_anticipation_time"] = random.uniform(2, 4) * 1000
        time.sleep(Dict["Door_anticipation_time"] / 1000)

        if params['EyeTrackerSupport']:
            tracker.sendMessage('TRIAL_RESULT 0')
            DfTR = ELIdxRecord(DfTR, params,SectionName,time.time()-ELstartTime,i, "After lock: Door Anticipation Time.")
            tracker.sendMessage('TRIALID %d' % params["idxTR"])
            # tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % ('./img/practice/combined.jpg', 1024 / 2, 780 / 2, width, height))
            # tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, 512-width*50/1024,
            #                                                                     390-height*40/780,
            #                                                                     512+width*50/1024,
            #                                                                     390+height*50/780,
            #                                                                     'Reward (Question mark)'))
            ELstartTime = time.time()

        if random.random() > doorOpenChanceMap[level]:
            Dict["Door_opened"] = "closed"
            img1.draw();win.flip()
            triggerGo(port, params, r, p, 5)  # Door outcome: it didn’t open
            event.waitKeys(maxWait=2)

            if params['EyeTrackerSupport']:
                tracker.sendMessage('TRIAL_RESULT 0')
                DfTR = ELIdxRecord(DfTR, params, SectionName, time.time() - ELstartTime, i, "Reward screen (Door not opened) displayed.")
                tracker.sendMessage('TRIALID %d' % params["idxTR"])
                ELstartTime = time.time()
        else:
            Dict["Door_opened"] = "opened"
            if random.random() < 0.5:
                Dict["Door_outcome"] = "punishment"
                awardImg = "./img/outcomes/" + p + "_punishment.jpg"
                img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -height * 0.028],
                                        size=(width * 0.235, height * 0.464))
                message = visual.TextStim(win, text="-" + p, wrapWidth=2)
                message.pos = (0, 50)
                img1.draw();img2.draw();message.draw();win.flip()
                triggerGo(port, params, r, p, 4)  #Door outcome: punishment
                sound1 = sound.Sound("./img/sounds/punishment_sound.wav")
                sound1.play()
                event.waitKeys(maxWait=2)
                sound1.stop()
                totalCoin -= int(p)
                displayText(win, "-" + str(p))
            else:
                Dict["Door_outcome"] = "reward"
                awardImg = "./img/outcomes/" + r + "_reward.jpg"
                img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -height * 0.028],
                                        size=(width * 0.235, height * 0.464))
                message = visual.TextStim(win, text="+" + r, wrapWidth=2)
                message.pos = (0, 50)
                img1.draw();img2.draw();win.flip()
                triggerGo(port, params, r, p, 3)  # Door outcome: reward
                sound1 = sound.Sound("./img/sounds/reward_sound.wav")
                sound1.play()
                event.waitKeys(maxWait=2)
                sound1.stop()
                totalCoin += int(r)
            if params['EyeTrackerSupport']:
                tracker.sendMessage('TRIAL_RESULT 0')
                DfTR = ELIdxRecord(DfTR, params, SectionName, time.time() - ELstartTime, i, "Reward screen (Door Opened) displayed.")
                tracker.sendMessage('TRIALID %d' % params["idxTR"])
                ELstartTime = time.time()

        if params['EyeTrackerSupport']:
            imgScreenShot = './img/outscreenshot/' + str(params['idxImg']) + '.jpg'
            imgScreenShot2 = './output/img/outscreenshot/' + str(params['idxImg']) + '.jpg'

            win.getMovieFrame()  # Defaults to front buffer, I.e. what's on screen now.
            win.saveMovieFrames(imgScreenShot)
            win.saveMovieFrames(imgScreenShot2)
            params['idxImg'] += 1

            tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (imgScreenShot, 1024 / 2, 780 / 2, width, height))
            tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, 512-width*50/1024,
                                                                                390-height*40/780,
                                                                                512+width*50/1024,
                                                                                390+height*50/780,
                                                                                'Reward (Question mark)'))

        # ITI duration
        if params['EyeTrackerSupport']:
            startTime = time.time()
            width = params["screenSize"][0]
            height = params["screenSize"][1]
            tracker.sendMessage('!V IMGLOAD CENTER %s %d %d' % ("./img/ITI_fixation.jpg", width/2, height/2))
            tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (
            1, int(335 * width / 1024), int(217 * height / 780), int(689 * width / 1024), int(561 * height / 780),
            'fixation treasure'))
            WaitEyeGazed(win, params, tracker)
            Dict["ITI_duration"] = time.time() - startTime

        else:
            width = params["screenSize"][0]
            height = params["screenSize"][1]
            img1 = visual.ImageStim(win=win, image="./img/iti.jpg", units="pix", opacity=1, size=(width, height))
            img1.draw();win.flip();
            Dict["ITI_duration"] = random.uniform(1.5, 3.5) * 1000
            time.sleep(Dict["ITI_duration"] / 1000)

        if params['EyeTrackerSupport']:
            tracker.sendMessage('TRIAL_RESULT 0')
            DfTR = ELIdxRecord(DfTR, params,SectionName,time.time()-ELstartTime,i, "ITI screen displayed.")

        Dict["Total_coins"] = totalCoin
        Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # Eyetracker finish recording
    if params['EyeTrackerSupport']:
        # Eyetracker stop recording
        tracker.setRecordingState(False)

        # open a connection to the tracker and download the result file.
        trackerIO = pylink.EyeLink('100.1.1.1')
        trackerIO.receiveDataFile("et_data.EDF", params[SectionName])

        # Stop the ioHub Server
        io.quit()
        trackerIO.close()

    return Df,DfTR
