import pandas as pd
import datetime

def tableWriteRaw(Df, Dict):
    # Move data in Dict into Df.
    Df = Df.append(pd.Series(dtype=float), ignore_index=True)  # Insert Empty Rows
    Dict["TimeStamp"] =datetime.datetime.utcnow().strftime("%m%d%Y_%H:%M:%S.%f")[:-4]
    for key in Dict:
        Df[key].loc[len(Df) - 1] = Dict[key]  # FYI, len(Df)-1: means the last row of pandas dataframe.
    return Df

# Header = ["TimeStamp","expName","subjectID","Session","Run","Block","TrialCount","Section","Section Start Time",
#           "Section End Time","Image Displayed","Button Pressed","Button Response Time"]

def tableWrite(df,params,dict):
    # Move data in Dict into Df.
    df = df.append(pd.Series(dtype=float), ignore_index=True)  # Insert Empty Rows
    dict["Run"] = params["Run"]
    dict["Block"] = params["Block"]
    dict["TrialCount"] = params["TrialCount"]
    for key in dict:
        df[key].loc[len(df) - 1] = dict[key]  # FYI, len(Df)-1: means the last row of pandas dataframe.
    return df
