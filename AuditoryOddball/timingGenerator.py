# Python3-based package
"""
MIT License

Copyright (c) 2021 NIMH

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
"""
@author: Kyunghun Lee
- Created on Thu, Sep 30, 2021  2:01:52 PM by KL
"""

# Import dependencies.
import pandas as pd
import datetime
import numpy as np
import random

def recordStimuli(df,timestamp,duration,stimuli):
    # df.loc[] = [timestamp,duration,stimuli]
    # df.index = df.index + 1  # shifting index
    df2 = {'Time Stamp (start)': timeStamp,'Duration':duration,'Stimuli':stimuli}
    df = df.append(df2, ignore_index=True)
    return df

for numFile in range(6):

    numOfSets = 6
    numTrials = 100
    headers = ['Time Stamp (start)','Duration','Stimuli']
    delays = np.arange(1, 3.25, 0.25).tolist()
    delays = delays * 18
    random.shuffle(delays[len(np.arange(1, 3.25, 0.25).tolist())*17:])
    # delays = delays[:165]
    random.shuffle(delays)

    numStandards = [3,4,5]
    numStandards = numStandards * 10
    random.shuffle(numStandards)
    # numStandards.pop()
    print(len(numStandards))

    novelDeviants = ['n','d']
    novelDeviants = novelDeviants * 14
    random.shuffle(novelDeviants)

    # Pandas dataframe Initialization
    df = pd.DataFrame(columns=headers)

    timeStamp = 0
    standardCount = 0
    delayCount = 0

    # 20 seconds no sound
    df = recordStimuli(df, 0, 20, "No sound (20 seconds)")
    timeStamp += 20

    for j in range(10):
        df = recordStimuli(df, timeStamp, 0.2, "Standard (" + str(standardCount + 1) + ") presented")
        standardCount += 1
        timeStamp += 0.2

        delay = delays.pop() - 0.2
        df = recordStimuli(df, timeStamp, delay, "interval")
        timeStamp += delay
        delayCount += 1

    for i in range(28):
        numStandard = numStandards.pop()
        for j in range(numStandard):
            df = recordStimuli(df, timeStamp, 0.2, "Standard (" + str(standardCount+1) + ") presented")
            standardCount += 1
            timeStamp += 0.2

            delay = delays.pop() - 0.2
            df = recordStimuli(df, timeStamp, delay, "interval")
            timeStamp += delay
            delayCount += 1
        novelDeviant = novelDeviants.pop()
        if novelDeviant == 'n':
            df = recordStimuli(df, timeStamp, 0.2, "Novel presented")
            timeStamp += 0.2
        else:
            df = recordStimuli(df, timeStamp, 0.2, "Deviant presented")
            timeStamp += 0.2
        delay = delays.pop() - 0.2
        df = recordStimuli(df, timeStamp, delay, "interval")
        timeStamp += delay
        delayCount += 1

    # 10 standards after each run.
    for j in range(10):
        df = recordStimuli(df, timeStamp, 0.2, "Standard (" + str(standardCount + 1) + ") presented")
        standardCount += 1
        timeStamp += 0.2

        delay = delays.pop() - 0.2
        df = recordStimuli(df, timeStamp, delay, "interval")
        timeStamp += delay
        delayCount += 1

    # 20 seconds no sound
    df = recordStimuli(df, 0, 20, "No sound (20 seconds)")
    timeStamp += 20


    df.to_csv("./timing/" + str(numFile) + ".csv", mode='w', sep=',', encoding='utf-8')

