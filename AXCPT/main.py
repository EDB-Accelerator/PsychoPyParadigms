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
from psychopy import visual,core
import pandas as pd
import glob

# Import developer-defined functions
sys.path.insert(1, './src')
from PlayUserInputGUI import PlayUserInputGUI





UserInputBank = PlayUserInputGUI()

# Declare primary task parameters.
params = {
    'expName' : 'AXCPT', # The name of this experiment
    'subjectID' : UserInputBank[0],      # Subject ID
    'Session' : UserInputBank[1], # Session ID
    'numTrial': UserInputBank[2],  # The number of Trials.
    'fullscr': UserInputBank[3],  # The resolution of Psychopy Window
}

if params['numTrial'] == 'default':
    params['numTrial'] = 40
else:
    params['numTrial'] = int(params['numTrial'])

# Import dependencies.
import sys
from psychopy import visual,core
import pandas as pd
import glob

# Import developer-defined functions
sys.path.insert(1, './src')
from PlayUserInputGUI import PlayUserInputGUI

def WaitUserSpace():
    from psychopy import core, event
    # Wait for user types a space key.
    c = ['']
    while (c[0] != 'space'):
        core.wait(1 / 120)
        c = event.waitKeys()  # read a character

        if c == ['q'] or c == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()

# Welcome Screen
win = visual.Window(monitor="testMonitor", color="black", winType='pyglet')
win.mouseVisible = False
message = visual.TextStim(win,text="Welcome!\n\n"+
                          "Please remember the task where we ask you to\n"+
                          "remember a series of letters\n\n\n\n\n\n\n"+
                          "Please press SPACE to see an example.",
                                  units='pix', wrapWidth=1000, color="white",height=25)
message.draw()
win.flip()
WaitUserSpace()

# Introduction
message = visual.TextStim(win,text="The task sequence looks like:",
                                  units='pix', wrapWidth=1000, color="white",height=25,pos=[0,250])
message.draw()
win.flip()
WaitUserSpace()

for i in range(3):
    imgFile = "resource/img/intro" + str(i) + ".JPG"
    img1 = visual.ImageStim(win=win, image=imgFile, units="pix", opacity=1)
    img1.draw()
    message.draw()
    win.flip()
    WaitUserSpace()

# Introduction Slide 2
message = visual.TextStim(win,text="Press the YES (index) key as quickly as you can when you see the\n"+
                          "blue letter that completes the target sequence. Press the NO\n"+
                          "(middle) key as quickly as you can for all other letters.\n\n\n\n\n"+
                          "Please Space Bar to continue",
                                  units='pix', wrapWidth=1000, color="white",height=25)
message.draw()
win.flip()
WaitUserSpace()

# Introduction Slide 3
message = visual.TextStim(win,text="Are you ready to start the task\n"
                                   "or\n"
                                   "should we review the instructions again?",
                                  units='pix', wrapWidth=1000, color="white",height=25)
message.draw()
win.flip()
WaitUserSpace()







timingFiles = glob.glob('timing/*.csv')
timingFile = timingFiles[0]
numTrial = int(params['numTrial'])
dfTiming = pd.read_csv(timingFile,header=None,names=['Trial Type','Delay Between Letters', 'Delay Between Trials'])

for i in range(numTrial):

    # ITI
    message = visual.TextStim(win, text="+", wrapWidth=2,color="black")
    message.draw()
    win.flip()

    core.wait(2)

    # Get Letter type
    trialLetter = dfTiming.iloc[i]['Trial ' \
                                   'Type']

    # Display the first letter
    message = visual.TextStim(win, text=trialLetter[0],
                              units='norm', wrapWidth=2, color="black")
    message.draw()
    win.flip()
    core.wait(0.5)

    # Display the second letter
    message = visual.TextStim(win, text=trialLetter[1],
                              units='norm', wrapWidth=2, color="black")
    message.draw()
    win.flip()
    core.wait(0.5)

# message.draw()
# win.flip()
# core.wait(3)
# win.close()
#
#
