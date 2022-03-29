import sys
sys.path.insert(1, './src')

from psychopy import core, visual, event
import time
from Helper import WaitSeconds
# from Helper import ,tableWrite,get_keypress
from Helper import get_keypress,WaitUserSpace
import datetime

def FlankerPlay(df,iti,dict,dictRaw,TrialType,win,params):
    Dict = {
        "ExperimentName": params['expName'],
        "Subject": params['subjectID'],
        "Session": params["Session"],
        "Version": params["Version"],
        "Trial Type": TrialType,
        "Section": "Flanker play",
        "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S"),
    }

    imgCONGL = 'img/CONGL.jpg'

    if TrialType == "CL":
        displayedStr = "<<<<<"
        flanker = "Congruent"
    elif TrialType == "CR":
        displayedStr = ">>>>>"
        flanker = "Congruent"
    elif TrialType == "IR":
        displayedStr = "<<><<"
        flanker = "Incongruent"
    elif TrialType == "IL":
        displayedStr = ">><>>"
        flanker = "Incongruent"
    else:
        displayedStr = "Error"
        print('imageType error at Flankerplay. Exit')
        core.quit()
    Dict[displayedStr] = displayedStr
    Dict[flanker] = flanker

    message = visual.TextStim(win, text=displayedStr,units='norm', wrapWidth=1000, color="white",height=0.3)
    message.draw()
    win.flip()
    core.wait(0.2)

    # Display User input Window (1.7 second)
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
    if c == ['q'] or c == ['Q']:
        print('Q pressed. Forced Exit.')
        core.quit()
    if len(c) >= 1:
        c = c[0]
    else:
        c = "No Response"

    ### Fixation Cross (for 1.9 seconds) ###
    startTime = datetime.datetime.now()
    message = visual.TextStim(win, text="+", units='pix',height=params['plusSize'],color="white")
    if params['debug']:
        message2 = visual.TextStim(win, text="Fixation Cross (1.9 seconds)",
                                  units='norm', wrapWidth=1000, color="red",pos=[0,0.5])
        message2.draw()
    message.draw()
    win.flip()
    c = ['']
    WaitSeconds(1.9)    # Wait for 1.9 seconds.
