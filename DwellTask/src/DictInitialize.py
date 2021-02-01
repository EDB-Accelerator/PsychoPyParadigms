def DictInitialize(params):

    dict = {'expName' : params['expName'],
            "subjectID": params['subjectID'],
            "Session": params['Session'],
    }
    dictRaw = dict.copy()

    return dict,dictRaw
