import sys
sys.path.insert(1, './src')

from psychopy import core, visual, event
# from Helper import ,tableWrite,get_keypress
from Helper import get_keypress,WaitUserSpace
import datetime

def InstructionPlay(df, win, params):
    Dict = {
        "ExperimentName": params['expName'],
        "Subject": params['subjectID'],
        "Session": params["Session"],
        "Version": params["Version"],
        "Section": "Instructions",
        "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S"),
    }

    # Display Instruction
    message = visual.TextStim(win, text="Do you want to see the instruction?\n\n(y: Yes, n: No)",
                              units='norm', color='white',wrapWidth=3)
    message.draw();
    win.flip();
    c = ['']

    # Wait for user types "y" or "n".
    userInput = ['0']
    while (userInput[0].upper() != "Y" and userInput[0].upper() != "N"):
        core.wait(1 / 120)
        userInput = event.waitKeys()  # read a characters
        # print(userInput)
        if userInput == ['q'] or userInput == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()

    # Introduction
    while (userInput[0].upper() == 'Y'):
        # Introduction Slide 2
        message = visual.TextStim(win, text="Please press the button that matches the direction of the middle arrow.\n" +
                                            "\n"
                                            "For < press the left button\n" +
                                            "For > press the right button.\n\n\n\n\n" +
                                            "Please SPACE BAR to continue",
                                  units='norm', wrapWidth=1000, color="white")
        message.draw()
        win.flip()
        WaitUserSpace(win)

        # Introduction Slide 3
        message = visual.TextStim(win, text="Are you ready to start the task?\n\n"
                                            "or\n\n"
                                            "should we review the instructions again?\n\n\n"
                                            "Press Y to review / Press N if ready to start",
                                  units='norm', wrapWidth=1000, color="white")
        message.draw()
        win.flip()
        userInput = ['']
        # Wait for user types "y" or "n".
        while (userInput[0].upper() != "Y" and userInput[0].upper() != "N"):
            core.wait(1 / 120)
            userInput = event.waitKeys()  # read a characters
            # print(userInput)
            if userInput == ['q'] or userInput == ['Q']:
                print('Q pressed. Forced Exit.')
                core.quit()

    # Log the dict result on pandas dataFrame.
    return tableWrite(df, params,Dict)
