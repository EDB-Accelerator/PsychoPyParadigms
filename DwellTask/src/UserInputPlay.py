from psychopy import gui
# Function to get user inputs.
def UserInputPlay():
    userInput = gui.Dlg(title="DOORS Task Information")
    userInput.addField('Subject ID:',)
    userInput.addField('Session:',1)
    userInput.addField('# of Run trials:', 2)
    return userInput.show()