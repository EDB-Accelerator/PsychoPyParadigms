import sys
sys.path.insert(1, './src')

from psychopy import core, visual, event
from Helper import WaitSeconds
from DictWrite import DictWrite
import datetime

def ReadyPlay(df,dict,win,params,blockCount):
    # Initialization
    startTimeStr = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = datetime.datetime.now()

    # Display the message
    message = visual.TextStim(win, text="Waiting for scanner \n\n(Please press 5 when it is ready.)",
                              units='norm', wrapWidth=1000, color="white")
    message.draw()
    win.flip()
    userInput = ['']

    # Wait for user types "y" or "n".
    while (userInput[0].upper() != "5"):
        core.wait(1 / 120)
        userInput = event.waitKeys()  # read a characters
        if userInput == ['q'] or userInput == ['Q']:
            print('Q pressed. Forced Exit.')
            core.quit()

    # Section Termination
    dict["Section"] = "Waiting for scanner"
    dict["Start Time"] = startTimeStr
    dict["End Time"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    dict["Duration"] = datetime.datetime.now() - startTime
    df,dict = DictWrite(df,dict,params)

    # Initialization
    startTimeStr = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = datetime.datetime.now()

    # Get Ready screen.
    message = visual.TextStim(win, text="Get Ready",
                              units='norm', wrapWidth=1000, color="white")
    message.draw()
    win.flip()
    WaitSeconds(8)

    # Section Termination
    dict["Section"] = "Get Ready Screen"
    dict["Start Time"] = startTimeStr
    dict["End Time"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    dict["Duration"] = datetime.datetime.now() - startTime
    df,dict = DictWrite(df, dict, params)

    return df,dict
