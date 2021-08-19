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
import random

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
Header = ["expName", "subjectID", "Session", "TrialCount", "Trial Type","Event", "Start Time", "End Time", "Duration (sec)",
          'Timing File', "User Response", "Right Answer", "Correct or Incorrect", "User Response TimeStamp",
          "User Response Time (the amount of time that passes from time the letter was shown)","Cue Letter","Probe Letter"]
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
random.shuffle(timingFiles)

# timingFile = timingFiles[0]
for timingFile in timingFiles:
    BList = ['B','C','F','H','I','M','Q','R','T','V','Z']
    YList = ['Y','D','E','G','J','L','N','O','P','S','U','W']
    random.shuffle(BList)
    random.shuffle(YList)

    # Load a Timing File.
    dfTiming = pd.read_csv(timingFile,header=None,names=['Trial Type','Delay Between Letters', 'Delay Between Trials'])

    ### wait section (wait for "space bar") ###
    startTime = datetime.datetime.now()
    message = visual.TextStim(win, text="Press Wait for the Task to Start\n\n"
                                        "(Experimenter, press 'SPACE BAR')",
                              units='norm', wrapWidth=1000, color="white")
    if params['debug']:
        message2 = visual.TextStim(win, text="waiting for spacebar",
                                  units='norm', wrapWidth=1000, color="red",pos=[0,0.5])
        message2.draw()

    message.draw()
    win.flip()
    c = ['']
    # Wait for user until user types "space bar".
    while (c[0]!="space"):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

    # wait Section Termination
    DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount="",trialType="",
              event="waiting for spacebar", timingFile=timingFile, userResponse="space bar", rightAnswer="space bar",
              userResponseTime="",userResponseOffset=0,cueLetter="",probeLetter="")

    ### ITI section (wait for "5") ###
    startTime = datetime.datetime.now()
    message = visual.TextStim(win, text="+", wrapWidth=2,units='norm',color="white")
    if params['debug']:
        message2 = visual.TextStim(win, text="ITI (waiting for 5)",
                                  units='norm', wrapWidth=1000, color="red",pos=[0,0.5])
        message2.draw()
    message.draw()
    win.flip()
    c = ['']
    # Wait for user until user types "5".
    while (c[0]!="5"):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

    DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount="",trialType="",
              event="ITI (waiting for 5)", timingFile=timingFile, userResponse="5", rightAnswer="5",
              userResponseTime="",userResponseOffset=0,cueLetter="",probeLetter="")

    ### ITI section (end) ###

    for i in range(params['numTrial']):
        # Extract Timing Information
        trialLetter = dfTiming.iloc[i]['Trial Type']
        delayBetweenLetters = dfTiming.iloc[i]['Delay Between Letters'] / 1000
        delayBetweenTrials = dfTiming.iloc[i]['Delay Between Trials'] / 1000

        # Display the first letter (cue)
        startCueTime = datetime.datetime.now()
        rightAnswer = "N"

        CueLetter = 'A' if trialLetter[0] == 'A' else BList.pop()
        ProbeLetter = 'X' if trialLetter[1] == 'X' else YList.pop()

        # message = visual.TextStim(win, text=trialLetter[0],wrapWidth=2,units='norm',color="cyan",height=1.005)
        message = visual.TextStim(win, text=CueLetter, units='pix',height=80,color="cyan",
                                  font='arial',bold=True)
        message.draw()
        if params['debug']:
            message2 = visual.TextStim(win, text="first letter (cue) displayed for 0.5 sec.",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        win.flip()
        c,responseTime = WaitAndGetUserInput([],0.5)
        if responseTime == "":
            responseTime = "No response"
            c = "No response"

        DataWrite(params=params, startTime=startCueTime, endTime=datetime.datetime.now(), trialCount=str(i),
                  # trialType=trialLetter,event="First Letter Displayed.("+str(trialLetter[0]) + ")",
                  trialType=trialLetter, event="First Letter Displayed.(" + str(CueLetter) + ")",
                  timingFile=timingFile, userResponse=c, rightAnswer=rightAnswer,userResponseTime=responseTime,
                  userResponseOffset=0,cueLetter=CueLetter,probeLetter=ProbeLetter)

        # Display Fixation Cross (response window)
        startResponseFixationTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", units='pix',height=32,color="white")
        message.draw()
        if params['debug']:
            message2 = visual.TextStim(win, text="fixation cross (response window) for 1.5 sec.",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        win.flip()

        if c != "No response":
            c = "Already answered"
            core.wait(1.5)
        else:
            c,responseTime = WaitAndGetUserInput(c,1.5)
            if responseTime == "":
                responseTime = "No response"
                c = "No response"

        DataWrite(params=params, startTime=startResponseFixationTime, endTime=datetime.datetime.now(), trialCount=str(i),
                  trialType=trialLetter,
                  event="Fixation Displayed (Response Window)",
                  timingFile=timingFile, userResponse=c, rightAnswer=rightAnswer,userResponseTime=responseTime,
                  userResponseOffset=0.5,cueLetter="",probeLetter="")

        # Display Fixation Cross (Delay Between Letters)
        startTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", units='pix',height=32,color="white")
        message.draw()
        if params['debug']:
            message2 = visual.TextStim(win, text="fixation cross (delay between letters) for "+str(delayBetweenLetters) +" sec.",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        win.flip()
        core.wait(delayBetweenLetters)
        DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount=str(i),trialType=trialLetter,
                  event="Fixation Displayed (Delay Between Letters)",
                  timingFile=timingFile, userResponse="", rightAnswer="",userResponseTime="",
                  userResponseOffset=0,cueLetter="",probeLetter="")

        # Display the second letter (probe)
        startProbeTime = datetime.datetime.now()
        rightAnswer = "Y" if trialLetter == "AX" else "N"

        # message = visual.TextStim(win, text=trialLetter[1],wrapWidth=2,units='norm',color="white",height=1.005)
        message = visual.TextStim(win, text=ProbeLetter, units='pix',height=80, color="white",
                                  font='arial',bold=True)
        message.draw()
        if params['debug']:
            message2 = visual.TextStim(win, text="second letter (probe) displayed for 0.5 sec",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        win.flip()
        c,responseTime = WaitAndGetUserInput([],0.5)
        if responseTime == "":
            responseTime = "No response"
            c = "No response"

######
# startTime = startProbeTime
# endTime = datetime.datetime.now()
# trialCount = str(i)
# trialType = trialLetter
# event="Second Letter Displayed.("+str(trialLetter[1]) + ")"
# timingFile=timingFile
# userResponse=c
# rightAnswer=rightAnswer
# userResponseTime=responseTime
# userResponseOffset=0

######

        DataWrite(params=params, startTime=startProbeTime, endTime=datetime.datetime.now(), trialCount=str(i),trialType=trialLetter,
                  # event="Second Letter Displayed.("+str(trialLetter[1]) + ")",
                  event="Second Letter Displayed.(" + str(ProbeLetter) + ")",
                  timingFile=timingFile, userResponse=c, rightAnswer=rightAnswer,userResponseTime=responseTime,
                  userResponseOffset=0,cueLetter=CueLetter,probeLetter=ProbeLetter)

        # Display Fixation Cross (response window)
        startResponseFixationTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", units='pix',height=32,color="white")
        message.draw()
        if params['debug']:
            message2 = visual.TextStim(win, text="fixation cross (response window) for 1.5 sec",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        win.flip()

        if c != "No response":
            c = "Already answered"
            core.wait(1.5)
        else:
            c,responseTime = WaitAndGetUserInput(c,1.5)
            if responseTime == "":
                responseTime = "No response"
                c = "No response"

        DataWrite(params=params, startTime=startResponseFixationTime, endTime=datetime.datetime.now(), trialCount=str(i),trialType=trialLetter,
                  event="Fixation Displayed (Response Window)",
                  timingFile=timingFile, userResponse=c, rightAnswer=rightAnswer,userResponseTime=responseTime,
                  userResponseOffset=0.5,cueLetter="",probeLetter="")

        # Display Fixation Cross (Delay Between Trials)
        startTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", units='pix',height=32,color="white")
        if params['debug']:
            message2 = visual.TextStim(win, text="fixation cross (delay between trials) for "+str(delayBetweenTrials) +" sec.",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        message.draw()
        win.flip()
        core.wait(delayBetweenTrials)
        DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount=str(i),trialType=trialLetter,
                  event="Fixation Displayed (Delay Between Trials)",
                  timingFile=timingFile, userResponse="", rightAnswer="",userResponseTime="",
                  userResponseOffset=0,cueLetter="",probeLetter="")

message = visual.TextStim(win, text="Thank you!",
                          units='norm', wrapWidth=1000, color="white")
message.draw()
win.flip()
core.wait(2)
win.close()
