import glob
import re
import random
import pandas as pd
from psychopy import core, visual, event, sound
from Helper import fadeInOutImage, displayText, showImage, overlapImage, displayVAS

# Declare primary task parameters.
params = {
# Declare stimulus and response parameters
    'expName' : "Doors_AA_v7", # The name of the experiment
    'nTrials': 15,            # number of trials in this session
    'subjectID' : 23986,      # Subject ID
    'stimDur': 1,             # time when stimulus is presented (in seconds)
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
    'fullScreen': True,       # run in full screen mode?
    'screenToShow': 0,        # display on primary screen (0) or secondary (1)?
    'fixCrossSize': 0.1,       # size of cross, in height units
    'fixCrossPos': [0,0],     # (x,y) pos of fixation cross displayed before each stimulus (for gaze drift correction)
    'screenColor':(128,128,128) # in rgb255 space: (r,g,b) all between 0 and 255
}

## Setup Section.
win = visual.Window([1200, 800], monitor="testMonitor")

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
          "DoorAction_RT","ITI_duration","Total_coins","VAS_type","VAS_score","VAS_RT","Q_type","Q_score","Q_RT"]

Df = pd.DataFrame(columns=Header)
Dict = {}
Dict["ExperimentName"] = 1234;Dict["Subject"] = "Jimmy"

def tableWrite(Df,Dict):
    # Move data in Dict into Df.
    Df = Df.append(pd.Series(dtype=float), ignore_index=True) #Insert Empty Rows
    for key in Dict:
        Df[key].loc[len(Df)-1] = Dict[key] # FYI, len(Df)-1: means the last row of pandas dataframe.
    return Df,Dict

# ====================== #
# ======== VAS ========= #
# ====================== #
# Common Dictionary initialization (common entries for all data)
Dict = {}
Dict["ExperimentName"] = params['expName']
Dict["Subject"] = params['subjectID']

# VAS (Anxiety)
Dict["VAS_type"] = "Anxiety"
Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(win,"How anxious do you feel right now?",['Not anxious', 'Very anxious'])
Df,Dict = tableWrite(Df,Dict) # Log the dict result on pandas dataFrame.

# VAS (Avoidance)
Dict["VAS_type"] = "Avoidance"
Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(win,"How much do you feel like taking part in the task?",
                                               ['Not at all', 'Very much'])
Df,Dict = tableWrite(Df,Dict) # Log the dict result on pandas dataFrame.

# VAS (Tired)
Dict["VAS_type"] = "Tired"
Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(win,"How tired are you right now?",['Not at all tired', 'Very tired'])
Df,Dict = tableWrite(Df,Dict) # Log the dict result on pandas dataFrame.

# VAS (Mood)
Dict["VAS_type"] = "Mood"
Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(win,"Think about your mood right now. How would you describe it?",
                       ['Worst mood ever', 'Best mood ever'])
Df,Dict = tableWrite(Df,Dict) # Log the dict result on pandas dataFrame.

# ====================== #
# ===== Instruction ==== #
# ====================== #
message = visual.TextStim(win, text="Do you want to see the instruction? (y: Yes, n: No)")
message.draw();win.flip();

# displayText(win, "Do you want to see the instruction? \n\n(y: Yes, n: No)",wrapWidth=2)
c = ['']
# Wait for user types "y" or "n".
while(c[0].upper() != "Y" and c[0].upper() != "N"):
    core.wait(1 / 120)
    c = event.waitKeys()  # read a character

# If user types "y", run instruction.
if c[0].upper() == "Y":
    c = ['R']
    while(c[0].upper() == "R"):
        core.wait(1 / 120)
        for i in range(1,17):
            imgFile = "./instruction/Slide" + str(i) + ".JPG"
            img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(1200, 800))
            img1.draw();win.flip();
            c = event.waitKeys()

# ====================== #
# ===== Instruction ==== #
# ====================== #
# Get the image file list.
score = 0
imgList = glob.glob("./img/doors/*.jpg")
iterNum = params['nTrials']
for i in range(iterNum):
    # Pick up random image.
    randN = random.randint(0,len(imgList)-1)
    imgFile = imgList[randN]
    imgFile.split('/')[-1]
    p,r = re.findall(r'\d+', imgFile.split('/')[-1])

    # Display the image.
    c = ['']
    level = 5
    width = pow(1.1, level) * 400
    height = pow(1.1, level) * 225
    img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width,height))
    img1.draw();win.flip();event.waitKeys()

    while(c[0]!="return"):
        core.wait(1 / 60)
        c = event.waitKeys()  # read a character
        if c[0] == "up" and level < 9:
            level += 1
        elif c[0] == "down" and level > 0:
            level -= 1

        width = pow(1.1,level) * 400
        height = pow(1.1,level) * 225
        img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
        img1.draw();win.flip()

    if random.random() > 0.1 * level:
        img1 = visual.ImageStim(win=win, image="./img/door_100.jpg", units="pix", opacity=1)
        img1.draw();win.flip();event.waitKeys()
        displayText(win, "Door Closed\n\n Total Score: " + str(score))
        event.waitKeys()
        continue
    else:
        # showImage(win, "./img/door_25.jpg", 1, None)
        # event.waitKeys()

        if random.random() < 0.5:
            awardImg = "./img/outcomes/" + p + "_punishment.jpg"
            width = 100*pow(1.1,level-5)
            height = 190*pow(1.1,level-5)
            img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1,pos=[0,-10],size=(width,height))
            message = visual.TextStim(win, text="-"+p, wrapWidth=2)
            message.pos = (0,50)
            img1.draw();img2.draw();message.draw();win.flip()
            sound1 = sound.Sound("./img/sounds/punishment_sound.wav")
            sound1.play()
            event.waitKeys()
            sound1.stop()
            score -= int(p)
            displayText(win, "Lose your score: " + str(p) + "!!\n\n Total Score: " + str(score))
            event.waitKeys()
        else:
            awardImg = "./img/outcomes/" + r + "_reward.jpg"
            width = 100*pow(1.1,level-5)
            height = 190*pow(1.1,level-5)
            img2 = visual.ImageStim(win=win, image=awardImg, units="pix", opacity=1,pos=[0,-10],size=(width,height))
            message = visual.TextStim(win, text="+"+r, wrapWidth=2)
            message.pos = (0,50)
            img1.draw();img2.draw();message.draw();win.flip()
            sound1 = sound.Sound("./img/sounds/reward_sound.wav")
            sound1.play()
            event.waitKeys()
            sound1.stop()
            score += int(r)
            displayText(win, "Earn your score: " + str(r) + "!!\n\n Total Score: " + str(score))
            event.waitKeys()

displayText(win, "Your total score is " + str(score))
event.waitKeys()
if score > 10:
    showImage(win, "./img/happy_ending.jpg", 1, (1200,800))
    event.waitKeys()
else:
    displayText(win, "Please try again! Thank you!\n")
    event.waitKeys()

f = open(params['outFile'], "w")
f.write(Header + "\n")
f.close()
win.close()
