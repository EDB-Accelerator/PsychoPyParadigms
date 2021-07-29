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
@author: Kyunghun Lee
- Created on Sun Jul 25 01:37:33 EDT 2021 by KL
"""

# Import dependencies.
import sys
from psychopy import visual,core,event
import pandas as pd
import glob
import time
import datetime

# Import developer-defined functions
sys.path.insert(1, './src')
from WaitAndGetUserInput import WaitAndGetUserInput,WaitUserSpace
from DictWrite import DataWrite
from PlayUserInputGUI import PlayUserInputGUI
from PlayIntroduction import PlayIntroduction

# Receive User input from GUI window
params = PlayUserInputGUI()

# Start Session
startTime = datetime.datetime.now()

# Make Empty output files Construct pandas dataframe structure.
Header = ["expName", "subjectID", "Session", "TrialCount", "Event", "Start Time", "End Time", "Duration (sec)",
          'Timing File', "User Response", "Right Answer", "Correct or Incorrect", "User Response TimeStamp",
          "User Response Time (the amount of time that passes from time the letter was shown)"]
df = pd.DataFrame(columns=Header)
df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)

# Psychopy Window Initialization
win = visual.Window(monitor="testMonitor", color="black", winType='pyglet',size=[1024,768])
win.mouseVisible = False

# Display Welcome Screen / Introduction
win = PlayIntroduction(win,params)

# Get a Timing file list
timingFiles = glob.glob('timing/*.csv')
timingFiles.sort()

# timingFile = timingFiles[0]
for timingFile in timingFiles:

    # Load a Timing File.
    dfTiming = pd.read_csv(timingFile,header=None,names=['Trial Type','Delay Between Letters', 'Delay Between Trials'])

    ### ITI section ###
    startTime = datetime.datetime.now()
    message = visual.TextStim(win, text="+", wrapWidth=2,units='norm',color="white")
    message.draw()
    win.flip()
    c = ['']
    # Wait for user until user types "5".
    while (c[0]!="5"):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

    # ITI Section Termination
    DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount="",
              event="ITI", timingFile=timingFile, userResponse="5", rightAnswer="5",userResponseTime="",
              userResponseOffset=0)
    ### ITI section (end) ###

    for i in range(params['numTrial']):
        # Extract Timing Information
        trialLetter = dfTiming.iloc[i]['Trial Type']
        delayBetweenLetters = dfTiming.iloc[i]['Delay Between Letters'] / 1000
        delayBetweenTrials = dfTiming.iloc[i]['Delay Between Trials'] / 1000

        # Display the first letter (cue)
        startCueTime = datetime.datetime.now()
        rightAnswer = "N"

        message = visual.TextStim(win, text=trialLetter[0],wrapWidth=2,units='norm',color="blue",height=1.005)
        message.draw()
        win.flip()
        c,responseTime = WaitAndGetUserInput([],0.5)
        if responseTime == "":
            responseTime = "No response"
            c = "No response"

        DataWrite(params=params, startTime=startCueTime, endTime=datetime.datetime.now(), trialCount=str(i),
                  event="First Letter Displayed.",
                  timingFile=timingFile, userResponse=c, rightAnswer=rightAnswer,userResponseTime=responseTime,
                  userResponseOffset=0)

        # Display Fixation Cross (response window)
        startResponseFixationTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", wrapWidth=2,units='norm',color="white")
        message.draw()
        win.flip()
        c,responseTime = WaitAndGetUserInput(c,1.5)
        DataWrite(params=params, startTime=startResponseFixationTime, endTime=datetime.datetime.now(), trialCount=str(i),
                  event="Fixation Displayed (Response Window)",
                  timingFile=timingFile, userResponse=c, rightAnswer=rightAnswer,userResponseTime=responseTime,
                  userResponseOffset=0.5)

        # Display Fixation Cross (Delay Between Letters)
        startTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", wrapWidth=2,units='norm',color="white")
        message.draw()
        win.flip()
        core.wait(delayBetweenLetters)
        DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount=str(i),
                  event="Fixation Displayed (Delay Between Letters)",
                  timingFile=timingFile, userResponse="", rightAnswer="",userResponseTime="",
                  userResponseOffset=0)

        # Display the second letter (probe)
        startProbeTime = datetime.datetime.now()
        rightAnswer = "Y" if trialLetter == "AX" else "N"
        message = visual.TextStim(win, text=trialLetter[1],wrapWidth=2,units='norm',color="white",height=1.005)
        message.draw()
        win.flip()
        c,responseTime = WaitAndGetUserInput([],0.5)
        if responseTime == "":
            responseTime = "No response"
            c = "No response"

        DataWrite(params=params, startTime=startProbeTime, endTime=datetime.datetime.now(), trialCount=str(i),
                  event="Second Letter Displayed.("+str(trialLetter[1]) + ")",
                  timingFile=timingFile, userResponse=c, rightAnswer=rightAnswer,userResponseTime=responseTime,
                  userResponseOffset=0)

        # Display Fixation Cross (response window)
        startResponseFixationTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", wrapWidth=2,units='norm',color="white")
        message.draw()
        win.flip()
        c,responseTime = WaitAndGetUserInput(c,1.5)
        DataWrite(params=params, startTime=startResponseFixationTime, endTime=datetime.datetime.now(), trialCount=str(i),
                  event="Fixation Displayed (Response Window)",
                  timingFile=timingFile, userResponse=c, rightAnswer=rightAnswer,userResponseTime=responseTime,
                  userResponseOffset=0.5)

        # Display Fixation Cross (Delay Between Trials)
        startTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", wrapWidth=2,units='norm',color="white")
        message.draw()
        win.flip()
        core.wait(delayBetweenTrials)
        DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount=str(i),
                  event="Fixation Displayed (Delay Between Trials)",
                  timingFile=timingFile, userResponse="", rightAnswer="",userResponseTime="",
                  userResponseOffset=0)
