from psychopy import visual,core
import time,random,datetime,sys

# Import defined functions
sys.path.insert(1, './src')
from tableWrite import tableWrite,tableWriteRaw

# Header = ["Section Start Time","Section End Time","expName","subjectID","Session","Run","Block","TrialCount","Section",
#           "Image Displayed","Button Pressed","Button Response Time"]
# HeaderRaw = ["TimeStamp","expName","subjectID","Session","Event"]

def DisplayBlank(df,dfRaw,params,dict,dictRaw,win):

    blankTime = [0,2,4]
    blankDuration = random.choice(blankTime)

    # Record status
    dict["Section Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Section"] = "DisplayBlank"
    dict["Image Displayed"] = "Blank for " + str(blankDuration) + " sec"
    dict["Button Pressed"] = ""
    dict["Button Correct/Incorrect"] = ""
    dict["Button Response Time"] = ""
    dictRaw["Event"] = dict["Image Displayed"] + "shown (start)"
    dfRaw = tableWriteRaw(dfRaw, dictRaw)

    # fixation = visual.ShapeStim(win, lineColor='#000000', lineWidth=0, vertices=(
    #     (0,0), (0,1)), units='height', closeShape=False,
    #                              name='fixCross');
    # fixation.draw()
    win.flip()
    core.wait(blankDuration)

    # Record status
    dict["Section End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dictRaw["Event"] = dict["Image Displayed"] + " shown (end)"
    dfRaw = tableWriteRaw(dfRaw, dictRaw)

    return tableWrite(df,params,dict),dfRaw
