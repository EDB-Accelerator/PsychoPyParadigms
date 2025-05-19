from psychopy import gui

# Function to get user inputs.
def userInputPlay():
    userInput = gui.Dlg(title="DOORS Task Information")
    userInput.addField('Subject Number:',)
    userInput.addField('Session:',1)
    userInput.addField('Version:', 3,choices=[3])
    userInput.addField('# of Practice Trials:', 5)
    userInput.addField('# of TaskRun1:', 25)
    userInput.addField('# of TaskRun2:', 25)
    userInput.addField('# of TaskRun3:', 24)
    # userInput.addField('Trigger Support:', True)
    # userInput.addField('Eyetracker Support:', choices=[False])
    userInput.addField('Full Screen', True)
    userInput.addField('Joystick Sensitivity (0: very sensitive, 1: normal, 2: less sensitive, 3: No joystick support', 2, choices=[0,1,2,3])
    # userInput.addField('Eyetracker Circle', True)
    userInput.addField('Sound Mode:',choices=['PTB','Others'])
    userInput.addField('Heat Support:', True)
    userInput.addField('Heat1:', 34.0)
    userInput.addField('Heat2:', 36.0)
    userInput.addField('Heat3:', 38.0)
    userInput.addField('Heat4:', 40.0)
    userInput.addField('Heat5:', 42.0)
    userInput.addField('Heat6:', 44.0)
    userInput.addField('Heat7:', 46.0)
    userInput.addField("Reward Screen Time:", 6.5)

    # userInput.addField('Trigger Support:', True)

    return userInput.show()