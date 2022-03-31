import sys
sys.path.insert(1, './src')

from psychopy import core, visual, event
from Helper import WaitUserSpace
from DictWrite import DictWrite
import datetime

def InstructionPlay(df,dict,win,params):
    startTimeStr = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = datetime.datetime.now()

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
        if userInput == ['q'] or userInput == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()

    # Introduction
    while (userInput[0].upper() == 'Y'):
        # Introduction Slide 1
        message = visual.TextStim(win, text="Please press the button that matches\n"
                                            "the direction of the middle arrow.\n" +
                                            "\n"
                                            "For < press the left button\n" +
                                            "For > press the right button.\n\n\n\n\n" +
                                            "Please SPACE BAR to continue",
                                  units='norm', wrapWidth=1000, color="white")
        message.draw()
        win.flip()
        WaitUserSpace(win)

        # Introduction Slide 2
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

    # Section Termination
    dict["Section"] = "Instruction"
    dict["Start Time"] = startTimeStr
    dict["End Time"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    dict["Duration"] = datetime.datetime.now() - startTime
    df,dict = DictWrite(df,dict,params)

    return df,dict
