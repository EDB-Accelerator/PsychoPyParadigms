"""
Flanker Psychopy Game (Conversion from E-prime)
Base: Python3, Psychopy3

- Created Wed Mar 16 08:58:05 EDT 2022 by Kyunghun Lee
"""

# Import standard python libraries
from psychopy import visual,core, event,gui
import numpy as np
import os, glob,datetime
import pandas as pd
import glob,sys
import random
import time
sys.path.insert(1, './src')
# from DictWrite import DictWriteRaw,DictWriteStart,DictWriteEnd
from DictInitialize import DictInitialize
from InstructionPlay import InstructionPlay
from Helper import WaitSeconds
from FlankerPlay import FlankerPlay
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
    userInput.addField('The number of Trials',45,choices=[45,5,1])
    UserInputBank = userInput.show()

    params = {
        'expName': 'FlankerTask',  # The name of the experiment
        'Version': UserInputBank[0],  # Version
        'subjectID': UserInputBank[1],  # Subject ID
        'Session': UserInputBank[2],  # Session ID
        'nTrials': UserInputBank[3],  # Session ID
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

# Timing File load
# timingFiles = glob.glob('timing/*.csv')
# random.shuffle(timingFiles)
# timingFile = timingFiles[0]
timingFile = "timing/iti.csv"

# Load a Timing File.
dfTiming = pd.read_csv(timingFile,header=None,names=['ITI'])
ITIs = np.array(dfTiming['ITI'])

# Instruction +Presentation
win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
df = InstructionPlay(df,win,params)

# Waiting for scanner (press 5).
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

# Get Ready screen.
message = visual.TextStim(win, text="Get Ready",
                          units='norm', wrapWidth=1000, color="white")
message.draw()
win.flip()
WaitSeconds(8)

# Show the flanker image.
orderMat = [0,1,2,3]*9
random.shuffle(orderMat)
random.shuffle(ITIs)

for i in range(params['nTrials']):
    n = orderMat[i]
    if n == 0:
        FlankerPlay(df,ITIs[i],dict,dictRaw,"CL",win,params)
    elif n == 1:
        FlankerPlay(df,ITIs[i],dict,dictRaw,"CR",win,params)
    elif n == 2:
        FlankerPlay(df,ITIs[i],dict,dictRaw,"IR",win,params)
    elif n == 3:
        FlankerPlay(df,ITIs[i],dict,dictRaw,"IL",win,params)

# imgCONGL = 'img/CONGL.jpg'
#
# messageCONGL= visual.TextStim(win, text="<<<<<",units='norm', wrapWidth=1000, color="white",height=0.3)
# messageCONGR= visual.TextStim(win, text=">>>>>",units='norm', wrapWidth=1000, color="white",height=0.3)
# messageINCONGR= visual.TextStim(win, text="<<><<",units='norm', wrapWidth=1000, color="white",height=0.3)
# messageINCONGL= visu*al.TextStim(win, text=">><>>",units='norm', wrapWidth=1000, color="white",height=0.3)
#
# messageCONGL.draw()
# win.flip()
#
# # Response Window
# # Get user input.
# c = []
# startTime = time.time()
# dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
# event.clearEvents()
# while time.time() - startTime < 1.7:
#     core.wait(1 / 120)
#     if c == []:
#         c = event.getKeys()
#     if len(c) >= 1:
#         dictRaw["Event"] = "User Response:" + c[0]
#         # DictWriteRaw(dfRaw, dictRaw, params)
# if c == ['q'] or c == ['Q']:
#     print('Q pressed. Forced Exit.')
#     core.quit()
# if len(c) >= 1:
#     c = c[0]
# else:
#     c = "No Response"










