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
    userInput.addField('Yes Key', 2)
    userInput.addField('No Key', 4)

    UserInputBank = userInput.show()

    # # Declare primary task parameters.
    # params = {
    #     'expName' : 'AXCPT', # The name of this experiment
    #     'subjectID' : UserInputBank[0],      # Subject ID
    #     'Session' : UserInputBank[1], # Session ID
    #     'numTrial': UserInputBank[2],  # The number of Trials.
    #     'fullscr': UserInputBank[3],  # The resolution of Psychopy Window
    #     'debug' : UserInputBank[4], # Debugging mode
    #     'fontSize': UserInputBank[5],
    #     'plusSize': UserInputBank[6],
    #     'yesKey':str(UserInputBank[7]),
    #     'noKey': str(UserInputBank[8]),
    #
    #     'timingFile' : "",
    # }
    return UserInputBank
