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

# Import standard python libraries
import pandas as pd
import glob
import re

inFiles = glob.glob('./script/input/*.csv')


for i in range(len(inFiles)):
# i = 0
    inFile = inFiles[i]

    df = pd.read_csv(inFile)
    answers = [3,5,3,4,2,4,5,2,4,3,1,3,1,2,3,1,1,4,4,2,5,3,1,4]
    df["Correct Answer"] = ""
    df["User Answer Correctness"] = ""
    count = 0
    correctAnswers = []
    correctness = []
    for index, row in df.iterrows():
        # print(row['c1'], row['c2'])
        # print(index)

        if "Test:" in row['Section'] or "Practice try" in row['Section']:
            # print(row['Section'])
            txt = row['Section']
            if "Practice try" in row['Section']:
                answer = "1"
            else:
                i = int(re.findall(r'\d+', txt)[0])-1
                answer = answers[i]
            if row["User Answer"] != "1" and row["User Answer"] != "2" and row["User Answer"] != "3" and row["User Answer"] != "4"\
                and row["User Answer"] != "5" and row["User Answer"] != "6":
                correctness.append("")
                correctAnswers.append("")
            else:
                correct = "Correct" if str(row["User Answer"]) == str(answer) \
                    else "Incorrect"
                correctAnswers.append(str(answer))
                correctness.append(correct)
                count += 1
        else:
            correctAnswers.append("")
            correctness.append("")

    df["Correct Answer"] = correctAnswers
    df["User Answer Correctness"] = correctness

    columns = ['SubjectID', 'expName', 'Session', 'Section', 'Section Start Time',
           'Section End Time', 'Section Time', 'Response Time', 'User Answer','Correct Answer', 'User Answer Correctness',
               'Image Group', 'Image Count',
           'Image Displayed #1', 'Image Displayed #2', 'Image Displayed #3',
           'Image Displayed #4', 'Image Displayed #5', 'Image Displayed #6'
           ]
    df = df[columns]

    outFile = inFile.replace('input','output')
    outFile = outFile.replace('.csv','_fixed.csv')

    df.to_csv(outFile,index=False)