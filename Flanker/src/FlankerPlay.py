import sys
sys.path.insert(1, './src')

from psychopy import core, visual, event
import time
# from Helper import ,tableWrite,get_keypress
from Helper import get_keypress,WaitUserSpace
import datetime

def FlankerPlay(df,dict,dictRaw,imageType,win,params):
    Dict = {
        "ExperimentName": params['expName'],
        "Subject": params['subjectID'],
        "Session": params["Session"],
        "Version": params["Version"],
        "Section": "Instructions",
        "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S"),
    }

    imgCONGL = 'img/CONGL.jpg'

    if imageType=="CONGL":
        displayedStr = "<<<<<"
    elif imageType=="CONGR":
        displayedStr = ">>>>>"
    elif imageType=="INCONGR":
        displayedStr = "<<><<"
    elif imageType=="INCONGR":
        displayedStr = ">><>>"
    else:
        displayedStr = "Error"

    message = visual.TextStim(win, text=displayedStr,units='norm', wrapWidth=1000, color="white",height=0.3)
    message.draw()
    win.flip()

    # messageCONGL=visual.TextStim(win, text="<<<<<",units='norm', wrapWidth=1000, color="white",height=0.3)
    # messageCONGR= visual.TextStim(win, text=">>>>>",units='norm', wrapWidth=1000, color="white",height=0.3)
    # messageINCONGR= visual.TextStim(win, text="<<><<",units='norm', wrapWidth=1000, color="white",height=0.3)
    # messageINCONGL= visual.TextStim(win, text=">><>>",units='norm', wrapWidth=1000, color="white",height=0.3)
    # Response Window
    # Get user input.
    c = []
    startTime = time.time()
    dict["Start Time"] = datetime.datetime.now().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    event.clearEvents()
    while time.time() - startTime < 1.7:
        core.wait(1 / 120)
        if c == []:
            c = event.getKeys()
        if len(c) >= 1:
            dictRaw["Event"] = "User Response:" + c[0]
            # DictWriteRaw(dfRaw, dictRaw, params)
    if c == ['q'] or c == ['Q']:
        print('Q pressed. Forced Exit.')
        core.quit()
    if len(c) >= 1:
        c = c[0]
    else:
        c = "No Response"