# Python3-based package
"""
MIT License

Copyright (c) 2021 NIMH

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""
mainV1.py

Auditory Oddball Task Main Driver File (Version 1).

Created on Wed, Oct  6, 2021  3:39:42 PM

@author: Kyunghun Lee
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
from DictWrite import DictWriteRaw,DictWriteStart,DictWriteEnd
from StartMusic import playSound
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
    userInput = gui.Dlg(title="Auditory Oddball Task Information")
    userInput.addField('Subject ID:',)
    userInput.addField('Session:',)
    userInput.addField('Version:', choices=[1])
    userInput.addField('Timing File:', choices=[0,1,2,3,4,5])
    userInput.addField('Serial Port support', choices=[True,False])
    UserInputBank = userInput.show()

    params = {
        'expName': 'Auditory Oddball Task',  # The name of the experiment
        'subjectID': UserInputBank[0],  # Subject ID
        'Session': UserInputBank[1],  # Session ID
        'Version': UserInputBank[2],  # Version
        'TimingFile': UserInputBank[3], # Timing File
        'SerialPortSupport': UserInputBank[4], # Serial Port Support7
    }
    return params
params = userInputPlay()
mixer.init()

# Serial Port Initialization
if params['SerialPortSupport']:
    import serial
    userInput = gui.Dlg(title="Serial Port Configuration")
    userInput.addField('Port:', "COM4", choices=['COM1','COM2','COM3','COM4'])
    userInput.addField('baudrate',19200)
    userInput.addField('timeout', 0.01)
    userInput.addField('bytesize',8)
    UserInputBank = userInput.show()

    params['port'] = UserInputBank[0]
    params['baudrate'] = UserInputBank[1]
    params['timeout'] = UserInputBank[2]
    params['bytesize'] = UserInputBank[3]

    # serialPort = serial.Serial(port="COM3", baudrate=9600,
    #                            bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    serialPort = serial.Serial(port=params['port'], baudrate=params['baudrate'],
                               bytesize=params['bytesize'], timeout=params['timeout'], stopbits=serial.STOPBITS_ONE)

# Read timing File
df = pd.read_csv('timing/' + str(params['TimingFile'])+ '.csv')

# Decide the name of output files.
timeLabel = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
params['outFile'] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
              timeLabel + ".csv"
params['outFileRaw'] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
              timeLabel + "_raw.csv"


# Dictionary Intialization
dict = {}
Raw = {}

def waitTime(startTime, duration):
    # while time.time() - startTime < duration:
    #     keys = event.getKeys()
    #     if keys == ['q'] or keys == ['Q']:
    #         print('Q pressed. Forced Exit.')
    #         core.quit()
    #     core.wait(1 / 120)
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
