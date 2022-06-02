import sys
sys.path.insert(1, './src')

import datetime
import subprocess as subp
from psychopy import visual
from Helper import waitUserSpace, tableWrite

def FortuneGamePlay(Df, win,params,SectionName,gameResult):
    Dict = {
        "Section": SectionName,
        "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S"),
    }

    win.close()
    if gameResult == 18:
        subp.check_call("runFortuneWheel18.bat", shell=True)
        win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
        message = visual.TextStim(win,
                                  text="You have won $18.\n\nPress the spacebar when you are ready to keep playing.",
                                  units='norm', wrapWidth=2)
    elif gameResult == 16:
        subp.check_call("runFortuneWheel16.bat", shell=True)
        win = visual.Window(params['screenSize'], monitor="testMonitor", color="black", winType='pyglet')
        message = visual.TextStim(win,
                                  text="You have won $16.\n\nPress the spacebar when you are ready to keep playing.",
                                  units='norm', wrapWidth=2)
    message.draw()
    win.flip()
    waitUserSpace(Df, params)

    return tableWrite(Df, params,Dict),win
