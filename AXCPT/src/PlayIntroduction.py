def PlayIntroduction(win,params,timingFileCount,df):

    from psychopy import visual, core, event
    from WaitAndGetUserInput import WaitUserSpace
    from DictWrite import DataWrite
    import datetime

    # Section Initialization
    startTime = datetime.datetime.now()

    # Welcome / Introduction Screen
    message = visual.TextStim(win,text="Welcome!\n\n"+
                              "Please remember the task where we ask you to\n"+
                              "remember a series of letters\n\n\n\n\n\n\n"+
                              "Please press SPACE BAR to see an example.",
                                      units='norm', wrapWidth=1000, color="white")
    message.draw()
    win.flip()
    win.winHandle.activate()
    WaitUserSpace(win)

    # Introduction
    userInput = [params['yesKey']]
    while (userInput[0].upper()==params['yesKey']):

        message = visual.TextStim(win,text="The task sequence looks like:",
                                          units='norm', wrapWidth=1000, color="white",pos=[0,0.5])
        message.draw()
        win.flip()
        WaitUserSpace(win)


        for i in range(3):
            imgFile = "resource/img/intro" + str(i) + ".JPG"
            img1 = visual.ImageStim(win=win, image=imgFile, units="norm", opacity=1,size=[1.2,1.2])
            img1.draw()
            message.draw()
            win.flip()
            WaitUserSpace(win)

        # Introduction Slide 2
        message = visual.TextStim(win,text="Press the YES (Right) key as quickly as you can\n"
                                           "when you see the blue letter that completes the\n"
                                           "target sequence.\n\n"
                                           "Press the NO (Left) key as quickly as you can\n"
                                           "for all other letters.\n\n\n\n\n"+
                                  "Please SPACE BAR to continue",
                                          units='norm', wrapWidth=1000, color="white")
        message.draw()
        win.flip()
        WaitUserSpace(win)

        # Introduction Slide 3
        message = visual.TextStim(win,text="Are you ready to start the task?\n\n"
                                           "or\n\n"
                                           "should we review the instructions again?\n\n\n"
                                           "Press Y to review / Press N if ready to start",
                                          units='norm', wrapWidth=1000, color="white")
        message.draw()
        win.flip()
        userInput = ['']
        # Wait for user types "y" or "n".
        while (userInput[0].upper() != params['yesKey'] and userInput[0].upper() != params['noKey']):
            core.wait(1 / 3000)
            userInput = event.waitKeys()  # read a characters
            # print(userInput)
            # if userInput == ['q'] or userInput == ['Q']:
            #     print('Q pressed. Forced Exit.')
            #     core.quit()


    # Section Termination
    df = DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount="",timingCount=timingFileCount,trialType="",
              event="Instruction displayed", timingFile="", userResponse="", rightAnswer="",userResponseTime="",
              userResponseOffset=0,cueLetter="",probeLetter="",correctness="",df=df)

    return win
