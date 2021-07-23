def LoadTimingFile(inFile):
    import pandas as pd

    bad_words = ['events', '-----','class']

    with open(inFile) as oldfile, open('.tmp/1.csv', 'w') as newfile:
        newfile.write('class,start,dur,rest\n')
        for line in oldfile:
            if not line.strip(): continue
            if not any(bad_word in line for bad_word in bad_words):
                line = line.replace('(disgust)','')
                line = line.replace('(anger)', '')
                line = ','.join(line.split()) +'\n'
                newfile.write(line)

    df = pd.read_csv('.tmp/1.csv')
    # dfRun1 = df.iloc[0:60]
    # dfRun2 = df.iloc[60:120]
    # dfRun3 = df.iloc[120:]
    # return dfRun1,dfRun2,dfRun3
    return df
