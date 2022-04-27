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

# Function to get user inputs.
def PlayUserInputGUI():
    from psychopy import prefs, gui
    import datetime

    userInput = gui.Dlg(title="AXCPT task Information")
    userInput.addField('Subject ID:',)
    userInput.addField('Session:',)
    userInput.addField('# of trials per block (** there are 3 blocks):', choices=["default","5","3","1"])
    userInput.addField('Full Screen', True)
    userInput.addField('Debug',False)
    userInput.addField('Font Size (pixel)', 200)
    userInput.addField('+ Size (pixel)', 72)


    UserInputBank = userInput.show()

    # Declare primary task parameters.
    params = {
        'expName' : 'AXCPT', # The name of this experiment
        'subjectID' : UserInputBank[0],      # Subject ID
        'Session' : UserInputBank[1], # Session ID
        'numTrial': UserInputBank[2],  # The number of Trials.
        'fullscr': UserInputBank[3],  # The resolution of Psychopy Window
        'debug' : UserInputBank[4], # Debugging mode
        'fontSize': UserInputBank[5],
        'plusSize': UserInputBank[6],

        'timingFile' : "",
    }

    if params['numTrial'] == 'default':
        params['numTrial'] = 40
    else:
        params['numTrial'] = int(params['numTrial'])

    timeLabel = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
    prefs.general['fullscr'] = params['fullscr']
    params['outFile'] = "result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
              "_"+timeLabel + "_all.csv"
    params['outFile1'] = "result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) + \
                        "_" + timeLabel + "_block1.csv"
    params['outFile2'] = "result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) + \
                        "_"+ timeLabel + "_block2.csv"
    params['outFile3'] = "result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) + \
                        "_"+ timeLabel + "_block3.csv"
    params['outFile4'] = "result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) + \
                        "_"+ timeLabel + "_block4.csv"
    params['outFile5'] = "result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) + \
                         "_"+ timeLabel + "_block5.csv"
    params['outFile6'] = "result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) + \
                         "_"+ timeLabel + "_block6.csv"

    return params
