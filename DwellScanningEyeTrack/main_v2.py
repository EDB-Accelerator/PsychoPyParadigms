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
- Music Interface updated on Wed, Aug  4, 2021 11:23:24 AM by KL
- Major Update (New training image dataset) on Wed, Aug 25, 2021  5:10:20 PM by KL
"""

# Import standard python libraries
import datetime,sys,random
from psychopy import visual,prefs,core,event,sound
# from glob import glob
import glob
import pylink
import numpy as np
from shutil import copyfile

# Import developer-defined functions
sys.path.insert(1, './src')
from UserInputPlay import UserInputPlay,UserInputPlayTwoThree
from DictInitialize import DictInitialize
from DisplayFixationCross import DisplayFixationCross
from DisplayMatrix import DisplayMatrix
from DisplayBlank import DisplayBlank
from DisplayRest import DisplayRest
from EyeTrackerIntialization import EyeTrackerIntialization
from EyeTrackerCalibration import EyeTrackerCalibration
from LoadTimingFile import LoadTimingFile
# from GetEmotionLabels import GetEmotionLabels,GetEmotionLabelsThreeFour
from GetEmotionLabels import GetEmotionLabels
from MakeAOI import MakeAOI
# from StartMusic import playMusic,pauseMusic,stopMusic
from WaitUserSpace import WaitUserSpace
from MusicControl import PauseMusic,UnpauseMusic,StopMusic
from DictWrite import DictWrite,DictWriteRaw
from DisplayIntroduction import DisplayIntroduction
import os
import pandas as pd
import pickle
import asyncio
import threading
import subprocess
import time
from psychopy import prefs


# # Audio library configuration.
# prefs.hardware['audioLib'] = ['PTB']
# StopMusic()

# p = subprocess.Popen('C:\Program Files\PsychoPy\python.exe src/StartMusic2.py')
# UnpauseMusic()

# Make empty output directory if it does not exist.
directory = './result'
if not os.path.exists(directory):
    os.makedirs(directory)

# Pandas configuration (debugging options)
pd.set_option('display.max_columns', None)

# Output Summary Header Initialization
Header = ["Start Time","End Time","Duration","expName","Version","subjectID","Session","Section",'timingFile',"TrialCount",
          "Image Displayed","Emotion Image Group","Image Race","The number of neutral faces","The number of emotional faces"]

# Output Raw Header Initialization
HeaderRaw = ["TimeStamp","expName","Version","subjectID","Session","Event"]

# Check if the previous session is not completed.
resumeOkay = 'no'
if os.path.isfile('.tmp/params.pkl'):

    from tkinter import *
    import tkinter.messagebox

    root = Tk()
    # Getting back the objects:
    with open('.tmp/params.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
        params, prefs, dfLabel, df, dfRaw, index, section, trial, RunList, dict, dictRaw = pickle.load(f)

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
        dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
        startTime = time.time()
        dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
        dict["Duration"] = time.time() - startTime
        DictWrite(df, params, dict)
        # if params['musicMode'] != 'off':
            # sound1 = sound.Sound(params['playlist'][params['musicIdx']])

        # Full screen support
        prefs.general['fullscr'] = params['fullscr']

        # Backup the latest EDF file.
        # backupEDFFile = params["edfFile"] + "section" + str(section)
        # copyfile(backupEDFFile + ".edf", backupEDFFile + 'backup' + datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4] + ".edf")

    else:
        print('new session selected. saved session will be deleted.')
        os.remove('.tmp/params.pkl')
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
        # 'BlockNum' : 3, # The number of blocks
        # 'RunNum' : 2, # The number of Runs
        'numTrial': UserInputBank[3],  # The number of Trials.
        'fullscr': UserInputBank[4],  # The resolution of Psychopy Window
        'screenSize': UserInputBank[5],  # The resolution of Psychopy Window
        'eyeSelection' : UserInputBank[6],  # Which eye will be used for eyetracking
        'circle' : UserInputBank[7],
        'faceMatrixDuration': 6,
        # 'musicList' : UserInputBank[9],
        'eyeIdx' : 0,
        'EyeLinkSupport': UserInputBank[8],
        'TrialCount': 0,
        "Emotion Image Group": "",
    }

    if params['Version'] == 'Green':
        params['Version'] = 3
    elif params['Version'] == 'Blue':
        params['Version'] = 4
    # if params['Version'] != 2:
    #     userInputBank2 = UserInputPlayTwoThree()
    #     params["Section"] = "Week" + str(userInputBank2[0])
    #     week = userInputBank2[0]

    # The number of trials configuration
    # if "default" in params['numTrial']:
    #     params['numTrial'] = 60 if params['Version'] == 2 else 30
    # else:
    #     params["numTrial"] = int(params["numTrial"])
    if "default" in params['numTrial']:
        params['numTrial'] = 30
    else:
        params["numTrial"] = int(params["numTrial"])

    # The number of Runs
    # params['RunNum'] = 3 if params['Version'] == 2 else 1
    params['RunNum'] = 3

    # Full screen support
    prefs.general['fullscr'] = params['fullscr']

    # Parameter Configuration based on the version.
    params['faceMatrixDuration'] = 6
    if params['Version'] == 2:
        # params['blankTime'] = [0,2,4]
        params['musicMode'] = 'off'

        # Load Timing File.
        # timingFileList = glob("timing/notUsed/*.txt")

        # if len(timingFileList) == 0:
        #     print("There is no available timing files. Please upload timing file.")
        #     exit(0)

        # random.shuffle(timingFileList)

        # params['timingFile'] = timingFileList[0]
        # df1, df2, df3 = LoadTimingFile(params['timingFile'])
    elif params['Version'] == 3:
        # params['blankTime'] = [2]
        params['musicMode'] = 'allTheTime'
        # params['faceMatrixDuration'] = 24
    elif params['Version'] == 4:
        # params['blankTime'] = [2]
        params['musicMode'] = 'onlyWhenStareAt'
        # params['faceMatrixDuration'] = 24

    # Music Selection
    if params['musicMode'] != 'off':
        # Run Music Selection GUI
        # os.system("dwellscansub\python.exe" + " src/MusicSelectionGUI.py")
        p = subprocess.Popen('C:\Program Files\PsychoPy3\python.exe src/MusicSelectionGUI.py')
        p.wait()

        os.system(sys.executable+" src/MusicSelectionGUI.py")
        df = pd.read_csv('.tmp/userMusicSelection.csv')
        playlist = df['fileName'].tolist()
        random.shuffle(playlist)
        params['playlist'] = playlist
        params['musicIdx'] = 0

        # Start Music sub-process
        p = subprocess.Popen('C:\Program Files\PsychoPy3\python.exe src/StartMusic2.py')

        # Delete music sub-process related files.
        fileList = ['.tmp/a', '.tmp/b', '.tmp/c']
        for F in fileList:
            if os.path.exists(F):
                os.remove(F)
        # labelFile = glob('img_training/Week' + str(week) + '/*.csv')[0]
        # dfLabel = pd.read_csv(labelFile)

    dfLabel = {}
    import os
    # import glob
    if params['Version'] == 2:
        labelFileList = glob.glob(f"img/Version_2*/*/*/*.csv")
    else:
        labelFileList = glob.glob(f"img/Version_3*/*/*/*.csv")
    labelList = []
    for i,labelFile in enumerate(labelFileList):
        # label = labelFile.split('_')[1]
        # label = os.path.basename(labelFile).split('_map')[0]
        label = os.path.dirname(labelFile)
        labelList.append(label)
        dfLabel[label] = pd.read_csv(labelFile)

    # else:
    #     dfLabel = {}
    #     import os
    #     # import glob
    #     labelFileList = glob.glob("labels/*")
    #     labelList = []
    #     for i,labelFile in enumerate(labelFileList):
    #         # label = labelFile.split('_')[1]
    #         label = os.path.basename(labelFile).split('_map')[0]
    #         labelList.append(label)
    #         dfLabel[label] = pd.read_csv(labelFile)

        # Old one
        # dfLabel = {}
        # labelList = ['6N10A','6N10D','8N8A','8N8D','10N6A','10N6D']
        # for label in labelList:
        #     dfLabel[label] = pd.read_csv('label_old/' + label + '.csv')


    # Decide the name of output files.
    timeLabel = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
    params['outFile'] = "./result/CSV/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
              "_" + timeLabel + ".csv"
    params['outFileRaw'] = "./result/CSV/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
              "_" + timeLabel + "_raw.csv"
    params["edfFile"] = "./result/EDF/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
              "_" + timeLabel + "_"
    params['outMusicSelection'] = "./result/CSV/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
              "_" + timeLabel + "_music_selection.csv"

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

    if params['Version'] == 2 or params['Version'] == 3 or params['Version'] == 4:
        # RunList = ['6N10D','8N8D','10N6D','6N10A','8N8A','10N6A']
        # RunList = labelList
        RunList = ['Angry-Happy','Disgust-Neutral','Sad-Happy']
        idx = 0
        Imgs = {}
        for run in RunList:
            params["Emotion Image Group"] = run
            # if 'D' in run:
            #     Imgs[run] = glob('img/Disgust-Neutral/' + run + '/*.jpeg')
            # elif 'A' in run:
            #     Imgs[run] = glob('img/Anger-Neutral/' + run + '/*.jpeg')
            imgFolderName = "Version_2_Assessment_Dwell" if params['Version'] == 2 else "Version_3_4_Task_Music"
            ImgsFolder = glob.glob(f'img/{imgFolderName}/' + run)[0]
            Imgs_Asian = glob.glob(f"{ImgsFolder}/A*/*.jpeg")
            Imgs_Black = glob.glob(f"{ImgsFolder}/B*/*.jpeg")
            Imgs_White = glob.glob(f"{ImgsFolder}/W*/*.jpeg")

            # Shuffle
            import random
            random.shuffle(Imgs_Asian)
            random.shuffle(Imgs_Black)
            random.shuffle(Imgs_White)

            # Select 10 imasges from each race categories.
            Imgs[run] = Imgs_Asian[:10] + Imgs_Black[:10] + Imgs_White[:10]
            random.shuffle(Imgs[run])
        random.shuffle(RunList)
        # Load Timing File
        # dfTiming = LoadTimingFile(params['timingFile'])
        # ImgList = []
        # for emotion in dfTiming['class']:
        #     emotion = emotion[1:-1]
        #     ImgList.append(Imgs[emotion].pop())

        # params['RestTiming'] = np.array(dfTiming['rest'])
    # else:
    #     ImgFolder = 'img_training/Week' + str(week)
    #     ImgList = glob(ImgFolder + '/*.jpg')
    #     random.shuffle(ImgList)
    #
    # params['ImgList'] = ImgList

# Run the main task.
if os.path.isfile('.tmp/params.pkl') == False:
    index = 0
    section = 0

win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')

# while section < 3:
if params['Version'] < 5:
    while section < params['RunNum']:
        params["Section"] = section # This block is different from original block.
        run = RunList[section]
        params["Emotion Image Group"] = run
        # Eyetracker Calibration.
        if params['EyeLinkSupport']:
            win,io,tracker = EyeTrackerIntialization(params,win)
            tracker = EyeTrackerCalibration(df,dfRaw,dict,dictRaw,params, tracker,win)
        else:
            tracker = None

        # Instruction Slide
        # DisplayIntroduction(df, dfRaw, params, dict, dictRaw, win, tracker)

        # If version is 2, '5' needs to be pressed to continue.
        # message = visual.TextStim(win,text="Waiting for scanner…\n ",
        #                           units='norm', wrapWidth=2, color="black")
        # message.draw()
        win.flip()
        # c = ''

        # Record (start)
        # dictRaw["Event"] = "Message: Waiting for scanner (start)"
        # DictWriteRaw(dfRaw, dictRaw, params)
        # startTime = time.time()
        # dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
        #
        # while (c != ['5']):
        #     core.wait(1 / 120)
        #     c = event.getKeys()
        #
        # # Record (end)
        # dictRaw["Event"] = "Message: Waiting for scanner (end)"
        # DictWriteRaw(dfRaw, dictRaw, params)
        # dict["Image Displayed"] = "Message: Waiting for scanner"
        # dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
        # dict["Duration"] = time.time() - startTime
        # DictWrite(df, params, dict)

        # Wait for 5 seconds. (Get Ready Screen)
        message = visual.TextStim(win,
                                  text="Get Ready\n ",
                                  units='norm', wrapWidth=2, color="black")
        message.draw()
        win.flip()
        # core.wait(8)

        # Record Result (raw start)
        dictRaw["Event"] = "Message: Get Ready (start)"
        DictWriteRaw(dfRaw, dictRaw, params)
        startTime = time.time()
        dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]

        core.wait(5)
        # Record result
        dictRaw["Event"] = "Message: Get Ready (end)"
        DictWriteRaw(dfRaw, dictRaw, params)
        dict["Image Displayed"] = "Message: Get Ready"
        dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
        dict["Duration"] = time.time() - startTime
        DictWrite(df, params, dict)

        # Start recording
        dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
        sectionStartTime = time.time()
        dict["Section"] = "Start Recording"
        dict["Image Displayed"] = "Recording started"
        dictRaw["Event"] = "Recording started"
        DictWriteRaw(dfRaw, dictRaw, params)

        if params['EyeLinkSupport']:
            tracker.setRecordingState(True)

        dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
        dict["Duration"] = time.time() - sectionStartTime
        DictWrite(df, params, dict)

        # Start Music
        if params['Version'] != 2:
            UnpauseMusic()

        # for trial in range(params['numTrial']):
        if os.path.isfile('.tmp/params.pkl') == False:
            trial = 0

        # Fixation Line randomization
        fixationOrder = ['l','r','c']*10
        random.shuffle(fixationOrder)
        params['fixationOrder'] = fixationOrder

        while trial < params['numTrial']:
            params["TrialCount"] = trial
            # img = (params['ImgList'])[trial+section*params['numTrial']]
            img = Imgs[run][trial]

            # Get emotion labels.
            emotion, labels = GetEmotionLabels(dfLabel, img)

            # Fixation cross section (Version 2 only)
            DisplayFixationCross(df=df,dfRaw=dfRaw,params=params,dict=dict,dictRaw=dictRaw,win=win,tracker=tracker)

            # Display face matrix
            DisplayMatrix(df=df,dfRaw=dfRaw,img=img,params=params,dict=dict,dictRaw=dictRaw,win=win,tracker=tracker,
                          labels=labels,emotion=emotion)

            # Display Rest (Blank) (Version 2 only).
            # DisplayBlank(df=df, dfRaw=dfRaw, params=params, dict=dict, dictRaw=dictRaw, win=win, tracker=tracker,
            #                  blankTime=params['RestTiming'][index])
            DisplayBlank(df=df, dfRaw=dfRaw, params=params, dict=dict, dictRaw=dictRaw, win=win, tracker=tracker,
                             blankTime=2.0)
            index += 1
            trial += 1

        # Stop Recording
        dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
        sectionStartTime = time.time()
        dict["Section"] = "Recording Ended"
        dict["Image Displayed"] = "Recording ended"
        dictRaw["Event"] = "Recording ended"
        DictWriteRaw(dfRaw, dictRaw, params)

        dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
        dict["Duration"] = time.time() - sectionStartTime
        DictWrite(df, params, dict)

        # Import the result (from eyetracker)
        if params['EyeLinkSupport']:
            tracker.setRecordingState(False)
            trackerIO = pylink.EyeLink('100.1.1.1')
            trackerIO.receiveDataFile("et_data.EDF", params["edfFile"] + "section" + str(section) +".edf")
            # Stop the ioHub Server
            io.quit()
            trackerIO.close()

        if section != 2:
            # Rest between each section. (ITI duration)
            DisplayRest(df, dfRaw, params, dict, dictRaw, win)
        section += 1
        trial = 0
        # Save the current status.
        with open('.tmp/params.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
            pickle.dump([params, prefs, dfLabel, df, dfRaw, index, section, trial,dict, dictRaw], f)
# else:
#     # Eyetracker Calibration.
#     win,io,tracker = EyeTrackerIntialization(params,win)
#     tracker = EyeTrackerCalibration(df,dfRaw,dict,dictRaw,params, tracker,win)
#
#     # Wait for 8 seconds. (Get Ready Screen)
#     message = visual.TextStim(win,
#                               text="Get Ready\n ",
#                               units='norm', wrapWidth=2, color="black")
#     message.draw()
#     win.flip()
#     core.wait(8)
#
#     # Start recording
#     dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
#     sectionStartTime = time.time()
#     dict["Section"] = "Start Recording"
#     dict["Image Displayed"] = "Recording started"
#     dictRaw["Event"] = "Recording started"
#     DictWriteRaw(dfRaw, dictRaw, params)
#
#     tracker.setRecordingState(True)
#
#     dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
#     dict["Duration"] = time.time() - sectionStartTime
#     DictWrite(df, params, dict)
#
#     # Start Music
#     UnpauseMusic()
#
#     # If the program has been resumed, start from trial=0.
#     if os.path.isfile('.tmp/params.pkl') == False:
#         trial = 0
#
#     for trial in range(params['numTrial']):
#         params["TrialCount"] = trial
#         img = (params['ImgList'])[trial]
#
#         # Get emotion labels.
#         emotion,labels = GetEmotionLabelsThreeFour(dfLabel,img)
#
#         # Display face matrix
#         DisplayMatrix(df=df,dfRaw=dfRaw,img=img,params=params,dict=dict,dictRaw=dictRaw,win=win,tracker=tracker,
#                       labels=labels,emotion=emotion)
#
#     # Stop Recording
#     dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
#     sectionStartTime = time.time()
#     dict["Section"] = "Recording Ended"
#     dict["Image Displayed"] = "Recording ended"
#     dictRaw["Event"] = "Recording ended"
#     DictWriteRaw(dfRaw, dictRaw, params)
#
#     tracker.setRecordingState(False)
#
#     dict["End Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
#     dict["Duration"] = time.time() - sectionStartTime
#     DictWrite(df, params, dict)
#
#     # Import the result (from eyetracker)
#     trackerIO = pylink.EyeLink('100.1.1.1')
#     trackerIO.receiveDataFile("et_data.EDF", params["edfFile"] + "section" + str(section) +".edf")
#
#     # Stop the ioHub Server
#     if params['EyeLinkSupport']:
#         io.quit()
#         trackerIO.close()
#     trial = 0
#     # Save the current status.
#     with open('.tmp/params.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
#         pickle.dump([params, prefs, dfLabel, df, dfRaw, index, section, trial,dict, dictRaw], f)


# Stop music.
if params['musicMode'] != 'off':
    # sound1 = stopMusic(sound1)
    StopMusic()

# Close the psychopy window.
# win.close()

# if params['Version'] == 2:
#     # Move timing file into 'used' folder.
#     try:
#         os.makedirs('timing/used')
#     except:
#         pass
#
#     params['timingFileNew'] = params['timingFile'].replace('notUsed','used')
#     os.rename(params['timingFile'],params['timingFileNew'])

if params['musicMode'] != 'off':
    copyfile(".tmp/userMusicSelection.csv", params['outMusicSelection'])

# Delete status backup pickle file
try:
    os.remove('.tmp/params.pkl')
except:
    pass

# win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')
win.mouseVisible = False
message = visual.TextStim(win,text="Thank you so much!\n ",
                                  units='norm', wrapWidth=2, color="black")
message.draw()
win.flip()
core.wait(3)
win.close()
