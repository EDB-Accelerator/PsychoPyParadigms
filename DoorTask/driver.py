import glob
import re
import random
import pandas as pd
from psychopy import core, visual, event, sound
from psychopy.hardware import joystick
from Helper import fadeInOutImage, displayText, showImage, overlapImage, displayVAS, displayInstruction,tableWrite
import datetime

# Declare primary task parameters.
params = {
# Declare stimulus and response parameters
    'expName' : "Doors_AA_v7", # The name of the experiment
    'nTrials': 5,            # number of trials in this session
    'subjectID' : 23986,      # Subject ID
    'DistanceStart' : 50,
    'winSize': 1,             # time when stimulus is presented (in seconds)
    'ISI': 2,                 # time between when one stimulus disappears and the next appears (in seconds)
    'tStartup': 2,            # pause time before starting first stimulus
    'triggerKey': 't',        # key from scanner that says scan is starting
    'respKeys': ['r','b','y','g'],           # keys to be used for responses (mapped to 1,2,3,4)
    'respAdvances': True,     # will a response end the stimulus?
    'imageDir': 'Faces/',    # directory containing image stimluli
    'imageSuffix': '.jpg',   # images will be selected randomly (without replacement) from all files in imageDir that end in imageSuffix.
# declare output file location
    'outFile': './output.csv', # the location of output file.
# declare display parameters
#     'fullScreen': True,       # run in full screen mode?
    'screenSize' : [1200,800],
    'screenToShow': 0,        # display on primary screen (0) or secondary (1)?
    'fixCrossSize': 0.1,       # size of cross, in height units
    'fixCrossPos': [0,0],     # (x,y) pos of fixation cross displayed before each stimulus (for gaze drift correction)
    'screenColor':(128,128,128) # in rgb255 space: (r,g,b) all between 0 and 255
}

## Setup Section.
win = visual.Window(params['screenSize'], monitor="testMonitor")

# Display NIMH logo.
fadeInOutImage(win,"./img/nimh.png",0.5,(600,600))

# ====================== #
# ==== Title Screen ==== #
# ====================== #
img1 = visual.ImageStim(win=win,image="./img/title.jpg",units="pix",size=(1200,800),opacity=1) #
img1.draw();win.flip();event.waitKeys()

# ======================== #
# Dataframe Initialization #
# ======================== #
Header = ["ExperimentName","SessionStartDateTime","Subject","Session","Version","Section","Subtrial",
          "DistanceFromDoor_SubTrial","Distance_lock","Distance_start","Distance_min","Distance_max",
          "Door_anticipation_time","Door_opened","Door_outcome","Reward_magnitude","Punishment_magnitude",
          "DoorAction_RT","ITI_duration","Total_coins","VAS_type","VAS_totalCoin","VAS_RT","Q_type","Q_totalCoin","Q_RT"]

Df = pd.DataFrame(columns=Header)
Dict = {}
Dict["ExperimentName"] = 1234;Dict["Subject"] = "Jimmy"

# ====================== #
# ======== VAS ========= #
# ====================== #
# Common Dictionary initialization (common entries for all VAS)
Dict = {}
Dict["ExperimentName"] = params['expName']
Dict["Subject"] = params['subjectID']
Dict["Session"] = 1
Dict["Version"] = 1
Dict["Section"] = "VAS1"

# VAS (Anxiety)
Dict["VAS_type"] = "Anxiety"
Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
Dict["VAS_totalCoin"], Dict["VAS_RT"] = displayVAS(win,"How anxious do you feel right now?",['Not anxious', 'Very anxious'])
Df = tableWrite(Df,Dict) # Log the dict result on pandas dataFrame.

# VAS (Avoidance)
Dict["VAS_type"] = "Avoidance"
Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
Dict["VAS_totalCoin"], Dict["VAS_RT"] = displayVAS(win,"How much do you feel like taking part in the task?",
                                               ['Not at all', 'Very much'])
Df = tableWrite(Df,Dict) # Log the dict result on pandas dataFrame.

# VAS (Tired)
Dict["VAS_type"] = "Tired"
Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
Dict["VAS_totalCoin"], Dict["VAS_RT"] = displayVAS(win,"How tired are you right now?",['Not at all tired', 'Very tired'])
Df = tableWrite(Df,Dict) # Log the dict result on pandas dataFrame.

# VAS (Mood)
Dict["VAS_type"] = "Mood"
Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
Dict["VAS_totalCoin"], Dict["VAS_RT"] = displayVAS(win,"Think about your mood right now. How would you describe it?",
                       ['Worst mood ever', 'Best mood ever'])
Df = tableWrite(Df,Dict) # Log the dict result on pandas dataFrame.

# ====================== #
# ===== Instruction ==== #
# ====================== #
Dict = {};
Dict["ExperimentName"] = params['expName']
Dict["Subject"] = params['subjectID']
Dict["Session"] = 1
Dict["Version"] = 1
Dict["Section"] = "Instructions"
Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
displayInstruction(win)
Df = tableWrite(Df,Dict) # Log the dict result on pandas dataFrame.

# ====================== #
# ===== Practice ======= #
# ====================== #


# Get the DOOR image file list.
totalCoin = 0
imgList = glob.glob("./img/doors/*.jpg")
iterNum = params['nTrials']
for i in range(iterNum):
    Dict = {};
    Dict["ExperimentName"] = params['expName']
    Dict["Subject"] = params['subjectID']
    Dict["Session"] = 1
    Dict["Version"] = 1
    Dict["Section"] = "Practice"
    Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    # Pick up random image.
    randN = random.randint(0,len(imgList)-1)
    imgFile = imgList[randN]
    imgFile.split('/')[-1]
    p,r = re.findall(r'\d+', imgFile.split('/')[-1])
    Dict["Punishment_magnitude"] = p
    Dict["Reward_magnitude"] = r

    # Display the image.
    c = ['']
    level = Dict["Distance_start"] = params["DistanceStart"]
    width = params["screenSize"][0] * (1 - level/110)
    height = params["screenSize"][1] * (1 - level/110)
    img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width,height))
    img1.draw();win.flip();event.waitKeys()

    while(c[0]!="return"):
        core.wait(1 / 60)
        c = event.waitKeys()  # read a character
        if c[0] == "up" and level < 100:
            level += 1
        elif c[0] == "down" and level > 0:
            level -= 1

        width = params["screenSize"][0] * (1 - level / 110)
        height = params["screenSize"][1] * (1 - level / 110)
        img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
        img1.draw();win.flip()
    Dict["DistanceFromDoor_SubTrial"] = level

    if random.random() < level * 0.01:
        Dict["Door_opened"] = "closed"
        img1 = visual.ImageStim(win=win, image="./img/door_100.jpg", units="pix", opacity=1)
        img1.draw();win.flip();event.waitKeys()
        displayText(win, "Door Closed\n\n Total totalCoin: " + str(totalCoin))
        event.waitKeys()
        continue
    else:
        Dict["Door_opened"] = "opened"
        if random.random() < 0.5:
            Dict["Door_outcome"] = "punishment"
            awardImg = "./img/outcomes/" + p + "_punishment.jpg"
            width = 200 * (1 - level / 110)
            height = 400 * (1 - level / 110)
            img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1,pos=[0,-10],size=(width,height))
            message = visual.TextStim(win, text="-"+p, wrapWidth=2)
            message.pos = (0,50)
            img1.draw();img2.draw();message.draw();win.flip()
            sound1 = sound.Sound("./img/sounds/punishment_sound.wav")
            sound1.play()
            event.waitKeys()
            sound1.stop()
            totalCoin -= int(p)
            displayText(win, "Lose your totalCoin: " + str(p) + "!!\n\n Total totalCoin: " + str(totalCoin))
            event.waitKeys()
        else:
            Dict["Door_outcome"] = "reward"
            awardImg = "./img/outcomes/" + r + "_reward.jpg"
            width = 200 * (1 - level / 110)
            height = 400 * (1 - level / 110)
            img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1,pos=[0,-10],size=(width,height))
            message = visual.TextStim(win, text="+"+r, wrapWidth=2)
            message.pos = (0,50)
            img1.draw();img2.draw();message.draw();win.flip()
            sound1 = sound.Sound("./img/sounds/reward_sound.wav")
            sound1.play()
            event.waitKeys()
            sound1.stop()
            totalCoin += int(r)
            displayText(win, "Earn your coin: " + str(r) + "!!\n\n Total Coin: " + str(totalCoin))
            Dict["Total_coins"] = totalCoin
            event.waitKeys()
    Df = tableWrite(Df, Dict)  # Log the dict result on pandas dataFrame.

displayText(win, "Your total coin is " + str(totalCoin))
event.waitKeys()
if totalCoin > 10:
    showImage(win, "./img/happy_ending.jpg", 1, (1200,800))
    event.waitKeys()
else:
    displayText(win, "Please try again! Thank you!\n")
    event.waitKeys()

# Write the output file.
f = open(params['outFile'], "w")
f.write(Header + "\n")
f.close()
win.close()
