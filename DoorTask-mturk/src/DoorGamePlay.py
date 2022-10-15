import sys

sys.path.insert(1, './src')

from psychopy import visual, event, sound
from pygame import mixer
from Helper import waitUserSpace, tableWrite, get_keypress, waitUserSpaceAndC
from JoystickInput import JoystickInput
import random, re, datetime, glob, time, platform
import pylink
import numpy as np
import pandas as pd
from WaitEyeGazed import WaitEyeGazed
from ELIdxRecord import ELIdxRecord
from psychopy.iohub import launchHubServer
import shutil
import os

def DoorGamePlay(Df, DfTR, win, params, iterNum, SectionName):
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

    win.close()
    win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
    win.mouseVisible = False

    width = params["screenSize"][0]
    height = params["screenSize"][1]

    # Read Door Open Chance file provided by Rany.
    doorOpenChanceMap = np.squeeze((pd.read_csv('./input/doorOpenChance.csv', header=None)).values)
    imgList = glob.glob(params['imageDir'] + params['imageSuffix'])
    totalCoin = 0

    if JoystickInput() == -1:
        print("There is no available Joystick.")
        exit()

    aoiTimeStart = time.time() * 1000
    for i in range(iterNum):

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
        if i % 49 == 0:
            random.shuffle(imgList)
        imgFile = imgList[i % 49]

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
        win.flip();

        startTime = time.time()
        Dict["Distance_max"] = Dict["Distance_min"] = params["DistanceStart"]
        Dict["Distance_lock"] = 0
        MaxTime = params['DistanceLockWaitTime'] * 1000

        # Initial screen
        width = params['width_bank'][level]
        height = params['height_bank'][level]
        img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
        count = 0
        joy = JoystickInput()
        position = (0, 0)
        rewardVSpunishment = "punishment" if random.random() < 0.5 else "reward"
        if rewardVSpunishment == "punishment":
            aoiInfo = " r" + str(r) + "p" + str(p) + "; p"
        else:
            aoiInfo = " r" + str(r) + "p" + str(p) + "; r"

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

            width = params['width_bank'][level]
            height = params['height_bank'][level]
            # preInput = joyUserInput
            Dict["Distance_max"] = max(Dict["Distance_max"], level)
            Dict["Distance_min"] = min(Dict["Distance_min"], level)

            img1.size = (width, height)
            img1.draw();
            win.flip()
            get_keypress(Df, params)

        Dict["DistanceFromDoor_SubTrial"] = level

        # Door Anticipation time
        Dict["Door_anticipation_time"] = random.uniform(2, 4) * 1000
        time.sleep(Dict["Door_anticipation_time"] / 1000)

        Dict["Door_outcome"] = ""
        Dict["Door_opened"] = ""
        if random.random() > doorOpenChanceMap[level]:
            Dict["Door_opened"] = "closed"
            img1.draw();
            win.flip()

        else:
            Dict["Door_opened"] = "opened"

            # if random.random() < 0.5:
            if rewardVSpunishment == "punishment":
                Dict["Door_outcome"] = "punishment"
                awardImg = "./img/outcomes/" + p + "_punishment.jpg"
                img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -height * 0.028],
                                        size=(width * 0.235, height * 0.464))
                message = visual.TextStim(win, text="-" + p, wrapWidth=2)
                message.pos = (0, 50)
                img1.draw();
                img2.draw();
                message.draw();
                win.flip()
                totalCoin -= int(p)
            else:
                Dict["Door_outcome"] = "reward"
                awardImg = "./img/outcomes/" + r + "_reward.jpg"
                img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -height * 0.028],
                                        size=(width * 0.235, height * 0.464))
                message = visual.TextStim(win, text="+" + r, wrapWidth=2)
                message.pos = (0, 50)
                img1.draw();
                img2.draw();
                win.flip()
                totalCoin += int(r)
            if params['EyeTrackerSupport']:
                if Dict["Door_outcome"] == "reward":
                    DfTR = ELIdxRecord(DfTR, params, SectionName, time.time() - ELstartTime, i,
                                       "Reward screen (score:" + str(r) + ") displayed.", r, p)
                else:
                    DfTR = ELIdxRecord(DfTR, params, SectionName, time.time() - ELstartTime, i,
                                       "Punishment screen (score:" + str(p) + ") displayed.", r, p)

                ELstartTime = time.time()

        if Dict["Door_outcome"] == "reward":
            # mixer.init()
            # mixer.music.load("./img/sounds/reward_sound.wav")
            # mixer.music.play()
            # event.waitKeys(maxWait=2)
            # mixer.music.stop()
            sound1 = sound.Sound("./img/sounds/reward_sound.wav")
            sound1.play()
            event.waitKeys(maxWait=2)
            sound1.stop()
        elif Dict["Door_outcome"] == "punishment":
            # mixer.init()
            # mixer.music.load("./img/sounds/punishment_sound.wav")
            # mixer.music.play()
            # event.waitKeys(maxWait=2)
            # mixer.music.stop()
            sound1 = sound.Sound("./img/sounds/punishment_sound.wav")
            sound1.play()
            event.waitKeys(maxWait=2)
            sound1.stop()
        else:
            event.waitKeys(maxWait=2)

        width = params["screenSize"][0]
        height = params["screenSize"][1]
        img1 = visual.ImageStim(win=win, image="./img/iti.jpg", units="pix", opacity=1, size=(width, height))
        img1.draw();
        win.flip();
        Dict["ITI_duration"] = random.uniform(1.5, 3.5) * 1000
        time.sleep(Dict["ITI_duration"] / 1000)

        Dict["Total_coins"] = totalCoin
        Df = tableWrite(Df, params, Dict)  # Log the dict result on pandas dataFrame.

    win.mouseVisible = True
    return Df, DfTR, win
