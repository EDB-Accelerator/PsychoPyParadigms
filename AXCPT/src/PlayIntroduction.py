def PlayIntroduction(win,params):

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
    WaitUserSpace()

    # Introduction
    c = ['Y']
    while (c[0].upper()=='Y'):

        message = visual.TextStim(win,text="The task sequence looks like:",
                                          units='norm', wrapWidth=1000, color="white",pos=[0,0.5])
        message.draw()
        win.flip()
        WaitUserSpace()


        for i in range(3):
            imgFile = "resource/img/intro" + str(i) + ".JPG"
            img1 = visual.ImageStim(win=win, image=imgFile, units="norm", opacity=1,size=[1.2,1.2])
            img1.draw()
            message.draw()
            win.flip()
            WaitUserSpace()

        # Introduction Slide 2
        message = visual.TextStim(win,text="Press the YES (index) key as quickly as you can when you see the\n"+
                                  "blue letter that completes the target sequence. Press the NO\n"+
                                  "(middle) key as quickly as you can for all other letters.\n\n\n\n\n"+
                                  "Please SPACE BAR to continue",
                                          units='norm', wrapWidth=1000, color="white")
        message.draw()
        win.flip()
        WaitUserSpace()

        # Introduction Slide 3
        message = visual.TextStim(win,text="Are you ready to start the task\n\n"
                                           "or\n\n"
                                           "should we review the instructions again?\n\n\n"
                                           "Press Y if Yes / Press N if No",
                                          units='norm', wrapWidth=1000, color="white")
        message.draw()
        win.flip()
        c = ['']
        # Wait for user types "y" or "n".
        while (c[0].upper() != "Y" and c[0].upper() != "N"):
            core.wait(1 / 120)
            c = event.waitKeys()  # read a characters

    # Section Termination
    DataWrite(params=params, startTime=startTime, endTime=datetime.datetime.now(), trialCount="",
              event="Instruction displayed", timingFile="", userResponse="", rightAnswer="",userResponseTime="",
              userResponseOffset=0)

    return win
