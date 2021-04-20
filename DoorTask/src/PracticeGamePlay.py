import sys
sys.path.insert(1, './src')

from psychopy import core, visual, event, sound,gui
from Helper import waitUserSpace,displayVAS,tableWrite,get_keypress,waitUserInput,triggerGo
import random, re, datetime, glob, time, platform
import pygame
from psychopy.hardware import joystick

# Door Game Session Module.
def PracticeGamePlay(Df, win, params, iterNum, port,SectionName):

    # if params['JoyStickSupport'] == False:
    #     return DoorGamePlay_keyboard(Df,win,params,iterNum,SectionName)

    width = params["screenSize"][0]
    height = params["screenSize"][1]

    # Start Section Display
    img1 = visual.ImageStim(win=win, image="./instruction/practice_start.jpg", units="pix", opacity=1,size=(width, height))
    # text1 = visual.TextStim(win, text="Press Any Buttons on Joystick to Continue", height=.12, units='norm', pos=[0, -0.3], wrapWidth=2)
    # text1.draw
    waitUserInput(Df,img1, win, params,'glfw')

    # Read Door Open Chance file provided by Rany.
    imgList = glob.glob("./img/practice/*_door.jpg")

    # Joystick Initialization
    joystick.backend = 'glfw'  # must match the Window
    nJoys = joystick.getNumJoysticks()  # to check if we have any
    if nJoys == 0:
        print("There is no available Joystick.")
        exit()
    joy = joystick.Joystick(0)  # id must be <= nJoys - 1
    for i in range(iterNum):
        Dict = {
            "ExperimentName" : params['expName'],
            "Subject" : params['subjectID'],
            "Session" : params["Session"],
            "Version" : params["Version"],
            "Section" : SectionName,
            "SessionStartDateTime" : datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
        }

        # Pick up random image.
        randN = random.randint(0, len(imgList) - 1)
        imgFile = imgList[randN]

        # Display the image.
        c = ['']
        level = Dict["Distance_start"] = params["DistanceStart"]
        # width = params["screenSize"][0] * (1 - level / 110)
        # height = params["screenSize"][1] * (1 - level / 110)
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
        img1.draw();
        triggerGo(port, params, 1, 1, 1)  # Door onset (conflict)
        win.flip()
        count = 0
        pygame.joystick.quit()
        pygame.joystick.init()
        preInput = joy.getY()
        while count < 3:  # while presenting stimuli
            # If waiting time is longer than 10 sec, exit this loop.
            Dict["DoorAction_RT"] = (time.time() - startTime) * 1000
            if Dict["DoorAction_RT"] > MaxTime:
                c[0] = "timeisUp"
                break
            # if (sum(joy.getAllButtons()) != 0):
            if joy.getButton(0)!=0:
                count += 1
                if count >= 2:
                    Dict["Distance_lock"] = 1
                    break

            joyUserInput = joy.getY()

            if joyUserInput < -0.1 and level < 100:
                level += 1
                level = min(100,level)
            elif joyUserInput > 0.1 and level > 0:
                level -= 1
                level = max(0,level)
            get_keypress(Df,params)
            width = params['width_bank'][level]
            height = params['height_bank'][level]

            # preInput = joyUserInput
            Dict["Distance_max"] = max(Dict["Distance_max"], level)
            Dict["Distance_min"] = min(Dict["Distance_min"], level)

            img1.size = (width, height)
            img1.draw();win.flip()
            # print("level :", str(level))


        triggerGo(port, params, 1, 1, 2)  # Joystick lock (start anticipation)
        Dict["DistanceFromDoor_SubTrial"] = level

        # Door Anticipation time
        Dict["Door_anticipation_time"] = random.uniform(2, 4) * 1000
        time.sleep(Dict["Door_anticipation_time"] / 1000)

        awardImg = "./img/practice/practice_outcome.jpg"
        # width = params["screenSize"][0] * 0.265 * (1 - level / 110)
        # height = params["screenSize"][1] * 0.5 * (1 - level / 110)
        img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -height * 0.028],
                                size=(width* 0.235, height* 0.464))
        # waitUserInput(Df,img2, win, params)
        img1.draw();img2.draw();win.flip()
        event.waitKeys(maxWait=2)

        # Dict["ITI_duration"] = random.uniform(1.5, 3.5) * 1000
        # time.sleep(Dict["ITI_duration"] / 1000)

        # ITI duration
        width = params["screenSize"][0]
        height = params["screenSize"][1]
        img1 = visual.ImageStim(win=win, image="./img/iti.jpg", units="pix", opacity=1, size=(width, height))
        img1.draw();win.flip();
        Dict["ITI_duration"] = random.uniform(1.5, 3.5) * 1000
        time.sleep(Dict["ITI_duration"] / 1000)

        Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    return Df