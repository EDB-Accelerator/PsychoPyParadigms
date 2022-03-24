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

def waitTime(startTime, duration):
    elapsedTime = time.time() - startTime
    core.wait(duration - elapsedTime)

novelSoundFiles = glob.glob('sound/*.WAV')
novelSoundFiles = [x for x in novelSoundFiles if 'PN650HZ' not in x and 'PO500HZ' not in x]
random.shuffle(novelSoundFiles)

startTime = time.time()
DictWriteRaw(params,event="task started")


win = visual.Window([1024,768], monitor="testMonitor", color="white", winType='pyglet')
message = visual.TextStim(win,text="Press 5 to continue\n ",
                                  units='norm', wrapWidth=2, color="black")
message.draw()
win.flip()
DictWriteRaw(params,event="Message: Press 5 to continue")

c = ''
while (c != ['5']):
    core.wait(1 / 120)
    c = event.getKeys()
DictWriteRaw(params,event="5 pressed")

if params['SerialPortSupport']:
    serialPort.write("5")
    serialPort.write(5)
    print("serial port write: 5")

for i in range(len(df)):
    duration = df.loc[i]['Duration']
    stimuli = df.loc[i]['Stimuli']
    if 'No sound' in stimuli:
        DictWriteRaw(params, event="No sound (start)")
        DictWriteStart(params)
        waitTime(time.time(),20)
        DictWriteRaw(params, event="No sound (end)")
        DictWriteEnd(params, "No sound")
        continue
    elif 'interval' in stimuli:
        DictWriteRaw(params, event="Interval (start)")
        DictWriteStart(params)
        waitTime(startTime,duration+0.2)
        DictWriteRaw(params, event="Interval (end)")
        DictWriteEnd(params, "Interval")
        continue

    if 'Standard' in stimuli:
        soundFile = 'sound/PO500HZ.WAV'
    elif 'Deviant' in stimuli:
        soundFile = 'sound/PN650HZ.WAV'
    elif 'Novel' in stimuli:
        soundFile = novelSoundFiles.pop()
    startTime = time.time()
    # sound1 = sound.Sound(soundFile)
    DictWriteRaw(params, event="Sound played (start):" + soundFile)
    DictWriteStart(params)
    playSound(mixer, soundFile)
    # sound1.play()
    DictWriteRaw(params, event="Sound played (end):" + soundFile)
    DictWriteEnd(params, "Sound played:" + soundFile)
