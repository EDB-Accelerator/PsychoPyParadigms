def ELIdxRecord(DfTR,params,section,duration,subtrial,event):

    # Create empty dictionary.
    dict = {}
    HeaderTR = ["Index","subjectID","Session","Version","Section","Subtrial","Event","Duration(ms)"]

    # Index Increment.
    params["idxTR"] += 1

    # Move data in Dict into Df.
    dict["Index"] = params["idxTR"]
    dict["subjectID"] = params["subjectID"]
    dict["Session"] = params["Session"]
    dict["Version"] = params["Version"]
    dict["Section"] = section
    dict["Subtrial"] = subtrial
    dict["Event"] = event
    dict["Duration(ms)"] = duration * 1000

    DfTR = DfTR.append(dict, ignore_index=True)

    return DfTR

