import sys
sys.path.insert(1, './src')

from psychopy import core, visual, event
from Helper import WaitSeconds
from DictWrite import DictWrite
import datetime

def BlankPlay(df,dict,win,params,blockCount,trialCount):
    # Initialization
    startTimeStr = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = datetime.datetime.now()

    # Display the message
    message = visual.TextStim(win, text="", wrapWidth=2,units='norm',color="white")
    message.draw()
    win.flip()
    WaitSeconds(0.5)

    # Section Termination
    dict["Section"] = "Blank Screen"
    dict["Start Time"] = startTimeStr
    dict["Trial Count"] = trialCount
    dict["End Time"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    dict["Duration"] = datetime.datetime.now() - startTime
    dict["Block Count"] = str(blockCount)
    df,dict = DictWrite(df, dict, params)

    return df,dict
