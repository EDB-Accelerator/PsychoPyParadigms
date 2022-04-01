import sys
sys.path.insert(1, './src')

from psychopy import core, visual
from Helper import WaitSeconds,WaitAndGetUserInput
from DictWrite import DictWrite
import datetime

def FlankerPlay(df,dict,TrialType,win,params,blockCount,trialCount):
    startTimeStr = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = datetime.datetime.now()

    if TrialType == "CL":
        displayedStr,flanker,direction = "<<<<<","Congruent","Left"
        correctAnswer,cellNumber = 4,4
    elif TrialType == "CR":
        displayedStr,flanker,direction = ">>>>>","Congruent","Right"
        correctAnswer,cellNumber = 2,4
    elif TrialType == "IR":
        displayedStr,flanker,direction = "<<><<","Incongruent","Right"
        correctAnswer,cellNumber = 2,5
    elif TrialType == "IL":
        displayedStr,flanker,direction = ">><>>","Incongruent","Left"
        correctAnswer,cellNumber = 4,5
    else:
        displayedStr = "Error"
        print('Image Type error at FlankerPlay.py. Exit')
        core.quit()

    # Display flanker image
    message = visual.TextStim(win, text=displayedStr,units='norm', wrapWidth=1000, color="white",height=0.3)
    message.draw()
    win.flip()
    WaitSeconds(0.2)
    c, userResponseTimeStamp = WaitAndGetUserInput([], 0.2)
    if userResponseTimeStamp == "":
        userResponse = "No response"
        correctness = ""
        userResponseTime = ""
    else:
        userResponse = c[0] if len(c) >= 0 else c
        correctness = "Correct" if userResponse == str(correctAnswer) else "Incorrect"
        userResponseTime = (userResponseTimeStamp - startTime).total_seconds()


    # Section Termination
    dict["Section"] = "Flanker Image Shown (0.2 sec)"
    dict["Start Time"] = startTimeStr
    dict["End Time"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    dict["Duration"] = datetime.datetime.now() - startTime
    dict["Block Count"] = str(blockCount)
    dict["Trial Count"] = str(trialCount)
    dict["Image Displayed"] = displayedStr
    dict["Flanker"] = flanker
    dict["Direction"] = direction
    dict["Correct Answer"] = correctAnswer
    dict["Cell Number"] = cellNumber
    dict["User Response"] = userResponse
    dict["Correct or Incorrect"] = correctness
    dict["User Response TimeStamp"] = userResponseTimeStamp
    dict["User Response Time"] = userResponseTime
    df,dict = DictWrite(df, dict, params)

    # Display User input Window (1.7 second)
    startTimeStr = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    startTime = datetime.datetime.now()
    message = visual.TextStim(win, text="", units='norm', wrapWidth=1000, color="white", height=0.3)
    message.draw()
    win.flip()

    if userResponseTimeStamp == "":
        c, userResponseTimeStamp = WaitAndGetUserInput([], 1.7)
        if userResponseTimeStamp == "":
            userResponse = "No response"
            correctness = ""
            userResponseTime = ""
        else:
            userResponse = c[0] if len(c)>=0 else c
            correctness = "Correct" if userResponse == str(correctAnswer) else "Incorrect"
            userResponseTime = (userResponseTimeStamp - startTime).total_seconds()
    else:
        userResponse = "Already Responded"
        correctness = ""
        userResponseTime = ""

    # Section Termination
    dict["Section"] = "Response Window (1.7 sec)"
    dict["Start Time"] = startTimeStr
    dict["End Time"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    dict["Duration"] = datetime.datetime.now() - startTime
    dict["Trial Count"] = str(trialCount)
    dict["Image Displayed"] = displayedStr
    dict["Flanker"] = flanker
    dict["Direction"] = direction
    dict["Correct Answer"] = correctAnswer
    dict["Cell Number"] = cellNumber
    dict["User Response"] = userResponse
    dict["Correct or Incorrect"] = correctness
    dict["User Response TimeStamp"] = userResponseTimeStamp
    dict["User Response Time"] = userResponseTime

    df,dict = DictWrite(df, dict, params)

    return df,dict