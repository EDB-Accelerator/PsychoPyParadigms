from psychopy import core, visual, event, sound,gui
import random, re, datetime, glob, time, platform
import pandas as pd
import numpy as np
from psychopy.hardware import joystick

# Function to wait for any user input.
def waitUserInput(img,win,params):
    if params['JoyStickSupport'] == False:
        event.waitKeys(maxWait=3)
    else:
        joystick.backend = 'pyglet'  # must match the Window
        nJoys = joystick.getNumJoysticks()  # to check if we have any
        if nJoys == 0:
            print("There is no available Joystick.")
            exit(1)
        joy = joystick.Joystick(0)  # id must be <= nJoys - 1
        startTime = time.time()

        while True:  # while presenting stimuli
            if sum(joy.getAllButtons())!=0:
                break
            if (time.time() - startTime) > 5:
                break
            img.draw();win.flip()
        img.draw();win.flip()

# Function to get user inputs.
def userInputPlay():
    userInput = gui.Dlg(title="DOORS Task Information")
    userInput.addField('ExperimentName:',"Doors_AA_v8.py")
    userInput.addField('Subject Number:',23986)
    userInput.addField('Session:',1)
    # userInput.addField('Version:',1)
    userInput.addField('Version:', choices=[1, 2])
    userInput.addField('# of Practice Trials:', 5)
    userInput.addField('# of TaskRun1:', 98)
    userInput.addField('# of TaskRun2:', 98)
    userInput.addField('Joystick Support:', True)
    return userInput.show()

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

    # Display Instruction
    message = visual.TextStim(win, text="Do you want to see the instruction? (y: Yes, n: No)")
    message.draw();
    win.flip();
    c = ['']
    # Wait for user types "y" or "n".
    while (c[0].upper() != "Y" and c[0].upper() != "N"):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

    # If user types "y", run instruction.
    if c[0].upper() == "Y":
        c = ['R']
        while (c[0].upper() == "R"):
            core.wait(1 / 120)
            for i in range(1, 17):
                imgFile = "./instruction/Slide" + str(i) + ".JPG"
                img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(1200, 800))
                img1.draw();
                win.flip();
                if i == 16:
                    c = event.waitKeys()
                else:
                    waitUserInput(img1, win, params)

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
    message = visual.TextStim(win, text="Before we continue, please answer a few questions.")
    message.draw();win.flip()
    waitUserInput(message, win, params)
    # event.waitKeys(maxWait=3)

    # VAS (Anxiety)
    startTime = time.time()
    Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(win, "How anxious do you feel right now?",
                                                       ['Not anxious', 'Very anxious'])
    Dict["VAS_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # VAS (Avoidance)
    Dict["VAS_type"] = "Avoidance"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(win, "How much do you feel like taking part in the task?",
                                                       ['Not at all', 'Very much'])
    Dict["VAS_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # VAS (Tired)
    Dict["VAS_type"] = "Tired"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(win, "How tired are you right now?",
                                                       ['Not at all tired', 'Very tired'])
    Dict["VAS_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # VAS (Mood)
    Dict["VAS_type"] = "Mood"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(win,
                                                       "Think about your mood right now. How would you describe it?",
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

    # Question (Won)
    Dict["Q_type"] = "Won"
    startTime = time.time()
    Dict["Q_score"], Dict["Q_RT"] = displayVAS(win, "How many coins do you think you won?",
                                                       ['Won very few', 'Won very many'])
    Dict["Q_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # Question (Lost)
    Dict["Q_type"] = "Lost"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["Q_score"], Dict["Q_RT"] = displayVAS(win, "How many coins do you think you lost?",
                                                       ['Lost very few', 'Lost very many'])
    Dict["Q_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # Question (Monster)
    Dict["Q_type"] = "Monster"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["Q_score"], Dict["Q_RT"] = displayVAS(win, "How often did you see the monster when the door opened?",
                                                       ['Never', 'All the time'])
    Dict["Q_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # Question (Coins)
    Dict["Q_type"] = "Coins"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["Q_score"], Dict["Q_RT"] = displayVAS(win,"How often did you win coins when the door opened?",
                                                       ['Never', 'All the time'])
    Dict["Q_RT"] = (time.time() - startTime) * 1000
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # Question (Performance)
    Dict["Q_type"] = "Performance"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = time.time()
    Dict["Q_score"], Dict["Q_RT"] = displayVAS(win,"How do you feel about how well you’ve done so far?",
                                               ["I didn't do well","I did very well"])
    Dict["Q_RT"] = (time.time() - startTime) * 1000

    # Log the dict result on pandas dataFrame.
    Df = tableWrite(Df, Dict)

    return Df


# Door Game Session Module.
def DoorGamePlay(Df, win, params, iterNum, SectionName):

    if params['JoyStickSupport'] == False:
        return DoorGamePlay_keyboard(Df,win,params,iterNum,SectionName)
    # Start Section Display
    message = visual.TextStim(win, text="Now [" + SectionName + "] Section is started.")
    waitUserInput(message, win, params)

    # Read Door Open Chance file provided by Rany.
    # doorOpenChanceMap = np.squeeze((pd.read_csv('./input/doorOpenChance.csv')).to_numpy())
    doorOpenChanceMap = np.squeeze((pd.read_csv('./input/doorOpenChance.csv',header=None)).values)
    imgList = glob.glob(params['imageDir'] + params['imageSuffix'])
    totalCoin = 0

    # Joystick Initialization
    joystick.backend = 'pyglet'  # must match the Window
    nJoys = joystick.getNumJoysticks()  # to check if we have any
    if nJoys == 0:
        print("There is no available Joystick.")
        exit()
    joy = joystick.Joystick(0)  # id must be <= nJoys - 1
    # if sum(joy.getAllButtons()) != 0:
    #     break
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
        # print(imgFile)
        # print(imgFile.split('/')[-1])

        if platform.system() =='Windows':
            p, r = re.findall(r'\d+', imgFile.split('\\')[-1])
        else:
            p, r = re.findall(r'\d+', imgFile.split('/')[-1])

        Dict["Punishment_magnitude"] = p
        Dict["Reward_magnitude"] = r

        # Display the image.
        c = ['']
        level = Dict["Distance_start"] = params["DistanceStart"]
        width = params["screenSize"][0] * (1 - level / 110)
        height = params["screenSize"][1] * (1 - level / 110)
        img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
        img1.draw();win.flip();

        startTime = time.time()
        Dict["Distance_max"] = Dict["Distance_min"] = params["DistanceStart"]
        Dict["Distance_lock"] = 0
        MaxTime = params['DistanceLockWaitTime'] * 1000


        # Initial screen
        width = params["screenSize"][0] * (1 - level / 110)
        height = params["screenSize"][1] * (1 - level / 110)
        img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
        img1.draw();
        win.flip()
        while True:  # while presenting stimuli
            # If waiting time is longer than 10 sec, exit this loop.
            Dict["DoorAction_RT"] = (time.time() - startTime) * 1000
            if Dict["DoorAction_RT"] > MaxTime:
                c[0] = "timeisUp"
                break
            if (sum(joy.getAllButtons()) != 0):
                Dict["Distance_lock"] = 1
                break

            joyUserInput = joy.getY()
            if joyUserInput != 1 and joyUserInput != -1:
                img1.draw();win.flip()
                continue

            if joyUserInput == 1 and level > 0:
                level -= 1
            elif joyUserInput == -1 and level < 100:
                level += 1

            Dict["Distance_max"] = max(Dict["Distance_max"], level)
            Dict["Distance_min"] = min(Dict["Distance_min"], level)

            width = params["screenSize"][0] * (1 - level / 110)
            height = params["screenSize"][1] * (1 - level / 110)
            # img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
            img1.size = (width, height)
            img1.draw();win.flip()

        Dict["DistanceFromDoor_SubTrial"] = level

        # Door Anticipation time
        Dict["Door_anticipation_time"] = random.uniform(2, 4) * 1000
        time.sleep(Dict["Door_anticipation_time"] / 1000)

        if random.random() < doorOpenChanceMap[level]:
            Dict["Door_opened"] = "closed"
            # img1 = visual.ImageStim(win=win, image="./img/door_100.jpg", units="pix", opacity=1)
            # img1.draw();win.flip();event.waitKeys(maxWait=3)
            # displayText(win, "Door Closed\n\n Total totalCoin: " + str(totalCoin))
            displayText(win, "Door Closed")
            # event.waitKeys(maxWait=3)
            # continue
        else:
            Dict["Door_opened"] = "opened"
            if random.random() < 0.5:
                Dict["Door_outcome"] = "punishment"
                awardImg = "./img/outcomes/" + p + "_punishment.jpg"
                width = 200 * (1 - level / 110)
                height = 400 * (1 - level / 110)
                img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -10],
                                        size=(width, height))
                message = visual.TextStim(win, text="-" + p, wrapWidth=2)
                message.pos = (0, 50)
                img1.draw();img2.draw();message.draw();win.flip()
                sound1 = sound.Sound("./img/sounds/punishment_sound.wav")
                sound1.play()
                event.waitKeys(maxWait=3)
                sound1.stop()
                totalCoin -= int(p)
                # displayText(win, "Lose your totalCoin: " + str(p) + "!!\n\n Total totalCoin: " + str(totalCoin))
                displayText(win, "-" + str(p))
            else:
                Dict["Door_outcome"] = "reward"
                awardImg = "./img/outcomes/" + r + "_reward.jpg"
                width = 200 * (1 - level / 110)
                height = 400 * (1 - level / 110)
                img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -10],
                                        size=(width, height))
                message = visual.TextStim(win, text="+" + r, wrapWidth=2)
                message.pos = (0, 50)
                img1.draw();img2.draw();message.draw();win.flip()
                sound1 = sound.Sound("./img/sounds/reward_sound.wav")
                sound1.play()
                event.waitKeys(maxWait=3)
                sound1.stop()
                totalCoin += int(r)
                # displayText(win, "Earn your coin: " + str(r) + "!!\n\n Total Coin: " + str(totalCoin))
                displayText(win, "+" + str(r))
        # startTime = time.time()
        # event.waitKeys(maxWait=3)
        # Dict["ITI_duration"] = (time.time() - startTime) * 1000
        # ITI duration
        Dict["ITI_duration"] = random.uniform(1.5, 3.5) * 1000
        time.sleep(Dict["ITI_duration"] / 1000)

        Dict["Total_coins"] = totalCoin
        Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # displayText(win, "Your total coin is " + str(totalCoin))
    # event.waitKeys(maxWait=3)
    # if totalCoin > params['totalRewardThreshold']:
    #     img = visual.ImageStim(win=win, image="./img/happy_ending.jpg", units="pix", opacity=1,
    #                            size=params['screenSize'])
    #     img.draw();win.flip()
    #     event.waitKeys(maxWait=3)
    # else:
    #     displayText(win, "Please try again! Thank you!\n")
    #     event.waitKeys(maxWait=3)
    return Df

# Door Game Session Module.
def DoorGamePlay_keyboard(Df, win, params, iterNum, SectionName):

    message = visual.TextStim(win, text="[" + SectionName + "] Section is started.")
    waitUserInput(message, win, params)

    # Read Door Open Chance file provided by Rany.
    doorOpenChanceMap = np.squeeze((pd.read_csv('./input/doorOpenChance.csv',header=None)).values)
    imgList = glob.glob(params['imageDir'] + params['imageSuffix'])
    totalCoin = 0

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
        imgFile.split('/')[-1]
        p, r = re.findall(r'\d+', imgFile.split('/')[-1])
        Dict["Punishment_magnitude"] = p
        Dict["Reward_magnitude"] = r

        # Display the image.
        c = ['']
        level = Dict["Distance_start"] = params["DistanceStart"]
        width = params["screenSize"][0] * (1 - level / 110)
        height = params["screenSize"][1] * (1 - level / 110)
        img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
        img1.draw();win.flip();

        startTime = time.time()
        Dict["Distance_max"] = Dict["Distance_min"] = params["DistanceStart"]
        while (c[0] != "return"):

            # If waiting time is longer than 10 sec, exit this loop.
            Dict["DoorAction_RT"] = (time.time() - startTime) * 1000
            # print(Dict["DoorAction_RT"])
            if Dict["DoorAction_RT"] > params['DistanceLockWaitTime'] * 1000:
                c[0] = "timeisUp"
                break
            core.wait(1 / 60)
            c = event.waitKeys(maxWait=0.1)  # read a character
            if c == None:
                c = ['']
                continue

            if c[0] != "up" and c[0] != "down":
                continue

            if c[0] == "up" and level < 100:
                level += 1
            elif c[0] == "down" and level > 0:
                level -= 1
            Dict["Distance_max"] = max(Dict["Distance_max"], level)
            Dict["Distance_min"] = min(Dict["Distance_min"], level)

            width = params["screenSize"][0] * (1 - level / 110)
            height = params["screenSize"][1] * (1 - level / 110)
            img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
            img1.draw();win.flip()

        if c[0] == "return":
            Dict["Distance_lock"] = 1
        else:
            Dict["Distance_lock"] = 0
        Dict["DistanceFromDoor_SubTrial"] = level

        # Door Anticipation time
        Dict["Door_anticipation_time"] = random.uniform(2, 4) * 1000
        time.sleep(Dict["Door_anticipation_time"] / 1000)

        # if random.random() < level * 0.01:
        if random.random()  < doorOpenChanceMap[level]:
            Dict["Door_opened"] = "closed"
            img1 = visual.ImageStim(win=win, image="./img/door_100.jpg", units="pix", opacity=1)
            # img1.draw();win.flip();event.waitKeys(maxWait=3)
            # displayText(win, "Door Closed\n\n Total totalCoin: " + str(totalCoin))
            displayText(win, "Door Closed")
            # event.waitKeys(maxWait=3)
            # continue
        else:
            Dict["Door_opened"] = "opened"
            if random.random() < 0.5:
                Dict["Door_outcome"] = "punishment"
                awardImg = "./img/outcomes/" + p + "_punishment.jpg"
                width = 200 * (1 - level / 110)
                height = 400 * (1 - level / 110)
                img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -10],
                                        size=(width, height))
                message = visual.TextStim(win, text="-" + p, wrapWidth=2)
                message.pos = (0, 50)
                img1.draw();img2.draw();message.draw();win.flip()
                sound1 = sound.Sound("./img/sounds/punishment_sound.wav")
                sound1.play()
                event.waitKeys(maxWait=3)
                sound1.stop()
                totalCoin -= int(p)
                # displayText(win, "Lose your totalCoin: " + str(p) + "!!\n\n Total totalCoin: " + str(totalCoin))
                displayText(win, "-" + str(p))
            else:
                Dict["Door_outcome"] = "reward"
                awardImg = "./img/outcomes/" + r + "_reward.jpg"
                width = 200 * (1 - level / 110)
                height = 400 * (1 - level / 110)
                img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1, pos=[0, -10],
                                        size=(width, height))
                message = visual.TextStim(win, text="+" + r, wrapWidth=2)
                message.pos = (0, 50)
                img1.draw();img2.draw();message.draw();win.flip()
                sound1 = sound.Sound("./img/sounds/reward_sound.wav")
                sound1.play()
                event.waitKeys(maxWait=3)
                sound1.stop()
                totalCoin += int(r)
                # displayText(win, "Earn your coin: " + str(r) + "!!\n\n Total Coin: " + str(totalCoin))
                displayText(win, "+" + str(r))
        # startTime = time.time()
        # event.waitKeys(maxWait=3)
        # Dict["ITI_duration"] = (time.time() - startTime) * 1000
        # ITI duration
        Dict["ITI_duration"] = random.uniform(1.5, 3.5) * 1000
        time.sleep(Dict["ITI_duration"] / 1000)

        Dict["Total_coins"] = totalCoin
        Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

    # displayText(win, "Your total coin is " + str(totalCoin))
    # event.waitKeys(maxWait=3)
    # if totalCoin > params['totalRewardThreshold']:
    #     img = visual.ImageStim(win=win, image="./img/happy_ending.jpg", units="pix", opacity=1,
    #                            size=params['screenSize'])
    #     img.draw();win.flip()
    #     event.waitKeys(maxWait=3)
    # else:
    #     displayText(win, "Please try again! Thank you!\n")
    #     event.waitKeys(maxWait=3)
    return Df

def tableWrite(Df, Dict):
    # Move data in Dict into Df.
    Df = Df.append(pd.Series(dtype=float), ignore_index=True)  # Insert Empty Rows
    for key in Dict:
        Df[key].loc[len(Df) - 1] = Dict[key]  # FYI, len(Df)-1: means the last row of pandas dataframe.
    return Df


def displayVAS(win, text, labels):
    scale = visual.RatingScale(win,
                               labels=labels,  # End points
                               scale=None,  # Suppress default
                               low=0, high=100, tickHeight=0, markerStart=50, precision=1, size = 2,textSize = 0.6,
                               acceptText='Continue', showValue=False, showAccept=True)  # markerstart=50
    myItem = visual.TextStim(win, text=text, height=.12, units='norm', wrapWidth=2)

    # Show scale and measure the elapsed wall-clock time.
    startTime = time.time()
    while scale.noResponse:
        scale.draw()
        myItem.draw()
        win.flip()
    endTime = time.time()
    win.flip()
    return scale.getRating(), endTime - startTime

def displayInstruction(win):
    message = visual.TextStim(win, text="Do you want to see the instruction? (y: Yes, n: No)")
    message.draw();
    win.flip();
    c = ['']
    # Wait for user types "y" or "n".
    while (c[0].upper() != "Y" and c[0].upper() != "N"):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

    # If user types "y", run instruction.
    if c[0].upper() == "Y":
        c = ['R']
        while (c[0].upper() == "R"):
            core.wait(1 / 120)
            for i in range(1, 17):
                imgFile = "./instruction/Slide" + str(i) + ".JPG"
                img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(1200, 800))
                img1.draw();win.flip();
                c = event.waitKeys()

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
