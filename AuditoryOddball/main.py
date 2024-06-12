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
Updated on Wed, Mar 23, 2022  9:58:32 AM: Serial Port Support
Updated on Fri, Apr  8, 2022  3:03:17 PM: Optimization (speed)

@author: Kyunghun Lee
"""

# Import standard python libraries
from psychopy import visual, prefs, core, event, sound, gui
from pygame import mixer
import os, glob, datetime
import pandas as pd
import pickle
import subprocess
import time, sys
import random

sys.path.insert(1, './src')
from DictWrite import DictWriteStart, DictWriteEnd
from StartMusic import playSound
import serial

# Make empty output directory if it does not exist.
directory = './result'
if not os.path.exists(directory):
    os.makedirs(directory)

# Pandas configuration (debugging options)
pd.set_option('display.max_columns', None)

# Output Summary Header Initialization
Header = ["Start Time", "End Time", "Duration", "Accumulated Time", "expName", "Version", "subjectID", 'timingFile',
          "Session", "Event",
          "Sound Type"]

# Output Raw Header Initialization
HeaderRaw = ["TimeStamp", "expName", "Version", "subjectID", "Session", "Event"]


# Function to get the Subject ID with validation
def getSubjectID():
    userInput = gui.Dlg(title="Enter Subject ID")
    userInput.addField('Subject ID:', )
    UserInputBank = userInput.show()  # Show input dialog
    subjectID = UserInputBank[0]
    if not subjectID.isalnum():
        gui.Dlg(title="Error", labelButtonOk='Ok', labelButtonCancel='Cancel').inform(
            'Error: Subject ID should only contain alphanumeric characters. Exiting...')
        core.quit()  # Quit if validation fails
    return subjectID


subjectID = getSubjectID()  # Call the function to get validated Subject ID

# Check for existing CSV files in the folder
save_directory = f'.save/{subjectID}/'
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
csv_files = glob.glob(f'{save_directory}*.csv')


def userInputSession(subjectID, csv_files):
    filesList = [f'Session from file: {os.path.basename(file)}' for file in csv_files if
                 os.path.basename(file).endswith('.csv')]
    filesList.reverse()
    session_choices = filesList + ['Create a new session']
    userInput = gui.Dlg(title="Auditory Oddball Task Session Information")
    userInput.addText(f'Subject ID: {subjectID}')  # Display Subject ID as non-editable text
    userInput.addField('Choose Session:', choices=session_choices)
    userInput.addField('Version:', choices=[1])
    userInput.addField('Timing File:', choices=[0, 1, 2, 3, 4, 5, 6])
    userInput.addField('Serial Port support', choices=[True, False])

    return userInput.show()


UserInputBank = userInputSession(subjectID, csv_files)  # Get user inputs with session options
print(UserInputBank)

# Random Seed
import random
# Determine the session number and create a new CSV file if 'Create a new session' is chosen
import re


def handleSessionChoice(subjectID, userInputBank, csv_files):
    session_choice = userInputBank[0]  # User's session choice
    print(f"session_choice:{session_choice}")
    if session_choice == 'Create a new session':
        # As before, create a new session
        session_number = len(csv_files) + 1
        random_seed = random.randint(1, 10000)
        time_stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        session_file_name = f'{session_number}_{time_stamp}.csv'
        session_file_path = f'.save/{subjectID}/{session_file_name}'
        df = pd.DataFrame({'Random Seed': [random_seed]})
        df.to_csv(session_file_path, index=False)
        return random_seed, session_file_path, str(session_number)
    else:
        # Extract session info from the chosen existing file
        pattern = r"(\d+)_(\d{8}_\d{6})\.csv"
        match = re.search(pattern, session_choice)
        if match:
            session_number, time_stamp = match.groups()
            session_file_name = f"{session_number}_{time_stamp}.csv"
            session_file_path = f'.save/{subjectID}/{session_file_name}'

            # Read the CSV to get the random seed
            df = pd.read_csv(session_file_path)
            random_seed = df['Random Seed'].iloc[0] if 'Random Seed' in df.columns else random.randint(1, 10000)

            return random_seed, session_file_path, str(session_number)
        else:
            raise ValueError("Invalid session file format")


random_seed, session_file_path, SessionNumber = handleSessionChoice(subjectID, UserInputBank, csv_files)

params = {
    'expName': 'Auditory Oddball Task',  # The name of the experiment
    'subjectID': subjectID,  # Subject ID
    'Session': SessionNumber,  # Session ID
    'Version': UserInputBank[1],  # Version
    'TimingFile': UserInputBank[2],  # Timing File
    'SerialPortSupport': UserInputBank[3],  # Serial Port Support7
}
print(params)

# Initialize Sound Mixer.
mixer.init()

# Serial Port Initialization
# Serial Port Initialization
if params['SerialPortSupport']:
    import serial

    userInput = gui.Dlg(title="Serial Port Configuration")
    userInput.addField('Port:', "LPT1", choices=['COM1', 'COM2', 'COM3', 'COM4', 'LPT1', 'None'])
    userInput.addField('baudrate', 19200)
    userInput.addField('timeout', 0.01)
    userInput.addField('bytesize', 8)
    UserInputBank = userInput.show()

    params['port'] = UserInputBank[0]
    params['baudrate'] = UserInputBank[1]
    params['timeout'] = UserInputBank[2]
    params['bytesize'] = UserInputBank[3]
    # Serial port testing
    if params['port'] in ['COM1', 'COM2', 'COM3', 'COM4']:
        serialPort = serial.Serial(port=params['port'], baudrate=params['baudrate'], bytesize=params['bytesize'],
                                   timeout=params['timeout'], stopbits=serial.STOPBITS_ONE)
    elif params['port'] == 'LPT1':
        from psychopy import parallel

        serialPort = parallel.ParallelPort(address=0x378)
    else:
        serialPort = None
    #                            bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    # serialPort.write("2")

    # serialPort = serial.Serial(port=params['port'], baudrate=params['baudrate'],
    #                            bytesize=params['bytesize'], timeout=params['timeout'], stopbits=serial.STOPBITS_ONE)

# Read timing File
dfTiming = pd.read_csv('timing/' + str(params['TimingFile']) + '.csv')

# Decide the name of output files.
timeLabel = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")


# params['outFile'] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
#               "_" + params['TimingFile'] + "_" + timeLabel + ".csv"
#
# params['outFileRaw'] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
#               "_" + params['TimingFile'] + "_" + timeLabel + "_raw.csv"
def generate_filename(base_path, exp_name, subject_id, session, timing_file, time_label, suffix=''):
    filename = f"{exp_name}_{subject_id}_{session}_{timing_file}_{time_label}{suffix}.csv"
    return os.path.join(base_path, filename)


params['outFile'] = generate_filename('./result', params['expName'], params['subjectID'], params['Session'],
                                      params['TimingFile'], timeLabel)
params['outFileRaw'] = generate_filename('./result', params['expName'], params['subjectID'], params['Session'],
                                         params['TimingFile'], timeLabel, '_raw')

# Dictionary Intialization
dict = {}
Raw = {}
df = pd.DataFrame(columns=Header)
dfRaw = pd.DataFrame(columns=HeaderRaw)


def waitTime(startTime, duration):
    # while time.time() - startTime < duration:
    #     keys = event.getKeys()
    #     if keys == ['q'] or keys == ['Q']:
    #         print('Q pressed. Forced Exit.')
    #         core.quit()
    #     core.wait(1 / 120)
    elapsedTime = time.time() - startTime
    core.wait(duration - elapsedTime)
    # time.sleep(duration - elapsedTime)


novelSoundFiles = glob.glob('sound/*.WAV')
novelSoundFiles = [x for x in novelSoundFiles if 'PN650HZ' not in x and 'PO500HZ' not in x]
random.seed(random_seed)
random.shuffle(novelSoundFiles)
novelSoundFiles = novelSoundFiles[params['TimingFile'] * 14:params['TimingFile'] * 14 + 14]
print(f"used index: {params['TimingFile'] * 14} to {params['TimingFile'] * 14 + 14}")

startTime = time.time()
# dfRaw = DictWriteRaw(dfRaw,params,event="task started")
print("task started")

win = visual.Window([1024, 768], monitor="testMonitor", color="white", winType='pyglet')
message = visual.TextStim(win, text="Press 5 to continue\n ",
                          units='norm', wrapWidth=2, color="black")
message.draw()
win.flip()
# dfRaw = DictWriteRaw(dfRaw,params,event="Message: Press 5 to continue")
print("Message: Press 5 to continue")

c = ''
while (c != ['5']):
    core.wait(1 / 120)
    c = event.getKeys()
# dfRaw = DictWriteRaw(dfRaw,params,event="5 pressed")
print("5 pressed")

params['gameStartTime'] = datetime.datetime.now()

if params['SerialPortSupport']:
    # dfRaw = DictWriteRaw(dfRaw,params, event="Serial Port Sent message (start)")
    DictWriteStart(params)
    if params['port'] in ['COM1', 'COM2', 'COM3', 'COM4']:
        serialPort.write(5)
    elif params['port'] == 'LPT1':
        serialPort.setData(0x5)

    df = DictWriteEnd(df, params, "Serial Port Sent message")

for i in range(len(dfTiming)):
    duration = dfTiming.loc[i]['Duration']
    stimuli = dfTiming.loc[i]['Stimuli']
    if 'No sound' in stimuli:
        # dfRaw = DictWriteRaw(dfRaw,params, event="No sound (start)")
        print("No sound (start)")
        DictWriteStart(params)
        waitTime(time.time(), 20)
        # dfRaw = DictWriteRaw(dfRaw,params, event="No sound (end)")
        print("No sound (end)")
        df = DictWriteEnd(df, params, "No sound")
        continue
    elif 'interval' in stimuli:
        # dfRaw = DictWriteRaw(dfRaw,params, event="Interval (start)")
        print("Interval (start)")
        DictWriteStart(params)
        # waitTime(time.time(),duration+0.2)
        waitTime(time.time(), duration)
        # dfRaw = DictWriteRaw(dfRaw,params, event="Interval (end)")
        print("Interval (end)")
        df = DictWriteEnd(df, params, "Interval")
        continue
    else:
        if 'Standard' in stimuli:
            soundFile = 'sound/PO500HZ.WAV'
        elif 'Deviant' in stimuli:
            soundFile = 'sound/PN650HZ.WAV'
        elif 'Novel' in stimuli:
            soundFile = novelSoundFiles.pop()
        # startTime = time.time()
        # sound1 = sound.Sound(soundFile)
        # dfRaw = DictWriteRaw(dfRaw,params, event="Sound played (start):" + soundFile)
        print("Sound played (start):" + soundFile)
        DictWriteStart(params)
        playSound(mixer, soundFile, duration)
        # sound1.play()
        # dfRaw = DictWriteRaw(dfRaw,params, event="Sound played (end):" + soundFile)
        print("Sound played (end):" + soundFile)
        df = DictWriteEnd(df, params, "Sound played:" + soundFile)

# Save the result
df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False, header=Header)
# dfRaw.to_csv(params['outFileRaw'], sep=',', encoding='utf-8', index=False,header=HeaderRaw)
win.close()
