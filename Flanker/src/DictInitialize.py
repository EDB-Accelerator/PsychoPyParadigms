# Header = ["expName","Version","subjectID","Session Number","Start Time","End Time","Duration","timingFile","Event",
          # "User Response", "Right Answer", "Correct or Incorrect","User Response TimeStamp","User Response Time"]

def DictInitialize(params):
    dict = {'expName': params['expName'],
            'Version': params['Version'],
            "subjectID": params['subjectID'],
            "Session Number": params['Session'],
            "User Response": "",
            }
    for h in params["header"]:
        if h not in dict: dict[h]=""
    return dict