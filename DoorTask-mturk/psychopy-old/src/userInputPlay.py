from psychopy import gui

# Function to get user inputs.
def userInputPlay():
    userInput = gui.Dlg(title="DOORS Task Information")
    userInput.addField('Subject Number:',)
    userInput.addField('Session:',1)
    userInput.addField('Version:', choices=[1, 2])
    userInput.addField('# of Practice Trials:', 5)
    userInput.addField('# of TaskRun1:', 49)
    userInput.addField('# of TaskRun2:', 49)
    userInput.addField('# of TaskRun3:', 49)
    userInput.addField('Full Screen', True)
    # userInput.addField('Eyetracker Circle', True)
    # userInput.addField('Sound Mode:',choices=['PTB','Others'])
    return userInput.show()