import sys

sys.path.insert(1, './src')

from psychopy import visual, event, sound
from pygame import mixer
from Helper import waitUserSpace, tableWrite, get_keypress, triggerGo, waitUserSpaceAndC
# from JoystickInput import JoystickInput
import random, re, datetime, glob, time, platform
import pylink
import numpy as np
import pandas as pd
from WaitEyeGazed import WaitEyeGazed
from ELIdxRecord import ELIdxRecord
# from EyeTrackerCalibration import EyeTrackerCalibration
# from psychopy.iohub import launchHubServer
import shutil
import os
from psychopy import core
def DoorGamePlay(Df, DfTR, win, params, iterNum, port, SectionName,excelTemps,my_pathway,imgList):
    debugClock = core.Clock()
    # expInfo = {
    #     'LHeat': 36.0,
    #     'MHeat': 41.0,
    #     'HHeat': 46.0,
    # }

    def SetPort(color, size):
        # SetPortData((color - 1) * 6 ** 2 + (size - 1) * 6 + (block))
        # print("excelTemps:", excelTemps)

        if size == 1:
            heat_key = f"Heat{color}"  # Dynamically construct the heat level key

            if heat_key in params:
                code = excelTemps[excelTemps['Temp'].astype(str).str.contains(str(params[heat_key]))]

                if params['HeatSupport']:
                    response = my_pathway.program(code.iat[0, 1])
                    my_pathway.start()
                    my_pathway.trigger()
                    print(f"Heat Level: {params[heat_key]}")
                    print("Matching Code:")
                    print(code)
                else:
                    print(f"Heat Level: {params[heat_key]}")
                    print("Matching Code:")
                    print(code)

        # if params['HeatSupport']:
        #     # if size == 1:
        #     #     if color == 1:
        #     #         code = excelTemps[excelTemps['Temp'].astype(str).str.contains(str(expInfo['LHeat']))]
        #     #         # logging.log(level=logging.EXP, msg='set medoc %s' % (code.iat[0, 1]))
        #     #     elif color == 2:
        #     #         code = excelTemps[excelTemps['Temp'].astype(str).str.contains(str(expInfo['MHeat']))]
        #     #         # logging.log(level=logging.EXP, msg='set medoc %s' % (code.iat[0, 1]))
        #     #     elif color == 3:
        #     #         code = excelTemps[excelTemps['Temp'].astype(str).str.contains(str(expInfo['HHeat']))]
        #     #     if params['HeatSupport']:
        #     #         response = my_pathway.program(code.iat[0, 1])
        #     #         my_pathway.start()
        #     #         my_pathway.trigger()
        #
        #     if size == 1:
        #         heat_key = f"Heat{color}"  # Dynamically construct the heat level key
        #
        #         if heat_key in params:
        #             code = excelTemps[excelTemps['Temp'].astype(str).str.contains(str(params[heat_key]))]
        #
        #             if params['HeatSupport']:
        #                 response = my_pathway.program(code.iat[0, 1])
        #                 my_pathway.start()
        #                 my_pathway.trigger()
        # # else:



    if params['JoyStickSupport']:
        from JoystickInput import JoystickInput
    else:
        from VirtualJoystickInput import JoystickInput

    params["idxTR"] = 0

    width = params["screenSize"][0]
    height = params["screenSize"][1]
    params['subTrialCounter'] = 0

    if SectionName == "TaskRun1":
        img1 = visual.ImageStim(win=win, image="./instruction/start_main_game.jpg", units="pix", opacity=1,
                                size=(width, height))
        img1.draw()
        win.flip()

        # Wait for User input.
        while (JoystickInput())['buttons_text'] == ' ':  # while presenting stimuli
            time.sleep(0.001)
            img1.draw();
            win.flip()
        while (JoystickInput())['buttons_text'] != ' ':  # while presenting stimuli
            time.sleep(0.001)

    # SetPort(3, 1, my_pathway)
    # Eyetracker start recording
    # if params['EyeTrackerSupport']:
    #
    #     message = visual.TextStim(win,
    #                               text="Eyetracker Calibration will start.  \n\nPress the spacebar when you are ready.",
    #                               units='norm', wrapWidth=2)
    #     message.draw();
    #     win.flip();
    #     waitUserSpace(Df, params)
    #
    #     iohub_config = {'eyetracker.hw.sr_research.eyelink.EyeTracker':
    #                         {'name': 'tracker',
    #                          'model_name': 'EYELINK 1000 DESKTOP',
    #                          'runtime_settings': {'sampling_rate': 500,
    #                                               'track_eyes': 'LEFT'}
    #                          }
    #                     }
    #     # Start new ioHub server.
    #     import psychopy.iohub.client
    #
    #     try:
    #         io = launchHubServer(**iohub_config)
    #     except:
    #         q = psychopy.iohub.client.ioHubConnection.getActiveConnection().quit()
    #         io = launchHubServer(**iohub_config)
    #     # Get the eye tracker device.
    #     tracker = io.devices.tracker
    #     tracker.sendCommand(
    #         "screen_pixel_coords = 0 0 %d %d" % (params['screenSize'][0] - 1, params['screenSize'][1] - 1))
    #
    #     # save screen resolution in EDF data, so Data Viewer can correctly load experimental graphics
    #     # see Data Viewer User Manual, Section 7: Protocol for EyeLink Data to Viewer Integration
    #     tracker.sendMessage("DISPLAY_COORDS = 0 0 %d %d" % (params['screenSize'][0] - 1, params['screenSize'][1] - 1))
    #
    #     # Eyetracker Calibration.
    #     c = 'c'
    #     while c != 'space':
    #         tracker = EyeTrackerCalibration(tracker)
    #         win.close()
    #         win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
    #         message = visual.TextStim(win,
    #                                   text="Calibration is completed.  Press the spacebar when you are ready to keep playing.\n Press 'c' to do calibration again.",
    #                                   units='norm', wrapWidth=2)
    #         message.draw();
    #         win.flip();
    #         c = waitUserSpaceAndC(Df, params)
    #     win.close()
    #
    #     # Eyetracker start recording
    #     tracker.setRecordingState(True)
    #     ELstartTime = time.time()
    #
    # win.close()
    # win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
    win.mouseVisible = False

    width = params["screenSize"][0]
    height = params["screenSize"][1]

    # Read Door Open Chance file provided by Rany.
    doorOpenChanceMap = np.squeeze((pd.read_csv('./input/doorOpenChance.csv', header=None)).values)
    # imgList = glob.glob(params['imageDir'] + params['imageSuffix'])
    # imgList = glob.glob(imgFolder + params['imageSuffix'])
    # tmp = []
    # for img in imgList:
    #     if "iti" in img: continue
    #     tmp.append(img)
    # imgList = tmp
    # imgList=

    totalCoin = 0

    if JoystickInput() == -1:
        print("There is no available Joystick.")
        exit()

    # if params['EyeTrackerSupport']:
    #     DfTR = ELIdxRecord(DfTR, params, SectionName, time.time() - ELstartTime, "",
    #                        "After Calibration Before Door Practice Game", "", "")
    #     tracker.sendMessage('TRIAL_RESULT 0')

    aoiTimeStart = time.time() * 1000
    for i in range(iterNum):
        debugClock.reset()
        # EDF labeling (start)
        # if params['EyeTrackerSupport']:
        #     tracker.sendMessage('TRIALID %d' % params["idxTR"])
        #     ELstartTime = time.time()

        params['subTrialCounter'] += 1
        Dict = {
            "ExperimentName": params['expName'],
            "Subject": params['subjectID'],
            "Session": params["Session"],
            "Version": params["Version"],
            "Section": SectionName,
            "Subtrial": params['subTrialCounter'],
            "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
        }

        # Pick up random image.
        # randN = random.randint(0, len(imgList) - 1)
        # if i % 49 == 0:
        #     random.shuffle(imgList)
        # imgFile = imgList[i % 49]
        imgFile = imgList.pop()
        # print(imgFile)
        if platform.system() == 'Windows':
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
        img1.draw();
        if 'debug' in params['subjectID']:
            level_text = visual.TextStim(win, text=f"Level: {level}", pos=(0.0, 0.0), units='norm', color='red',
                                         height=0.05, alignText='right')
            timer_text = visual.TextStim(win, text=f"{debugClock.getTime():.2f}s", pos=(0.1, 0.0), units='norm',
                                         color='red', height=0.04, alignText='right')
            status_text = visual.TextStim(win, text=f"door game play", pos=(0, 0.2), units='norm', color='red',
                                         height=0.05, alignText='right')
            level_text.text = f"Level: {level}"
            timer_text.text =f"{debugClock.getTime():.2f}s"
            timer_text.draw()
            level_text.draw()
            status_text.draw()
        win.flip();

        startTime = time.time()
        Dict["Distance_max"] = Dict["Distance_min"] = params["DistanceStart"]
        Dict["Distance_lock"] = 0
        MaxTime = params['DistanceLockWaitTime'] * 1000

        # Initial screen
        width = params['width_bank'][level]
        height = params['height_bank'][level]
        img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
        triggerGo(port, params, r, p, 1)  # Trigger: Door onset (conflict)
        count = 0
        joy = JoystickInput()
        position = (0, 0)
        rewardVSpunishment = "punishment" if random.random() < 0.5 else "reward"
        if rewardVSpunishment == "punishment":
            aoiInfo = " r" + str(r) + "p" + str(p) + "; p"
        else:
            aoiInfo = " r" + str(r) + "p" + str(p) + "; r"

        if 'debug' in params['subjectID']:
            # level_text = visual.TextStim(win, text=f"Level: {level}", pos=(0.9, 0.9), units='norm', color='red',
            #                              height=0.05, alignText='right')
            # timer_text = visual.TextStim(win, text=f"{debugClock.getTime():.2f}s", pos=(0.9, 0.8), units='norm',
            #                              color='red', height=0.04, alignText='right')
            level_text.draw()
            timer_text.text = f"{debugClock.getTime():.2f}s"
            timer_text.draw()


        # SetPort(3, 1, my_pathway)
        # event.waitKeys(maxWait=3)

        # my_pathway.start()

        # changed = True
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
            changed = True
            if joyUserInput < -0.5 and level < 100:
                level += 2
                level = min(100, level)
            elif joyUserInput < -0.1 - params['sensitivity'] * 0.1 and level < 100:
                level += 1
                level = min(100, level)
            elif joyUserInput > 0.5 and level > 0:
                level -= 2
                level = max(0, level)
            elif joyUserInput > 0.1 + params['sensitivity'] * 0.1 and level > 0:
                level -= 1
                level = max(0, level)
            else:
                changed = False

            width = params['width_bank'][level] if params['Version']!=3 else params['width_bank'][level]
            height = params['height_bank'][level] if params['Version']!=3 else params['height_bank'][level]
            # preInput = joyUserInput
            Dict["Distance_max"] = max(Dict["Distance_max"], level)
            Dict["Distance_min"] = min(Dict["Distance_min"], level)

            img1.size = (width, height)
            img1.draw();

            if 'debug' in params['subjectID']:
                # level_text = visual.TextStim(win, text=f"Level: {level}", pos=(0.9, 0.9), units='norm', color='red',
                #                              height=0.05, alignText='right')
                # timer_text = visual.TextStim(win, text=f"{debugClock.getTime():.2f}s", pos=(0.9, 0.8), units='norm',
                #                              color='red', height=0.04, alignText='right')
                level_text.text = f"Level: {level}"
                timer_text.text = f"{debugClock.getTime():.2f}s"
                timer_text.draw()
                level_text.draw()
                status_text.text=f"door game play. up to {params['DistanceLockWaitTime']}sec."
                status_text.draw()

            win.flip()
            get_keypress(Df, params)

        triggerGo(port, params, r, p, 2)  # Trigger: Joystick lock (start anticipation)
        Dict["DistanceFromDoor_SubTrial"] = level

        # if params['EyeTrackerSupport']:
        #     # Define last dynami AI before ending trial
        #     aoiTimeEnd = time.time() * 1000
        #     tracker.sendMessage('!V IAREA %d %d RECTANGLE %d %d %d %d %d %s' % (int(aoiTimeEnd - aoiTimeStart), 0,
        #                                                                         1, 512 - width * 105 / 1024,
        #                                                                         390 - height * 160 / 768,
        #                                                                         512 + width * 105 / 1024,
        #                                                                         390 + height * 200 / 768,
        #                                                                         'DOOR' + aoiInfo))
        #     # Reward
        #     tracker.sendMessage('!V IAREA %d %d RECTANGLE %d %d %d %d %d %s' % (int(aoiTimeEnd - aoiTimeStart), 0,
        #                                                                         2, 512 - width * 220 / 1024,
        #                                                                         390 - height * 155 / 768,
        #                                                                         512 - width * 130 / 1024,
        #                                                                         390 + height * 200 / 768,
        #                                                                         # 'Punishment Bar (Red bar)' + str(p)))
        #                                                                         'Punishment Bar (Red bar) ' + str(
        #                                                                             p) + aoiInfo))
        #
        #     # Punishment bar
        #     tracker.sendMessage('!V IAREA %d %d RECTANGLE %d %d %d %d %d %s' % (int(aoiTimeEnd - aoiTimeStart), 0,
        #                                                                         3, 512 + width * 220 / 1024,
        #                                                                         390 - height * 155 / 768,
        #                                                                         512 + width * 130 / 1024,
        #                                                                         390 + height * 200 / 768,
        #                                                                         'Reward Bar (Green bar) ' + str(
        #                                                                             r) + aoiInfo))
        #     tracker.sendMessage('TRIAL_RESULT 0')
        #     DfTR = ELIdxRecord(DfTR, params, SectionName, time.time() - ELstartTime, i,
        #                        "Playing Door Game (Before lock).", r, p)
        #     tracker.sendMessage('TRIALID %d' % params["idxTR"])
        #     tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (imgFile, 1024 / 2, 768 / 2, width, height))
        #     # Door
        #     tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, 512 - width * 105 / 1024,
        #                                                                   390 - height * 160 / 768,
        #                                                                   512 + width * 105 / 1024,
        #                                                                   390 + height * 200 / 768,
        #                                                                   'DOOR' + aoiInfo))
        #     # Reward
        #     tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (2, 512 - width * 220 / 1024,
        #                                                                   390 - height * 155 / 768,
        #                                                                   512 - width * 130 / 1024,
        #                                                                   390 + height * 200 / 768,
        #                                                                   'Punishment Bar (Red bar) ' + str(
        #                                                                       p) + aoiInfo))
        #
        #     # Punishment bar
        #     tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (3, 512 + width * 220 / 1024,
        #                                                                   390 - height * 155 / 768,
        #                                                                   512 + width * 130 / 1024,
        #                                                                   390 + height * 200 / 768,
        #                                                                   'Reward Bar (Green bar) ' + str(r) + aoiInfo))
        #
        #     ELstartTime = time.time()

        # Door Anticipation time
        # Dict["Door_anticipation_time"] = random.uniform(2, 4) * 1000
        # Dict["Door_anticipation_time"] = random.uniform(1, 3) * 1000
        # time.sleep(Dict["Door_anticipation_time"] / 1000)
        Dict["Door_anticipation_time"] = random.uniform(1, 3)
        wait_duration =  Dict["Door_anticipation_time"]
        debugClock.reset()
        timer = core.Clock()
        while timer.getTime() < wait_duration:
            if 'debug' in params['subjectID']:
                timer_text.text=f"{debugClock.getTime():.2f}s"
                img1.draw();
                level_text.draw()
                timer_text.draw()
                status_text.text=f"door anticipation time ({Dict['Door_anticipation_time']} sec)"
                status_text.draw()

                win.flip()



        # if params['EyeTrackerSupport']:
        #     tracker.sendMessage('TRIAL_RESULT 0')
        #     DfTR = ELIdxRecord(DfTR, params, SectionName, time.time() - ELstartTime, i,
        #                        "After lock: Door Anticipation Time.", r, p)
        #     tracker.sendMessage('TRIALID %d' % params["idxTR"])
        #     ELstartTime = time.time()

        Dict["Door_outcome"] = ""
        Dict["Door_opened"] = ""
        if random.random() > doorOpenChanceMap[level]:
            Dict["Door_opened"] = "closed"
            img1.draw();
            if 'debug' in params['subjectID']:
                # level_text = visual.TextStim(win, text=f"Level: {level}", pos=(0.9, 0.9), units='norm', color='red',
                #                              height=0.05, alignText='right')
                # timer_text = visual.TextStim(win, text=f"{debugClock.getTime():.2f}s", pos=(0.9, 0.8), units='norm',
                #                              color='red', height=0.04, alignText='right')
                level_text.text = f"Level: {level}"
                timer_text.text = f"{debugClock.getTime():.2f}s"
                timer_text.draw()
                level_text.draw()
                status_text.text=f"result:closed (2 sec)"
                status_text.draw()

                win.flip()
            triggerGo(port, params, r, p, 5)  # Door outcome: it didn’t open

            # if params['EyeTrackerSupport']:
            #     DfTR = ELIdxRecord(DfTR, params, SectionName, time.time() - ELstartTime, i,
            #                        "Reward screen (Door not opened) displayed.", r, p)
            #     ELstartTime = time.time()
        else:
            Dict["Door_opened"] = "opened"

            # if random.random() < 0.5:
            widthtmp = width if params['Version'] != 3 else width / 3.0
            heighttmp = height if params['Version'] != 3 else height / 3.0
            if rewardVSpunishment == "punishment":
                Dict["Door_outcome"] = "punishment"
                awardImg = "./img/outcomes/" + p + "_punishment.jpg"

                if params['HeatSupport']:
                    if int(p)<=2:
                        color=1
                    elif 3<int(p)<=5:
                        color=2
                    else:
                        color=3
                    # SetPort(3, 1, my_pathway)
                    # # from psychopy import core
                    # # timer = core.Clock()
                    # # timer.add(.1)
                    #
                    # SetPort(3, 1, my_pathway)
                    # # event.waitKeys(maxWait=10)
                    # # timer.add(.1)
                    # SetPort(3, 1, my_pathway)

                    # timer = core.Clock()
                    # timer.add(.1)

                    # my_pathway.trigger()
                    # event.waitKeys(maxWait=10)

                img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -heighttmp * 0.028],
                                        size=(widthtmp * 0.235, heighttmp * 0.464))
                message = visual.TextStim(win, text="-" + p, wrapWidth=2)
                message.pos = (0, 50)
                img1.draw();
                img2.draw();
                if 'debug' in params['subjectID']:
                    # level_text = visual.TextStim(win, text=f"Level: {level}", pos=(0.9, 0.9), units='norm', color='red',
                    #                              height=0.05, alignText='right')
                    # timer_text = visual.TextStim(win, text=f"{debugClock.getTime():.2f}s", pos=(0.9, 0.8), units='norm',
                    #                              color='red', height=0.04, alignText='right')
                    level_text.text = f"Level: {level}"
                    timer_text.text = f"{debugClock.getTime():.2f}s"
                    timer_text.draw()
                    level_text.draw()
                    status_text.text = f"result:punishment (4 sec)"
                    status_text.draw()
                message.draw();
                win.flip()
                triggerGo(port, params, r, p, 4)  # Door outcome: punishment
                totalCoin -= int(p)
            else:
                Dict["Door_outcome"] = "reward"
                awardImg = "./img/outcomes/" + r + "_reward.jpg"
                # widthtmp = width if params['Version']!=3 else width/3.5
                # heighttmp = height if params['Version'] != 3 else height / 3.5

                img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -heighttmp * 0.028],
                                        size=(widthtmp * 0.235, heighttmp * 0.464))
                message = visual.TextStim(win, text="+" + r, wrapWidth=2)
                message.pos = (0, 50)
                img1.draw();
                img2.draw();
                if 'debug' in params['subjectID']:
                    # level_text = visual.TextStim(win, text=f"Level: {level}", pos=(0.9, 0.9), units='norm', color='red',
                    #                              height=0.05, alignText='right')
                    # timer_text = visual.TextStim(win, text=f"{debugClock.getTime():.2f}s", pos=(0.9, 0.8), units='norm',
                    #                              color='red', height=0.04, alignText='right')
                    level_text.text = f"Level: {level}"
                    timer_text.text = f"{debugClock.getTime():.2f}s"
                    timer_text.draw()
                    level_text.draw()
                    status_text.text = f"result:reward (4 sec)"
                    status_text.draw()
                win.flip()
                triggerGo(port, params, r, p, 3)  # Door outcome: reward
                totalCoin += int(r)
            # if params['EyeTrackerSupport']:
            #     if Dict["Door_outcome"] == "reward":
            #         DfTR = ELIdxRecord(DfTR, params, SectionName, time.time() - ELstartTime, i,
            #                            "Reward screen (score:" + str(r) + ") displayed.", r, p)
            #     else:
            #         DfTR = ELIdxRecord(DfTR, params, SectionName, time.time() - ELstartTime, i,
            #                            "Punishment screen (score:" + str(p) + ") displayed.", r, p)
            #
            #     ELstartTime = time.time()

        # if params['EyeTrackerSupport']:
        #     if Dict["Door_outcome"] == "reward":
        #         resultReward = "reward (" + str(r) + ")" + aoiInfo
        #     elif Dict["Door_outcome"] == "punishment":
        #         resultReward = "punishment (" + str(p) + ")" + aoiInfo
        #     else:
        #         resultReward = "Door closed" + aoiInfo
        #
        #     if not os.path.exists('img/outscreenshot'):
        #         os.makedirs('img/outscreenshot')
        #
        #     if not os.path.exists('output/img/outscreenshot'):
        #         os.makedirs('output/img/outscreenshot')
        #
        #     imgScreenShot = './img/outscreenshot/ver' + str(Dict['Version']) + '_' + Dict["Door_opened"] + '_' + Dict[
        #         "Door_outcome"] + '_' + str(p) + '_' + str(r) + '_' + str(level) + '.jpg'
        #     imgScreenShot2 = './output/img/outscreenshot/ver' + str(Dict['Version']) + '_' + Dict["Door_opened"] + '_' + \
        #                      Dict["Door_outcome"] + '_' + str(p) + '_' + str(r) + '_' + str(level) + '.jpg'
        #
        #     win.getMovieFrame()  # Defaults to front buffer, I.e. what's on screen now.
        #     win.saveMovieFrames(imgScreenShot)
        #     shutil.copyfile(imgScreenShot, imgScreenShot2)
        #
        #     tracker.sendMessage('!V IMGLOAD CENTER %s %d %d %d %d' % (
        #     imgScreenShot, 1024 / 2, 768 / 2, params["screenSize"][0], params["screenSize"][1]))
        #     tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (1, 512 - width * 105 / 1024,
        #                                                                   390 - height * 160 / 768,
        #                                                                   512 + width * 105 / 1024,
        #                                                                   390 + height * 200 / 768,
        #                                                                   resultReward))
        if Dict["Door_outcome"] == "reward":
            mixer.init()
            mixer.music.load("./img/sounds/reward_sound.wav")
            mixer.music.play()
            # event.waitKeys(maxWait=2)
            # core.wait(2.0)  # Simple blocking pause
            wait_duration = 4.0
            debugClock.reset()
            timer = core.Clock()
            while timer.getTime() < wait_duration:
                if 'debug' in params['subjectID']:
                    timer_text.text=f"{debugClock.getTime():.2f}s"
                    img1.draw();
                    img2.draw();
                    level_text.draw()
                    timer_text.draw()
                    status_text.text = f"result:reward (4 sec)"
                    status_text.draw()
                    win.flip()

            mixer.music.stop()
            # sound1 = sound.Sound("./img/sounds/reward_sound.wav")
            # sound1.play()
            # event.waitKeys(maxWait=2)
            # sound1.stop()
        elif Dict["Door_outcome"] == "punishment":
            # SetPort(3, 1, my_pathway)
            # from psychopy import core
            # timer = core.Clock()
            # timer.add(.1)

            # SetPort(3, 1, my_pathway)
            # event.waitKeys(maxWait=10)
            # timer.add(.1)
            # SetPort(3, 1, my_pathway)
            SetPort(int(p),1)
            SetPort(int(p),1)
            SetPort(int(p),1)

            mixer.init()
            mixer.music.load("./img/sounds/punishment_sound.wav")
            mixer.music.play()
            # event.waitKeys(maxWait=2)

            # core.wait(4.0)  # Simple blocking pause
            wait_duration = 4.0
            debugClock.reset()
            timer = core.Clock()
            while timer.getTime() < wait_duration:
                if 'debug' in params['subjectID']:
                    timer_text.text=f"{debugClock.getTime():.2f}s"
                    img1.draw();
                    img2.draw();
                    level_text.draw()
                    timer_text.draw()
                    status_text.text = f"result:punishment (4 sec)"
                    status_text.draw()
                    win.flip()


            mixer.music.stop()
            # if params['HeatSupport']:
            #     my_pathway.trigger()
            # sound1 = sound.Sound("./img/sounds/punishment_sound.wav")
            # sound1.play()
            # event.waitKeys(maxWait=2)
            # sound1.stop()
        else:
            # event.waitKeys(maxWait=2)
            # core.wait(2.0)  # Simple blocking pause
            wait_duration = 4.0
            debugClock.reset()
            timer = core.Clock()
            while timer.getTime() < wait_duration:
                if 'debug' in params['subjectID']:
                    timer_text.text=f"{debugClock.getTime():.2f}s"
                    img1.draw();
                    # img2.draw();
                    level_text.draw()
                    timer_text.draw()
                    status_text.text = f"result:closed (2 sec)"
                    status_text.draw()
                    win.flip()

        # if params['EyeTrackerSupport']:
        #     tracker.sendMessage('TRIAL_RESULT 0')
        #     tracker.sendMessage('TRIALID %d' % params["idxTR"])

        # ITI duration
        # event.waitKeys(maxWait=5)
        # core.wait(5.0)  # Simple blocking pause
        # my_pathway.stop()
        # if params['EyeTrackerSupport']:
        #     startTime = time.time()
        #     width = params["screenSize"][0]
        #     height = params["screenSize"][1]
        #     tracker.sendMessage('!V IMGLOAD CENTER %s %d %d' % ("./img/ITI_fixation.jpg", width / 2, height / 2))
        #     tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % (
        #         1, int(335 * width / 1024), int(217 * height / 768), int(689 * width / 1024), int(561 * height / 768),
        #         'fixation treasure' + aoiInfo))
        #     WaitEyeGazed(win, params, tracker, False)
        #     Dict["ITI_duration"] = time.time() - startTime

        # else:
        width = params["screenSize"][0]
        height = params["screenSize"][1]
        img1 = visual.ImageStim(win=win, image="./img/iti.jpg" if params['Version']!=3 else "img/img_03312025/iti.jpg", units="pix", opacity=1, size=(width, height))
        img1.draw();
        if 'debug' in params['subjectID']:
            # level_text = visual.TextStim(win, text=f"Level: {level}", pos=(0.9, 0.9), units='norm', color='red',
            #                              height=0.05, alignText='right')
            # timer_text = visual.TextStim(win, text=f"{debugClock.getTime():.2f}s", pos=(0.9, 0.8), units='norm',
            #                              color='red', height=0.04, alignText='right')
            level_text.text = f"Level: {level}"
            timer_text.text = f"{debugClock.getTime():.2f}s"
            timer_text.draw()
            status_text.text = f"ITI (25 sec)"
            status_text.draw()
            level_text.draw()
        win.flip();
        # Dict["ITI_duration"] = random.uniform(1.5, 3.5) * 1000
        Dict["ITI_duration"] = 25
        # time.sleep(Dict["ITI_duration"] / 1000)
        # core.wait(Dict["ITI_duration"])
        wait_duration = Dict["ITI_duration"]
        debugClock.reset()
        timer = core.Clock()
        while timer.getTime() < wait_duration:
            if 'debug' in params['subjectID']:
                timer_text.text=f"{debugClock.getTime():.2f}s"
                img1.draw();
                status_text.text = f"ITI (25 sec)"
                status_text.draw()
                timer_text.draw()
                win.flip()

        # if params['EyeTrackerSupport']:
        #     tracker.sendMessage('TRIAL_RESULT 0')
        #     DfTR = ELIdxRecord(DfTR, params, SectionName, time.time() - ELstartTime, i, "ITI screen displayed.", "", "")

        Dict["Total_coins"] = totalCoin
        Df = tableWrite(Df, params, Dict)  # Log the dict result on pandas dataFrame.
        Df.to_csv(params['outFile_tmp'], sep=',', encoding='utf-8', index=False)

        # my_pathway.stop()

    # Eyetracker finish recording
    # if params['EyeTrackerSupport']:
    #     # Eyetracker stop recording
    #     tracker.setRecordingState(False)
    #
    #     # open a connection to the tracker and download the result file.
    #     trackerIO = pylink.EyeLink('100.1.1.1')
    #     trackerIO.receiveDataFile("et_data.EDF", params[SectionName])
    #
    #     # Stop the ioHub Server
    #     io.quit()
    #     trackerIO.close()
    win.mouseVisible = True
    return Df, DfTR, win,imgList
