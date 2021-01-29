from psychopy import gui
# Function to get user inputs.
def UserInputPlay():
    userInput = gui.Dlg(title="DOORS Task Information")
    userInput.addField('SDAN:',)
    userInput.addField('Session:',1)
    userInput.addField('# of Run1 trials:', 30)
    userInput.addField('# of Run2 trials:', 30)
    return userInput.show()