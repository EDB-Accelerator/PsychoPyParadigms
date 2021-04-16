from psychopy import core, visual, event, sound,gui
import random, re, datetime, glob, time, platform
import pandas as pd
import numpy as np
from psychopy.hardware import joystick
import pygame
from sys import exit

def shutdown_key():
    core.quit()

def get_keypress(Df,params):
    keys = event.getKeys()
    if keys == ['q'] or keys == ['Q'] or keys == ['Esc']:
        # Write the output file.
        outFile = params['outFolder'] + '/' + str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
                  str(params['Version']) + '_' + datetime.datetime.now().strftime("%m%d%Y_%H%M%S") + ".csv"

        print(outFile)
        Df.to_csv(outFile, sep=',', encoding='utf-8', index=False)

        print('Q pressed. Forced Exit.')
        core.quit()

def ResolutionIntialization(params,size_diff):
    width_bank = []
    height_bank = []
    width0 = params["screenSize"][0]
    height0 = params["screenSize"][1]
    # size_diff = 1/100
    if params['resolutionMode'] == False:
        for level in range(0,101):
            width = width0 * (0.0909 + level * size_diff)
            height = height0 * (0.0909 + level * size_diff)
            width_bank.append(width)
            height_bank.append(height)
    else:
        for level in range(0,101):
            width = width0 * (0.1 + pow(level,1.7) * size_diff*0.05)
            height = height0 * (0.1 + pow(level,1.7) * size_diff*0.05)
            width_bank.append(width)
            height_bank.append(height)
    params['width_bank'] = width_bank
    params['height_bank'] = height_bank

def triggerGo(port,params,r,p,e):
    if params['triggerSupport']:
        s = (e - 1) * 7 ** 2 + (int(p) - 1) * 7 + (int(r) - 1)
        port.setData(s)

def waitAnyKeys():
    # Wait for user types a space key.
    core.wait(1 / 120)
    c = ['']
    while (c[0] == ''):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character
        if c == ['q'] or c == ['Q'] or c == ['Esc']:
            print('Q pressed. Forced Exit.')
            core.quit()

def waitUserSpace(Df,params):
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

        if c == ['q'] or c == ['Q'] or c == ['Esc']:
            # Write the output file.
            outFile = params['outFolder'] + '/' + str(params['subjectID']) + '_' + str(params['Session']) + '_' + \
                      str(params['Version']) + '_' + datetime.datetime.now().strftime("%m%d%Y_%H%M%S") + ".csv"

            Df.to_csv(outFile, sep=',', encoding='utf-8', index=False)

            print('Q pressed. Forced Exit.')
            core.quit()

# Function to wait for any user input.
def waitUserInput(Df,img,win,params,mode):
    # if params['JoyStickSupport'] == False:
    #     event.waitKeys(maxWait=3)
    # else:
    if mode == 'glfw':
        joystick.backend = 'glfw'  # must match the Window
    else:
        joystick.backend = 'pyglet'  # must match the Window
    nJoys = joystick.getNumJoysticks()  # to check if we have any
    if nJoys == 0:
        print("There is no available Joystick.")
        exit()
    joy = joystick.Joystick(0)  # id must be <= nJoys - 1
    startTime = time.time()

    count = 0
    pygame.joystick.quit()
    pygame.joystick.init()
    while count < 3:  # while presenting stimuli
        # joy.getButton(0)
        # if sum(joy.getAllButtons())!=0:
        if joy.getButton(0)!=0:
            # print(joy.getAllButtons)
            # break
            count += 1
        if (time.time() - startTime) > 100:
            break
        img.draw();win.flip()

    get_keypress(Df, params)
    img.draw();win.flip()

# Function to get user inputs.
def userInputPlay():
    userInput = gui.Dlg(title="DOORS Task Information")
    # userInput.addField('ExperimentName:',"Doors_AA_v8.py")
    userInput.addField('Subject Number:',23986)
    userInput.addField('Session:',1)
    # userInput.addField('Version:',1)
    userInput.addField('Version:', choices=[1, 2])
    userInput.addField('# of Practice Trials:', 5)
    userInput.addField('# of TaskRun1:', 49)
    userInput.addField('# of TaskRun2:', 49)
    userInput.addField('# of TaskRun3:', 49)
    # userInput.addField('Joystick Support:', True)
    userInput.addField('Trigger Support:', True)
    userInput.addField('Eyetracker Support:', True)
    # userInput.addField('Port Address', "0xE050")
    # userInput.addField('Screen Size (W)', 1024)
    # userInput.addField('Screen Size (H)', 780)
    # userInput.addField('Volume', 0.8)
    # userInput.addField('Resolution Mode (Check: Square, Uncheck: Linear)', True)

    return userInput.show()

# def userInputPlay():
#     userInput = gui.Dlg(title="DOORS Task Information")
#     userInput.addField('ExperimentName:',"Doors_AA_v8.py")
#     userInput.addField('Subject Number:',23986)
#     userInput.addField('Session:',1)
#     # userInput.addField('Version:',1)
#     userInput.addField('Version:', choices=[1, 2])
#     userInput.addField('# of Practice Trials:', 5)
#     userInput.addField('# of TaskRun1:', 98)
#     userInput.addField('# of TaskRun2:', 98)
#     # userInput.addField('Joystick Support:', True)
#     userInput.addField('Trigger Support:', True)
#     userInput.addField('Port Address', "0xE050")
#     userInput.addField('Screen Size (W)', 1024)
#     userInput.addField('Screen Size (H)', 780)
#     userInput.addField('Volume', 0.8)
#     userInput.addField('Resolution Mode (Check: Square, Uncheck: Linear)', True)
#
#     return userInput.show()

# Instruction Session Module.
def InstructionPlay(Df, win, params):
    Dict = {
        "ExperimentName": params['expName'],
        "Subject": params['subjectID'],
        "Session": params["Session"],
        "Version": params["Version"],
        "Section": "Instructions",
        "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S"),
    }

    width = params["screenSize"][1] * 1.294
    height = params["screenSize"][1]

    # Display Instruction
    message = visual.TextStim(win, text="Do you want to see the instruction?\n\n(y: Yes, n: No)",units='norm', wrapWidth=3)
    message.draw();
    win.flip();
    c = ['']
    # Wait for user types "y" or "n".
    while (c[0].upper() != "Y" and c[0].upper() != "N"):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character
        get_keypress(Df,params)

    # If user types "y", run instruction.
    if c[0].upper() == "Y":
        c = ['R']
        while (c[0].upper() == "R"):
            # core.wait(1 / 120)
            for i in range(1, 17):
                imgFile = "./instruction/Slide" + str(i) + ".JPG"
                img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
                img1.draw();
                win.flip();
                if i == 16:
                    c = event.waitKeys()
                else:
                    waitUserSpace(Df,params)

    # Log the dict result on pandas dataFrame.
    return tableWrite(Df, Dict)

# VAS Session Module.
def VASplay(Df, win, params, SectionName):
    # VAS Initialization.
    Dict = {'ExperimentName': params['expName'],
            "Subject": params['subjectID'],
            "Session": params['Session'],
            "Version": params['Version'],
            "Section": SectionName,
            "VAS_type": "Anxiety",
            "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")}

    # VAS Start Screen
    message = visual.TextStim(win, text="Before we continue, please answer a few questions. \n\n Press the spacebar to continue.",units='norm', wrapWidth=3)
    message.draw();win.flip()
    # waitUserInput(Df,message, win, params)
    waitUserSpace(Df,params)
    # event.waitKeys(maxWait=3)

    # VAS (Anxiety)
    startTime = time.time()
    Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(Df,params,win, "How anxious do you feel right now?",
                                                       ['Not anxious', 'Very anxious'])
    Dict["VAS_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # VAS (Avoidance)
    Dict["VAS_type"] = "Avoidance"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(Df,params,win, "How much do you feel like taking part in the task?",
                                                       ['Not at all', 'Very much'])
    Dict["VAS_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # VAS (Tired)
    Dict["VAS_type"] = "Tired"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(Df,params,win, "How tired are you right now?",
                                                       ['Not at all tired', 'Very tired'])
    Dict["VAS_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # VAS (Mood)
    Dict["VAS_type"] = "Mood"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(Df,params,win,
                                                       "Think about your mood right now. \nHow would you describe it?",
                                                       ['Worst mood ever', 'Best mood ever'])
    Dict["VAS_RT"] = (time.time() - startTime) * 1000
    return tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

# Question Session Module.
def Questionplay(Df, win, params, SectionName):
    Dict = {'ExperimentName': params['expName'],
            "Subject": params['subjectID'],
            "Session": params['Session'],
            "Version": params['Version'],
            "Section": SectionName,
            "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")}

    width = params["screenSize"][0]
    height = params["screenSize"][1]

    # Question (Won)
    Dict["Q_type"] = "Won"
    startTime = time.time()
    Dict["Q_score"], Dict["Q_RT"] = displayVAS(Df,params,win, "How many coins do you think you won?",
                                                       ['Won very few', 'Won very many'])
    Dict["Q_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # Question (Lost)
    Dict["Q_type"] = "Lost"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["Q_score"], Dict["Q_RT"] = displayVAS(Df,params,win, "How many coins do you think you lost?",
                                                       ['Lost very few', 'Lost very many'])
    Dict["Q_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # Question (Monster versus Coin)
    Dict["Q_type"] = "Before"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["Q_score"], Dict["Q_RT"] = displayVAS(Df,params,win, "Before the door opened, what did you think you would see?",
                                                       ['Monster', 'Coins'])
    Dict["Q_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # Question (Monster)
    Dict["Q_type"] = "Monster"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["Q_score"], Dict["Q_RT"] = displayVAS(Df,params,win, "How often did you see the monster when the door opened?",
                                                       ['Never', 'All the time'])
    Dict["Q_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # Question (Coins)
    Dict["Q_type"] = "Coins"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["Q_score"], Dict["Q_RT"] = displayVAS(Df,params,win,"How often did you win coins when the door opened?",
                                                       ['Never', 'All the time'])
    Dict["Q_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # Question (Performance)
    Dict["Q_type"] = "Performance"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["Q_score"], Dict["Q_RT"] = displayVAS(Df,params,win,"How do you feel about how well you’ve done so far?",
                                               ["I didn't do well","I did very well"])
    Dict["Q_RT"] = (time.time() - startTime) * 1000

    # Log the dict result on pandas dataFrame.
    Df = tableWrite(Df, Dict)

    # Ending Screen
    img1 = visual.ImageStim(win=win, image="./instruction/end_slide.jpg", units="pix", opacity=1, size=(width, height))
    # waitUserInput(Df,img1, win, params)
    img1.draw();
    win.flip()
    waitUserSpace(Df,params)

    return Df

# Door Game Session Module.


# Df,win,params,params['numTaskRun1'],port,"TaskRun1"
# SectionName = "TaskRun1"
# iterNum = params['numTaskRun1']

def DoorGamePlay(Df, win, params, iterNum, port, SectionName):

    width = params["screenSize"][0]
    height = params["screenSize"][1]

    # if params['JoyStickSupport'] == False:
    #     return DoorGamePlay_keyboard(Df,win,params,iterNum,SectionName)
    if SectionName == "TaskRun1":
        img1 = visual.ImageStim(win=win, image="./instruction/start_main_game.jpg", units="pix", opacity=1,size=(width, height))
        waitUserInput(Df,img1, win, params,'glfw')

    # Read Door Open Chance file provided by Rany.
    doorOpenChanceMap = np.squeeze((pd.read_csv('./input/doorOpenChance.csv',header=None)).values)
    imgList = glob.glob(params['imageDir'] + params['imageSuffix'])

    totalCoin = 0

    # Joystick Initialization
    joystick.backend = 'glfw'  # must match the Window
    nJoys = joystick.getNumJoysticks()  # to check if we have any
    if nJoys == 0:
        print("There is no available Joystick.")
        exit()
    joy = joystick.Joystick(0)  # id must be <= nJoys - 1
    # if sum(joy.getAllButtons()) != 0:
    #     break

    # Shuffle image. # https://pynative.com/python-random-shuffle/

    for i in range(iterNum):
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
        # width = params["screenSize"][0] * (1 - level / 110)
        # height = params["screenSize"][1] * (1 - level / 110)
        width = params['width_bank'][level]
        height = params['height_bank'][level]
        img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
        img1.draw();
        win.flip()
        triggerGo(port, params, r, p, 1) # Trigger: Door onset (conflict)
        count = 0
        pygame.joystick.quit()
        pygame.joystick.init()
        preInput =  joy.getY()
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

            width = params['width_bank'][level]
            height = params['height_bank'][level]
            # preInput = joyUserInput
            Dict["Distance_max"] = max(Dict["Distance_max"], level)
            Dict["Distance_min"] = min(Dict["Distance_min"], level)

            img1.size = (width, height)
            img1.draw();win.flip()
            # print("level:" + str(level))
            get_keypress(Df,params)

        triggerGo(port, params, r, p, 2) # Trigger: Joystick lock (start anticipation)
        Dict["DistanceFromDoor_SubTrial"] = level

        # Door Anticipation time
        Dict["Door_anticipation_time"] = random.uniform(2, 4) * 1000
        time.sleep(Dict["Door_anticipation_time"] / 1000)

        if random.random() > doorOpenChanceMap[level]:
            Dict["Door_opened"] = "closed"
            img1.draw();win.flip()
            triggerGo(port, params, r, p, 5)  # Door outcome: it didn’t open
            event.waitKeys(maxWait=2)
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

        # ITI duration
        width = params["screenSize"][0]
        height = params["screenSize"][1]
        img1 = visual.ImageStim(win=win, image="./img/iti.jpg", units="pix", opacity=1, size=(width, height))
        img1.draw();win.flip();
        Dict["ITI_duration"] = random.uniform(1.5, 3.5) * 1000
        time.sleep(Dict["ITI_duration"] / 1000)

        Dict["Total_coins"] = totalCoin
        Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    return Df

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

def tableWrite(Df, Dict):
    # Move data in Dict into Df.
    Df = Df.append(pd.Series(dtype=float), ignore_index=True)  # Insert Empty Rows
    for key in Dict:
        Df[key].loc[len(Df) - 1] = Dict[key]  # FYI, len(Df)-1: means the last row of pandas dataframe.
    return Df


def displayVAS(Df,params,win, text, labels):
    scale = visual.RatingScale(win,
                               labels=labels,  # End points
                               scale=None,  # Suppress default
                               # markerStart=50,
                               low=0, high=100, tickHeight=0, precision=1, size = 2,textSize = 0.6,
                               acceptText='Continue', showValue=False, showAccept=True,markerColor="Yellow")  # markerstart=50
    myItem = visual.TextStim(win, text=text, height=.12, units='norm',pos=[0,0.3], wrapWidth=2)

    # Show scale and measure the elapsed wall-clock time.
    startTime = time.time()
    while scale.noResponse:
        scale.draw()
        myItem.draw()
        win.flip()
        get_keypress(Df,params)
    endTime = time.time()
    win.flip()
    return scale.getRating(), endTime - startTime

def fadeInOutImage(win, image, duration, size):
    for i in range(60):
        opacity = 1 / 60 * (i + 1)
        img = visual.ImageStim(win=win, image=image, units="pix", opacity=opacity, size=size)
        img.draw();win.flip()
        core.wait(duration / 60)

    for i in range(60):
        opacity = 1 - 1 / 60 * (i + 1)
        img = visual.ImageStim(win=win, image=image, units="pix", opacity=opacity, size=size)
        img.draw();win.flip()
        core.wait(duration / 60)


def displayText(win, textString):
    message = visual.TextStim(win, text=textString)
    message.draw()
    win.flip()
