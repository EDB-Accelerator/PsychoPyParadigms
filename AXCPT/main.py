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
- Updated on Fri Aug 20 09:15:51 EDT 2021 by KL
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

def checkUserQuit():
    c = event.getKeys()
    if c == ['q'] or c == ['Q']:
        print('Q pressed. Forced Exit.')
        core.quit()

def waitForSeconds(waitTime):
    startTime = time.time()
    while time.time() - startTime < waitTime:
        c = event.getKeys()
        if c == ['q'] or c == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()
        core.wait(1/120)

# Receive User input from GUI window
params = PlayUserInputGUI()

# Psychopy Window Initialization
win = visual.Window(monitor="testMonitor", color="black", size=[1024,768],winType='pyglet')
# win.mouseVisible = False
# winType='pyglet',
# Start Session
startTime = datetime.datetime.now()

# Make Empty output files Construct pandas dataframe structure.
Header = ["expName", "subjectID", "Session", "TrialCount", "TimingCount", "Trial Type", "Event", "Start Time",
          "End Time",
          "Duration (sec)",
          'Timing File', "User Response", "Right Answer", "Correct or Incorrect", "User Response TimeStamp",
          "User Response Time (the amount of time that passes from time the letter was shown)", "Cue Letter",
          "Probe Letter"]
df = pd.DataFrame(columns=Header)
df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)


# Display Welcome Screen / Introduction
win.winHandle.maximize()
win.winHandle.activate()
win.flip()
# win.winHandle.maximize()
win = PlayIntroduction(win,params,"")

# Get a Timing file list
timingFiles = glob.glob('timing/*.csv')
timingFiles.sort()
random.shuffle(timingFiles)

# timingFile = timingFiles[0]
timingFileCount = 0
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
        if c == ['q'] or c == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()

    # wait Section Termination
    DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount="",timingCount=timingFileCount, trialType="",
              event="waiting for spacebar", timingFile=timingFile, userResponse="space bar", rightAnswer="space bar",
              userResponseTime="",userResponseOffset=0,cueLetter="",probeLetter="",correctness="")

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
        if c == ['q'] or c == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()

    DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount="",timingCount=timingFileCount,trialType="",
              event="ITI (waiting for 5)", timingFile=timingFile, userResponse="5", rightAnswer="5",
              userResponseTime="",userResponseOffset=0,cueLetter="",probeLetter="",correctness="")

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
        message = visual.TextStim(win, text=CueLetter, units='pix',height=params['fontSize'],color="cyan",
                                  font='arial',bold=True)
        message.draw()
        if params['debug']:
            message2 = visual.TextStim(win, text="first letter (cue) displayed for 0.5 sec.",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        win.flip()
        c,responseTime = WaitAndGetUserInput([],0.5)
        if responseTime == "":
            responseTime = ""
            c = ""

        DataWrite(params=params, startTime=startCueTime, endTime=datetime.datetime.now(), trialCount=str(i+1),timingCount=timingFileCount,
                  # trialType=trialLetter,event="First Letter Displayed.("+str(trialLetter[0]) + ")",
                  trialType=trialLetter, event="First Letter Displayed.(" + str(CueLetter) + ")",
                  timingFile=timingFile, userResponse="", rightAnswer="",userResponseTime="",
                  userResponseOffset=0,cueLetter=CueLetter,probeLetter=ProbeLetter,correctness="")

        # Display Fixation Cross (response window)
        startResponseFixationTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", units='pix',height=params['plusSize'],color="white")
        message.draw()
        if params['debug']:
            message2 = visual.TextStim(win, text="fixation cross (cue response window) for 1.5 sec.",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        win.flip()

        if c != "":
            correctness = "Correct" if c == rightAnswer else "Incorrect"
            # c = "Already answered"
            # core.wait(1.5)
            waitForSeconds(1.5)
        else:
            c,responseTime = WaitAndGetUserInput(c,1.5)
            if responseTime == "":
                responseTime = "No response"
                c = "No response"
            correctness = "Correct" if c == rightAnswer else "Incorrect"

        DataWrite(params=params, startTime=startResponseFixationTime, endTime=datetime.datetime.now(), trialCount=str(i+1),timingCount=timingFileCount,
                  trialType=trialLetter,
                  event="Fixation Displayed (Cue Response Window)",
                  timingFile=timingFile, userResponse=c, rightAnswer=rightAnswer,userResponseTime=responseTime,
                  userResponseOffset=0.5,cueLetter=CueLetter,probeLetter=ProbeLetter,correctness=correctness)

        # Display Fixation Cross (Delay Between Letters)
        startTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", units='pix',height=params['plusSize'],color="white")
        message.draw()
        if params['debug']:
            message2 = visual.TextStim(win, text="fixation cross (delay between letters) for "+str(delayBetweenLetters) +" sec.",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        win.flip()
        # core.wait(delayBetweenLetters)
        waitForSeconds(delayBetweenLetters)
        DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount=str(i+1),timingCount=timingFileCount,trialType=trialLetter,
                  event="Fixation Displayed (Delay Between Letters)",
                  timingFile=timingFile, userResponse="", rightAnswer="",userResponseTime="",
                  userResponseOffset=0,cueLetter="",probeLetter="",correctness="")

        # Display the second letter (probe)
        startProbeTime = datetime.datetime.now()
        rightAnswer = "Y" if trialLetter == "AX" else "N"

        # message = visual.TextStim(win, text=trialLetter[1],wrapWidth=2,units='norm',color="white",height=1.005)
        message = visual.TextStim(win, text=ProbeLetter, units='pix',height=params['fontSize'], color="white",
                                  font='arial',bold=True)
        message.draw()
        if params['debug']:
            message2 = visual.TextStim(win, text="second letter (probe) displayed for 0.5 sec",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        win.flip()
        c,responseTime = WaitAndGetUserInput([],0.5)
        if responseTime == "":
            responseTime = ""
            c = ""

        DataWrite(params=params, startTime=startProbeTime, endTime=datetime.datetime.now(), trialCount=str(i+1),timingCount=timingFileCount,trialType=trialLetter,
                  # event="Second Letter Displayed.("+str(trialLetter[1]) + ")",
                  event="Second Letter Displayed.(" + str(ProbeLetter) + ")",
                  timingFile=timingFile, userResponse=c, rightAnswer="",userResponseTime="",
                  userResponseOffset=0,cueLetter=CueLetter,probeLetter=ProbeLetter,correctness="")

        # Display Fixation Cross (response window)
        startResponseFixationTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", units='pix',height=params['plusSize'],color="white")
        message.draw()
        if params['debug']:
            message2 = visual.TextStim(win, text="fixation cross (probe response window) for 1.5 sec",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        win.flip()

        if c != "":
            correctness = "Correct" if c == rightAnswer else "Incorrect"
            # c = "Already answered"
            # core.wait(1.5)
            waitForSeconds(1.5)
        else:
            c,responseTime = WaitAndGetUserInput(c,1.5)
            if responseTime == "":
                responseTime = "No response"
                c = "No response"
            correctness = "Correct" if c == rightAnswer else "Incorrect"

        DataWrite(params=params, startTime=startResponseFixationTime, endTime=datetime.datetime.now(), trialCount=str(i+1),timingCount=timingFileCount,
                  trialType=trialLetter,
                  event="Fixation Displayed (Probe Response Window)",
                  timingFile=timingFile, userResponse=c, rightAnswer=rightAnswer,userResponseTime=responseTime,
                  userResponseOffset=0.5,cueLetter=CueLetter,probeLetter=ProbeLetter,correctness=correctness)

        # Display Fixation Cross (Delay Between Trials)
        startTime = datetime.datetime.now()
        message = visual.TextStim(win, text="+", units='pix',height=params['plusSize'],color="white")
        if params['debug']:
            message2 = visual.TextStim(win, text="fixation cross (delay between trials) for "+str(delayBetweenTrials) +" sec.",
                                       units='norm', wrapWidth=1000, color="red", pos=[0, 0.5])
            message2.draw()
        message.draw()
        win.flip()
        # core.wait(delayBetweenTrials)
        waitForSeconds(delayBetweenTrials)
        DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount=str(i+1),timingCount=timingFileCount,trialType=trialLetter,
                  event="Fixation Displayed (Delay Between Trials)",
                  timingFile=timingFile, userResponse="", rightAnswer="",userResponseTime="",
                  userResponseOffset=0,cueLetter="",probeLetter="",correctness="")

    timingFileCount += 1

message = visual.TextStim(win, text="Thank you!",
                          units='norm', wrapWidth=1000, color="white")
message.draw()
win.flip()
core.wait(2)
win.close()
