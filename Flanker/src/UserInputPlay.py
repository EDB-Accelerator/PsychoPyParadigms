from psychopy import gui

# Function to get user inputs.
def UserInputPlay():
    userInput = gui.Dlg(title="Flanker Task Information")
    userInput.addField('Version:', choices=[1])
    userInput.addField('Subject ID (SDAN):',)
    userInput.addField('Session:',)
    userInput.addField('The number of Blocks', 3, choices=[3, 2, 1])
    userInput.addField('The number of Trials',36,choices=[36,5,1])
    UserInputBank = userInput.show()

    params = {
        'expName': 'FlankerTask',  # The name of the experiment
        'Version': UserInputBank[0],  # Version
        'subjectID': UserInputBank[1],  # Subject ID
        'Session': UserInputBank[2],  # Session ID
        'nBlocks': UserInputBank[3],  # Session ID
        'nTrials': UserInputBank[4],  # Session ID
        'screenSize': [1024, 768], # Screen Resolution
    }

    return params