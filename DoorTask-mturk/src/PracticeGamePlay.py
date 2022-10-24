import sys
sys.path.insert(1, './src')

from psychopy import visual, event
from psychopy.hardware import keyboard
from Helper import tableWrite,get_keypress,triggerGo,waitUserSpace,waitUserSpaceAndC
import random, datetime, glob, time
from ELIdxRecord import ELIdxRecord
from WaitEyeGazed import WaitEyeGazed
import time

# Debuging
# PracticeGamePlay(Df, win, params, params['numPractice'], port, "Practice")
# iterNum = params['numPractice']; SectionName = "Practice"

def newPoint(n,center,ratio):
    return int((n-center) * ratio + center)

# Door Game Session Module.
def PracticeGamePlay(Df, DfTR,win, params, iterNum, SectionName):

    # Eyetracker start recording
    params["idxTR"] = 0

    # win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
    win.mouseVisible = False

    width = params["screenSize"][0]
    height = params["screenSize"][1]

    # Start Section Display
    img1 = visual.ImageStim(win=win, image="./instruction/practice_start.jpg", units="pix", opacity=1,size=(width, height))
    # waitUserInput(Df,img1, win, params,'glfw')
    img1.draw();win.flip()

    # Wait for User input.
    # while (JoystickInput())['buttons_text'] == ' ':  # while presenting stimuli
    #     time.sleep(0.001)
    #     img1.draw();
    #     win.flip()
    # while (JoystickInput())['buttons_text'] != ' ':  # while presenting stimuli
    #     time.sleep(0.001)
    waitUserSpace(Df, params)

    # Read Door Open Chance file provided by Rany.
    imgList = glob.glob("./img/practice/*_door.jpg")

    aoiTimeStart = time.time() * 1000
    for i in range(iterNum):

        # # EDF labeling (start)
        # if params['EyeTrackerSupport']:
        #     tracker.sendMessage('TRIALID %d' % params["idxTR"])
        #     ELstartTime = time.time()

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
        startTime = time.time()

        Dict["Distance_max"] = Dict["Distance_min"] = params["DistanceStart"]
        Dict["Distance_lock"] = 0
        MaxTime = params['DistanceLockWaitTime'] * 1000

        # Initial screen
        width = params['width_bank'][level]
        height = params['height_bank'][level]
        img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
        # img1.draw();

        # if params['EyeTrackerSupport']:
        #     position = (0,0)
        #     circle = visual.Circle(win=win, units="pix", fillColor='black', lineColor='white', edges=1000, pos=position,
        #                            radius=5)
        #
        #     # tracker.sendMessage('!V IMGLOAD CENTER %s %d %d' % (imgFile, 1024/2, 768 / 2))

        win.flip()

        # count = 0
        # joy = JoystickInput()

        kb = keyboard.Keyboard()
        kb.clock.reset()  # when you want to start the timer from
        # c = kb.getKeys(['1', '2', '3'], waitRelease=False, clear=True)
        # while count < 4:  # while presenting stimuli
        c = [""]
        while True:  # while presenting stimuli
            # If waiting time is longer than 10 sec, exit this loop.
            Dict["DoorAction_RT"] = (time.time() - startTime) * 1000
            if Dict["DoorAction_RT"] > MaxTime:
                c = ["timeisUp"]
                break

            # c = event.getKeys(waitRelease=False)
            # c = kb.getKeys(['1','2','3'],waitRelease=False,clear = False)
            c = kb.getKeys(waitRelease=False, clear=True)
            # clear = False
            # print(len(c))
            # for key in c:
            #     print(key.name, key.rt, key.duration)

            # print(pygame.key.get_pressed())
            # print(level)
            if c == ['1']:
                level += 2
                level = min(100,level)
            elif c == ['2']:
                level -= 2
                level = max(0,level)
            elif c == ['3']:
                Dict["Distance_lock"] = 1
                break

            width = params['width_bank'][level]
            height = params['height_bank'][level]

            Dict["Distance_max"] = max(Dict["Distance_max"], level)
            Dict["Distance_min"] = min(Dict["Distance_min"], level)

            img1.size = (width, height)
            img1.draw()
            win.flip()

        Dict["DistanceFromDoor_SubTrial"] = level

        # Door Anticipation time
        Dict["Door_anticipation_time"] = random.uniform(2, 4) * 1000
        time.sleep(Dict["Door_anticipation_time"] / 1000)

        awardImg = "./img/practice/practice_outcome.jpg"
        img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -height * 0.028],
                                size=(width* 0.235, height* 0.464))
        img1.draw();img2.draw();win.flip()
        event.waitKeys(maxWait=2)

        # else:
        width = params["screenSize"][0]
        height = params["screenSize"][1]
        img1 = visual.ImageStim(win=win, image="./img/iti.jpg", units="pix", opacity=1, size=(width, height))
        img1.draw();win.flip();
        Dict["ITI_duration"] = random.uniform(1.5, 3.5) * 1000
        time.sleep(Dict["ITI_duration"] / 1000)

        Df = tableWrite(Df, params,Dict)  # Log the dict result on pandas dataFrame.

    win.mouseVisible = True
    return Df,DfTR,win,c

