import sys
sys.path.insert(1, './src')

from psychopy import visual
from Helper import waitUserSpace,displayVAS,tableWrite

# VAS Session Module.
def VASplay(Df, win, params, SectionName):
    # VAS Initialization.
    import datetime, time,random
    Dict = {'ExperimentName': params['expName'],
            "Subject": params['subjectID'],
            "Session": params['Session'],
            "Version": params['Version'],
            "Section": SectionName,
            "VAS_type": "Anxiety",
            "SessionStartDateTime": datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")}

    # VAS Start Screen
    message = visual.TextStim(win, text="Before we continue, please answer a few questions. \n\n Press the spacebar to continue.",units='norm', wrapWidth=3)
    message.draw();win.flip()
    # waitUserInput(Df,message, win, params)
    waitUserSpace(Df,params)
    # event.waitKeys(maxWait=3)


    # --- 1. Put each VAS item into a list ---------------------------------------
    # vas_items = [
    #     # (VAS_type, question text, anchors)
    #     ("Anxiety", "How anxious do you feel right now?", ['Calm', 'Anxious']),
    #     ("Avoidance", "How much do you feel like taking part in the task?", ['Not at all', 'Very much']),
    #     ("Tired", "How tired are you right now?", ['Not at all tired', 'Very tired']),
    #     ("Mood", "Think about your mood right now.\nHow would you describe it?",
    #      ['Worst mood ever', 'Best mood ever']),
    #     ("Annoy", "How annoyed do you feel right now?", ['Not at all', 'Very much']),
    # ]
    vas_items = [
        # (VAS_type, question text, anchors)
        ("Tired",
         "How TIRED do you feel right now?",
         ['Not at all', 'Extremely']),
        ("Avoidance", "How much do you feel like TAKING PART in the task?", ['Not at all', 'Extremely']),
        ("Annoy",
         "How ANNOYED do you feel right now?",
         ['Not at all', 'Extremely']),

        ("Anxiety",
         "How ANXIOUS do you feel right now?",
         ['Not at all', 'Extremely']),

        ("Mood",
         "How would you describe your MOOD right now?",
         ['Worst ever', 'Best ever']),

        # ("Control",
        #  "How much CONTROL did you feel over what happened in the game?",
        #  ['Not at all', 'Extremely']),
    ]

    # --- 2. Shuffle in-place (one line) -----------------------------------------
    random.shuffle(vas_items)  # different order every session

    # --- 3. Present in whatever order came out of the shuffle -------------------
    for vas_type, question, anchors in vas_items:
        Dict["VAS_type"] = vas_type
        Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")

        startTime = time.time()
        Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(Df, params, win, question, anchors)
        Dict["VAS_RT"] = (time.time() - startTime) * 1000

        Df = tableWrite(Df, params, Dict)  # log result in the same way as before

    # # VAS (Anxiety)
    # startTime = time.time()
    # Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(Df,params,win, "How anxious do you feel right now?",
    #                                                    ['Calm', 'Anxious'])
    # Dict["VAS_RT"] = (time.time() - startTime) * 1000
    # Df = tableWrite(Df, params,Dict)  # Log the dict result on pandas dataFrame.
    #
    # # VAS (Avoidance)
    # Dict["VAS_type"] = "Avoidance"
    # Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    # startTime = time.time()
    # Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(Df,params,win, "How much do you feel like taking part in the task?",
    #                                                    ['Not at all', 'Very much'])
    # Dict["VAS_RT"] = (time.time() - startTime) * 1000
    # Df = tableWrite(Df, params,Dict)  # Log the dict result on pandas dataFrame.
    #
    # # VAS (Tired)
    # Dict["VAS_type"] = "Tired"
    # Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    # startTime = time.time()
    # Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(Df,params,win, "How tired are you right now?",
    #                                                    ['Not at all tired', 'Very tired'])
    # Dict["VAS_RT"] = (time.time() - startTime) * 1000
    # Df = tableWrite(Df, params,Dict)  # Log the dict result on pandas dataFrame.
    #
    # # VAS (Mood)
    # Dict["VAS_type"] = "Mood"
    # Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    # startTime = time.time()
    # Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(Df,params,win,
    #                                                    "Think about your mood right now. \nHow would you describe it?",
    #                                                    ['Worst mood ever', 'Best mood ever'])
    # Dict["VAS_RT"] = (time.time() - startTime) * 1000
    # Df = tableWrite(Df, params, Dict)  # Log the dict result on pandas dataFrame.
    #
    # # VAS (Annoy)
    # Dict["VAS_type"] = "Annoy"
    # Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    # startTime = time.time()
    # Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(Df, params, win,
    #                                                "How annoyed do you feel right now?",
    #                                                ['Not at all', 'Very much'])
    # Dict["VAS_RT"] = (time.time() - startTime) * 1000
    # Df = tableWrite(Df, params, Dict)  # Log the dict result on pandas dataFrame.

    # Question (Charge)
    if SectionName != "VAS pre":
        Dict["VAS_type"] = "Charge"
        Dict["SessionStartDateTime"] = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
        startTime = time.time()
        Dict["VAS_score"], Dict["VAS_RT"] = displayVAS(Df,params,win,"How much CONTROL did you feel over what happened in the game?",
                                                   ['Not at all', 'Extremely'])
        Dict["VAS_RT"] = (time.time() - startTime) * 1000
        Df = tableWrite(Df, params, Dict)  # Log the dict result on pandas dataFrame.

    return tableWrite(Df, params,Dict)  # Log the dict result on pandas dataFrame.
