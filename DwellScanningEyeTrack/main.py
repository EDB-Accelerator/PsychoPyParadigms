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
DwellTask.py

DwellTask Psychopy3 Main Driver File.

Created on Thu Jan 28 15:20:30 EST 2021
Updated on Thu May  6 14:11:14 EDT 2021 (ITI: always 2 sec. Included rest screen)

@author: Kyunghun Lee
- Created on Thu Jan 28 15:20:30 EST 2021 by KL
- Major updated on July 5 EST 2021 by KL
- Pause and Resume on Wed, Jul 14, 2021  3:13:55 PM by KL
"""

# Import standard python libraries
import datetime,sys,random
from psychopy import visual,prefs,core,event,sound
from glob import glob
import pylink
import numpy as np
from shutil import copyfile

# Import developer-defined functions
sys.path.insert(1, './src')
from UserInputPlay import UserInputPlay
from DictInitialize import DictInitialize
from DisplayFixationCross import DisplayFixationCross
from DisplayMatrix import DisplayMatrix
from DisplayBlank import DisplayBlank
from DisplayRest import DisplayRest
from EyeTrackerIntialization import EyeTrackerIntialization
from EyeTrackerCalibration import EyeTrackerCalibration
from LoadTimingFile import LoadTimingFile
from GetEmotionLabels import GetEmotionLabels
from MakeAOI import MakeAOI
from StartMusic import playMusic,pauseMusic,stopMusic
from WaitUserSpace import WaitUserSpace
import os
import pandas as pd
import pickle

# Make empty output directory if it does not exist.
directory = './result'
if not os.path.exists(directory):
    os.makedirs(directory)

# Pandas configuration (debugging options)
pd.set_option('display.max_columns', None)

# Output Summary Header Initialization
Header = ["Start Time","End Time","Duration","expName","Version","subjectID","Session","Section",'timingFile',"TrialCount",
          "Image Displayed"]

# Output Raw Header Initialization
HeaderRaw = ["TimeStamp","expName","Version","subjectID","Session","Event"]

###
resumeOkay = 'no'
if os.path.isfile('params.pkl'):

    from tkinter import *
    import tkinter.messagebox

    root = Tk()
    # Getting back the objects:
    with open('params.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
        params, prefs, dfLabel, df, dfRaw, index, section, trial, dict, dictRaw = pickle.load(f)

    resumeOkay = tkinter.messagebox.askquestion('Resume', 'Do you want to resume your previous section? (subject id:' + params['subjectID'] + ')')
    if resumeOkay == 'yes':
        print('resume selected')
        root.destroy()

        # Record.
        from DictWrite import DictWrite, DictWriteRaw
        from shutil import copyfile
        import time
        dictRaw["Event"] = "Program Resumed"
        DictWriteRaw(dfRaw, dictRaw, params)
        params["TrialCount"] = trial
        params["Section"] = section
        dict["Image Displayed"] = "Program Resumed"
        dict["Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
        startTime = time.time()
        dict["End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
        dict["Duration"] = time.time() - startTime
        DictWrite(df, params, dict)
        if params['musicMode'] != 'off':
            sound1 = sound.Sound(params['playlist'][params['musicIdx']])

        # Full screen support
        prefs.general['fullscr'] = params['fullscr']

        # Backup the latest EDF file.
        # backupEDFFile = params["edfFile"] + "section" + str(section)
        # copyfile(backupEDFFile + ".edf", backupEDFFile + 'backup' + datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4] + ".edf")

    else:
        print('new session selected. saved session will be deleted.')
        os.remove('params.pkl')
        root.destroy()  # Closing Tkinter window forcefully.
    root.mainloop()

if resumeOkay == 'no':
    # Receive User input from Window.
    UserInputBank = UserInputPlay()

    # Declare primary task parameters.
    params = {
        'expName' : 'DwellTask', # The name of the experiment
        'subjectID' : UserInputBank[0],      # Subject ID
        'Session' : UserInputBank[1], # Session ID
        'Version': UserInputBank[2],  # Version
        'BlockNum' : 3, # The number of blocks
        'RunNum' : 2, # The number of Runs
        'numTrial': UserInputBank[3],  # The number of Trials.
        'fullscr': UserInputBank[4],  # The resolution of Psychopy Window
        'screenSize': UserInputBank[5],  # The resolution of Psychopy Window
        'eyeSelection' : UserInputBank[6],  # Which eye will be used for eyetracking
        'circle' : UserInputBank[7],
        'faceMatrixDuration': 6,
        # 'musicList' : UserInputBank[9],
        'eyeIdx' : 0,
    }

    # The number of trials configuration
    if "default" in params['numTrial']:
        params['numTrial'] = 60 if params['Version'] == 2 else 30
    else:
        params["numTrial"] = int(params["numTrial"])

    # Full screen support
    prefs.general['fullscr'] = params['fullscr']

    # Parameter Configuration based on the version.
    if params['Version'] == 2:
        # params['blankTime'] = [0,2,4]
        params['musicMode'] = 'off'
        params['faceMatrixDuration'] = 6
        # Load Timing File.
        timingFileList = glob("timing/notUsed/*.txt")

        if len(timingFileList) == 0:
            print("There is no available timing files. Please upload timing file.")
            exit(0)

        random.shuffle(timingFileList)

        params['timingFile'] = timingFileList[0]
        # df1, df2, df3 = LoadTimingFile(params['timingFile'])
    elif params['Version'] == 3:
        # params['blankTime'] = [2]
        params['musicMode'] = 'allTheTime'
        params['faceMatrixDuration'] = 24
    elif params['Version'] == 4:
        # params['blankTime'] = [2]
        params['musicMode'] = 'onlyWhenStareAt'
        params['faceMatrixDuration'] = 24

    # # Save the current status
    # with open('params.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    #     pickle.dump([params], f)

    # # Getting back the objects:
    # with open('params.pkl','rb') as f:  # Python 3: open(..., 'rb')
    #     a = pickle.load(f)

    # Music Selection
    if params['musicMode'] != 'off':
        # Run Music Selection GUI
        os.system("dwellscansub\python.exe" + " src/MusicSelectionGUI.py")
        df = pd.read_csv('userMusicSelection.csv')
        playlist = df['fileName'].tolist()
        random.shuffle(playlist)
        params['playlist'] = playlist
        params['musicIdx'] = 0
        sound1 = sound.Sound(params['playlist'][params['musicIdx']])
        # params['sound1'] = sound.Sound(params['playlist'][params['musicIdx']])

    dfLabel = {}
    labelList = ['6N-10A','6N-10D','8N-8A','8N-8D','10N-6A','10N-6D']
    for label in labelList:
        dfLabel[label] = pd.read_csv('label/' + label + '.csv')

    # Decide the name of output files.
    timeLabel = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
    params['outFile'] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
              timeLabel + ".csv"
    params['outFileRaw'] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
              timeLabel + "_raw.csv"
    params["edfFile"] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
              timeLabel + "_"
    params['outMusicSelection'] = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
              timeLabel + "_music_selection.csv"

    # Instance result initialization
    dict,dictRaw = DictInitialize(params)

    # Generate AOI locations for face matrix.
    MakeAOI(params)

    # Construct pandas dataframe structure.
    df = pd.DataFrame(columns=Header)
    dfRaw = pd.DataFrame(columns=HeaderRaw)

    # Make Empty output files.
    df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)
    dfRaw.to_csv(params['outFileRaw'], sep=',', encoding='utf-8', index=False)

    # Make image list.
    RunList = ['Anger-Neutral','Disgust-Neutral']
    idx = 0
    Imgs = {}
    for run in RunList:
        ImgTmp = []
        BlockList = glob('img/' + run + '/*')
        random.shuffle(BlockList)

        for block in BlockList:
            # params["Block"] = block.split('/')[-1]

            # Get Image list of each block and Shuffle.
            ImgTmp = ImgTmp + glob(block + '/*.jpeg')
            idx += 1
        random.shuffle(ImgTmp)
        Imgs[run] = ImgTmp

    ImgList = []
    if params['Version'] == 2:
        # Load Timing File
        dfTiming = LoadTimingFile(params['timingFile'])
        i = 0
        j = 0
        for emotion in dfTiming['class']:
            if emotion == 1:
                ImgList.append(Imgs['Disgust-Neutral'][i])
                i += 1
            else:
                ImgList.append(Imgs['Anger-Neutral'][j])
                j += 1
        params['RestTiming'] = np.array(dfTiming['rest'])

    elif params['Version'] == 3 or params['Version'] == 4:
        random.shuffle(Imgs['Disgust-Neutral'])
        random.shuffle(Imgs['Anger-Neutral'])

        # Image combination (DN: 30, AN: 30 for each block)
        imgList1 = Imgs['Disgust-Neutral'][:30] + Imgs['Anger-Neutral'][:30]
        imgList2 = Imgs['Disgust-Neutral'][30:60] + Imgs['Anger-Neutral'][30:60]
        imgList3 = Imgs['Disgust-Neutral'][60:] + Imgs['Anger-Neutral'][60:]

        # shuffle each list.
        random.shuffle(imgList1)
        random.shuffle(imgList2)
        random.shuffle(imgList3)

        # Combine varialbles into one single variable.
        ImgList = imgList1 + imgList2 + imgList3

    params['ImgList'] = ImgList

# Run the main task.
if os.path.isfile('params.pkl') == False:
    index = 0
    section = 0
# for section in range(3):
while section < 3:
    params["Section"] = section # This block is different from original block.

    # Eyetracker Calibration.
    win,io,tracker = EyeTrackerIntialization(params)
    win,tracker = EyeTrackerCalibration(df,dfRaw,dict,dictRaw,params, tracker,win)

    # If version is 2, '5' needs to be pressed to continue.
    if params['Version'] == 2:
        message = visual.TextStim(win,text="Please press 5 to continue.\n ",
                                  units='norm', wrapWidth=2, color="black")
        message.draw()
        win.flip()
        c = ''
        while (c != ['5']):
            core.wait(1 / 120)
            c = event.getKeys()

    # Wait for 8 seconds. (Get Ready Screen)
    message = visual.TextStim(win,
                              text="Get Ready\n ",
                              units='norm', wrapWidth=2, color="black")
    message.draw()
    win.flip()
    core.wait(8)

    # Start recording
    tracker.setRecordingState(True)

    # Start Music
    if params['musicMode'] != 'off':
        sound1 = playMusic(sound1,params)
    else:
        sound1 = ""

    # for trial in range(params['numTrial']):
    if os.path.isfile('params.pkl') == False:
        trial = 0
    while trial < params['numTrial']:
        params["TrialCount"] = trial
        img = (params['ImgList'])[trial+section*params['numTrial']]

        # Get emotion labels.
        emotion,labels = GetEmotionLabels(dfLabel,img)

        # Fixation cross section
        if params['Version'] == 2:
            DisplayFixationCross(df=df,dfRaw=dfRaw,params=params,dict=dict,dictRaw=dictRaw,win=win,tracker=tracker)

        # Display face matrix
        sound1 = DisplayMatrix(df=df,dfRaw=dfRaw,img=img,params=params,dict=dict,dictRaw=dictRaw,win=win,tracker=tracker,
                      labels=labels,emotion=emotion,sound1=sound1)

        # Display Rest.
        if params['Version'] == 2:
            DisplayBlank(df=df, dfRaw=dfRaw, params=params, dict=dict, dictRaw=dictRaw, win=win, tracker=tracker,
                         blankTime=params['RestTiming'][index])
        # else:
        #     DisplayBlank(df=df, dfRaw=dfRaw, params=params, dict=dict, dictRaw=dictRaw, win=win, tracker=tracker,
        #                  blankTime=2)
        index += 1
        trial += 1

        # Save the current status
        # with open('params.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
        #     pickle.dump([params, prefs, dfLabel, df, dfRaw, index], f)
        # Save the current status.
        # with open('params.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
        #     pickle.dump([params,prefs,dfLabel,df,dfRaw,index,section,trial,dict,dictRaw], f)

    # Stop Recording
    tracker.setRecordingState(False)

    # Import the result (from eyetracker)
    trackerIO = pylink.EyeLink('100.1.1.1')
    trackerIO.receiveDataFile("et_data.EDF", params["edfFile"] + "section" + str(section) +".edf")

    # Stop the ioHub Server
    io.quit()
    trackerIO.close()
    if section != 2:
        # Rest between each section. (ITI duration)
        sound1 = DisplayRest(df, dfRaw, params, dict, dictRaw, win,sound1)
    section += 1
    trial = 0
    # Save the current status.
    with open('params.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump([params, prefs, dfLabel, df, dfRaw, index, section, trial,dict, dictRaw], f)

# Stop music.
if params['musicMode'] != 'off':
    sound1 = stopMusic(sound1)

# Close the psychopy window.
win.close()

if params['Version'] == 2:
    # Move timing file into 'used' folder.
    params['timingFileNew'] = params['timingFile'].replace('notUsed','used')
    os.rename(params['timingFile'],params['timingFileNew'])

if params['musicMode'] != 'off':
    copyfile("userMusicSelection.csv", params['outMusicSelection'])

# Delete status backup pickle file
os.remove('params.pkl')

win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')
win.mouseVisible = False
message = visual.TextStim(win,text="Thank you so much!\n ",
                                  units='norm', wrapWidth=2, color="black")
message.draw()
win.flip()
core.wait(3)
win.close()