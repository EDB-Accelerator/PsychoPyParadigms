def DictInitialize(params):

    dict = {'expName' : params['expName'],
            'Version': params['Version'],
            "subjectID": params['subjectID'],
            "Session": params['Session'],
            "User Response": "",
    }
    dictRaw = dict.copy()

    return dict,dictRaw