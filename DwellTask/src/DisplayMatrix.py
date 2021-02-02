from psychopy import visual,event,core
import time,random,datetime,sys

# Import defined functions
sys.path.insert(1, './src')
from tableWrite import tableWrite,tableWriteRaw

# Header = ["Section Start Time","Section End Time","expName","subjectID","Session","Run","Block","TrialCount","Section",
#           "Image Displayed","Button Pressed","Button Response Time"]
# HeaderRaw = ["TimeStamp","expName","subjectID","Session","Event"]

def DisplayMatrix(df,dfRaw,img,params,dict,dictRaw,win):
    imgStim = visual.ImageStim(win=win, image=img, units="pix", opacity=1, size=params['screenSize'])
    imgStim.draw()
    win.flip()

    # Record status
    dict["Section Start Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dict["Section"] = "DisplayMatrix"
    dict["Image Displayed"] = img
    dict["Button Pressed"] = ""
    dict["Button Correct/Incorrect"] = ""
    dict["Button Response Time"] = ""
    dictRaw["Event"] = str(img) + " shown (start)"
    dfRaw = tableWriteRaw(dfRaw, dictRaw)

    # Wait for 6 seconds
    core.wait(6)

    # Record status
    dict["Section End Time"] = datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    dictRaw["Event"] = str(img) + " shown (end)"
    dfRaw = tableWriteRaw(dfRaw, dictRaw)

    return tableWrite(df,params,dict),dfRaw
