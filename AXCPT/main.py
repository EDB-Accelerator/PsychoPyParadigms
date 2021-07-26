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

if params['numTrial'] is 'default':
    params['numTrial'] = 40
else:
    params['numTrial'] = int(params['numTrial'])


win = visual.Window(monitor="testMonitor", color="white", winType='pyglet')
win.mouseVisible = False
message = visual.TextStim(win,text="Thank you so much!\n ",
                                  units='norm', wrapWidth=2, color="black")
message.draw()
win.flip()

timingFile = "timing/file01.csv"
numTrial = int(params['numTrial'])
dfTiming = pd.read_csv(timingFile,header=None,names=['Trial Type','Delay Between Letters', 'Delay Between Trials'])


for i in range(numTrial):
    print(i)




# message.draw()
# win.flip()
# core.wait(3)
# win.close()
#
#
