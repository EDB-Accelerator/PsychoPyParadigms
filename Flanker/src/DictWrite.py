from DictInitialize import DictInitialize

def DictWrite(df,dict,params):
    dict["Duration"] = dict["Duration"].total_seconds()
    df = df.append(dict, ignore_index=True)
    # df.to_csv(params['outFile'], sep=',', encoding='utf-8', index=False)
    dict = DictInitialize(params)
    return df,dict