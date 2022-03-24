"""
Flanker Psychopy Game (Conversion from E-prime)
Base: Python3, Psychopy3

- Created Wed Mar 16 08:58:05 EDT 2022 by Kyunghun Lee
"""

# Import standard python libraries
from psychopy import visual, prefs, core, event, sound,gui
from pygame import mixer
import os, glob,datetime
import pandas as pd
import pickle
import subprocess
import time,sys
import random
sys.path.insert(1, './src')
# from DictWrite import DictWriteRaw,DictWriteStart,DictWriteEnd
from DictInitialize import DictInitialize
from InstructionPlay import InstructionPlay
# from StartMusic import playSound
import serial

# Make empty output directory if it does not exist.
directory = './result'
if not os.path.exists(directory):
    os.makedirs(directory)

# Pandas configuration (debugging options)
pd.set_option('display.max_columns', None)

# Output Summary Header Initialization
Header = ["Start Time", "End Time", "Duration", "expName", "Version", "subjectID", 'timingFile',"Session", "Event",
          "Sound Type"]

# Output Raw Header Initialization
HeaderRaw = ["TimeStamp", "expName", "Version", "subjectID", "Session", "Event"]

# Function to get user inputs.
def userInputPlay():
    userInput = gui.Dlg(title="Flanker Task Information")
    userInput.addField('Version:', choices=[1])
    userInput.addField('Subject ID (SDAN):',)
    userInput.addField('Session:',)
    UserInputBank = userInput.show()

    params = {
        'expName': 'FlankerTask',  # The name of the experiment
        'Version': UserInputBank[0],  # Version
        'subjectID': UserInputBank[1],  # Subject ID
        'Session': UserInputBank[2],  # Session ID
        'screenSize': [1024, 768], # Screen Resolution
    }
    return params
params = userInputPlay()

# Decide the name of output files.
timeLabel = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
params['outFile'] = ''.join(["./result/",params["expName"],"_",str(params["subjectID"]),"_",str(params["Session"]),
                            timeLabel,".csv"])
params['outFileRaw'] = ''.join(["./result/",params["expName"],"_",str(params["subjectID"]),"_",str(params["Session"]),
                            timeLabel,"_raw.csv"])

# Dictionary and dataframe Initialization
Header = ["Start Time","End Time","Duration","expName","Version","subjectID","Session","Section","TrialCount",
          "Image Displayed","User Response"]
HeaderRaw = ["TimeStamp","expName","Version","subjectID","Session","Event"]
dict,dictRaw = DictInitialize(params)
df,dfRaw = pd.DataFrame(columns=Header),pd.DataFrame(columns=HeaderRaw)

# Instruction +Presentation
win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
df = InstructionPlay(df,win,params)

# Waiting for scanner screen.
message = visual.TextStim(win, text="Waiting for scanner \n\n(Please press 5 when it is ready.)",
                          units='norm', wrapWidth=1000, color="white")
message.draw()
win.flip()
userInput = ['']
# Wait for user types "y" or "n".
while (userInput[0].upper() != "5"):
    core.wait(1 / 120)
    userInput = event.waitKeys()  # read a characters
    # print(userInput)
    if userInput == ['q'] or userInput == ['Q']:
        print('Q pressed. Forced Exit.')
        core.quit()

# Show the flanker image.
img = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1, size=(width, height))
img1.draw();win.flip();










