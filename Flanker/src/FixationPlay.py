import sys
sys.path.insert(1, './src')

from psychopy import core, visual, event
from Helper import WaitSeconds
from DictWrite import DictWrite
import datetime

def FixationPlay(df,dict,win,params,blockCount,trialCount,iti):
    # Initialization
    startTimeStr = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = datetime.datetime.now()

    # Display the message
    message = visual.TextStim(win, text="+", wrapWidth=2,units='norm',color="white",height=0.3)
    message.draw()
    win.flip()
    WaitSeconds(iti)

    # Section Termination
    dict["Section"] = "Fixation Screen"
    dict["Start Time"] = startTimeStr
    dict["Block Count"] = str(blockCount)
    dict["Trial Count"] = trialCount
    dict["End Time"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    dict["Duration"] = datetime.datetime.now() - startTime
    df,dict = DictWrite(df, dict, params)

    return df,dict
