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

import pandas as pd
import datetime

def tableWriteRaw(Df, Dict):

    # Move data in Dict into Df.
    Df = Df.append(pd.Series(dtype=float), ignore_index=True)  # Insert Empty Rows
    Dict["TimeStamp"] =datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    for key in Dict:
        Df[key].loc[len(Df) - 1] = Dict[key]  # FYI, len(Df)-1: means the last row of pandas dataframe.
    return Df

def tableWrite(df,params,dict):

    # Move data in Dict into Df.
    df = df.append(pd.Series(dtype=float), ignore_index=True)  # Insert Empty Rows
    dict["Run"] = params["Run"]
    dict["Block"] = params["Block"]
    dict["TrialCount"] = params["TrialCount"]
    for key in dict:
        df[key].loc[len(df) - 1] = dict[key]  # FYI, len(Df)-1: means the last row of pandas dataframe.
    return df
