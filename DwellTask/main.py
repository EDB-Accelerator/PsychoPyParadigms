# Python3-based package
"""
DwellTask.py

DwellTask Psychopy3 Main Driver File.

Created on Thu Jan 28 15:20:30 EST 2021

@author: Kyunghun Lee
- Created on Thu Jan 28 15:20:30 EST 2021 by KL
"""

# Import all necessary standard python library
import datetime,os,sys,time,random
import pandas as pd
from psychopy import visual,core,event,parallel,prefs,gui
from glob import glob

# Import defined functions
sys.path.insert(1, './src')
from UserInputPlay import UserInputPlay
from DictInitialize import DictInitialize
from DisplayFixationCross import DisplayFixationCross
from DisplayMatrix import DisplayMatrix
from DisplayBlank import DisplayBlank

pd.set_option('display.max_columns', None)
# Receive User input from Window.
UserInputBank = UserInputPlay()
# Declare primary task parameters.
params = {
    'expName' : 'DwellTask', # The name of the experiment
    'subjectID' : UserInputBank[0],      # Subject ID
    'Session' : UserInputBank[1], # Session ID
    'BlockNum' : 3,
    'RunNum' : 2,
    'screenSize' : (1024,780),
    'numTrial': UserInputBank[2],  # The number of Trials.
    # "TrialCount" : 1,
}

# Instance result initialization
dict,dictRaw = DictInitialize(params)

# Open Window.
win = visual.Window(params['screenSize'],monitor="testMonitor",color="white",winType='pyglet')

# Make image list and Shuffle.
RunList = glob('./img/*')
random.shuffle(RunList)

# BlockList = [glob('./img/Anger-Neutral/*'),glob('./img/Disgust-Neutral/*')]
# DataFrame (Recording) Intialization.
Header = ["Section Start Time","Section End Time","expName","subjectID","Session","Run","Block","TrialCount","Section",
          "Image Displayed","Button Pressed","Button Correct/Incorrect","Button Response Time"]
HeaderRaw = ["TimeStamp","expName","subjectID","Session","Event"]
df = pd.DataFrame(columns=Header)
dfRaw = pd.DataFrame(columns=HeaderRaw)

for run in RunList:
    params["Run"] = run.split('/')[-1]
    # Get Block list and Shuffle.
    BlockList = glob(run + '/*')
    random.shuffle(BlockList)

    for block in BlockList:
        params["Block"] = block.split('/')[-1]
        # Get Image list of each block and Shuffle.
        ImgList = glob(block + '/*.jpeg')
        random.shuffle(ImgList)
        for trial in range(params['numTrial']):
            params["TrialCount"] = trial
            img = ImgList[trial]

            # Fixation cross section
            df,dfRaw = DisplayFixationCross(df=df,dfRaw=dfRaw,params=params,dict=dict,dictRaw=dictRaw,win=win)
            df,dfRaw = DisplayMatrix(df=df,dfRaw=dfRaw,img=img,params=params,dict=dict,dictRaw=dictRaw,win=win)
            df,dfRaw = DisplayBlank(df=df,dfRaw=dfRaw,params=params,dict=dict,dictRaw=dictRaw,win=win)

outFile = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
          datetime.datetime.now().strftime("%m%d%Y_%H%M%S") + ".csv"
outFileRaw = "./result/" + params["expName"] + "_" + str(params["subjectID"]) + "_" + str(params["Session"]) +\
          datetime.datetime.now().strftime("%m%d%Y_%H%M%S") + "_raw.csv"

df.to_csv(outFile, sep=',', encoding='utf-8', index=False)
dfRaw.to_csv(outFileRaw, sep=',', encoding='utf-8', index=False)

# Close the psychopy window.
win.close()
