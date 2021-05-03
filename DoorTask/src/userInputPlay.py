from psychopy import gui

# Function to get user inputs.
def userInputPlay():
    userInput = gui.Dlg(title="DOORS Task Information")
    userInput.addField('Subject Number:',23986)
    userInput.addField('Session:',1)
    userInput.addField('Version:', choices=[1, 2])
    userInput.addField('# of Practice Trials:', 5)
    userInput.addField('# of TaskRun1:', 49)
    userInput.addField('# of TaskRun2:', 49)
    userInput.addField('# of TaskRun3:', 49)
    userInput.addField('Trigger Support:', True)
    userInput.addField('Eyetracker Support:', True)
    userInput.addField('Full Screen', True)
    # userInput.addField('Resolution', (1024,780))
    return userInput.show()