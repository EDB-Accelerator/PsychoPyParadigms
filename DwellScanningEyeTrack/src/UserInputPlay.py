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

from psychopy import gui
import os

# Function to get user inputs.
def UserInputPlay():
    userInput = gui.Dlg(title="Dwell Task Information")
    userInput.addField('Subject ID:',)
    userInput.addField('Session:',)
    if os.path.isfile('.tmp/version2Lock.txt'):
        userInput.addField('Version:', choices=[2])
    else:
        # userInput.addField('Version:',choices=[3,4])
        userInput.addField('Version:', choices=['Green', 'Blue'])
    userInput.addField('# of trials per block (** there are 3 blocks):', choices=["default (30)","5","3","1"])
    userInput.addField('Full Screen', True)
    if os.path.isfile('.tmp/version2Lock.txt'):
        # userInput.addField('Resolution:', choices=[[1024,768],[1920,1080]])
        userInput.addField('Resolution:', choices=[[1024, 768]])
    else:
        # userInput.addField('Resolution:', choices=[[1920, 1080],[1024,768]])
        userInput.addField('Resolution:', choices=[[1024, 768]])
    userInput.addField('Which eye will be used?:', choices=["LEFT","RIGHT","BOTH"])
    userInput.addField('EyeTrack Circle', False)
    userInput.addField('EyeLink Support',True)
    # userInput.addField('Face Matrix Duration', 6)
    # userInput.addField('Music Folder:','./music')

    return userInput.show()

def UserInputPlayTwoThree():
    userInput = gui.Dlg(title="Dwell Task Training Information")
    userInput.addField('Week:', choices=[4,5,6,7,8,9,10,11,12])

    return userInput.show()