
# answer = None
#
# def check():
#     time.sleep(2)
#     if answer != None:
#         return
#     print("Too Slow")
#
# Thread(target = check).start()
#
# answer = input("Input something: ")


# from threading import Timer
# from psychopy import event,visual,core
#
# import time
# win = visual.Window(monitor="testMonitor", color="black", size=[1024,768],winType='pyglet')
#
# timeout = 10
# startTime = time.time()
# # t = Timer(timeout, print, ['Sorry, times up'])
# t = Timer(timeout, print, [str(time.time()-startTime)])
# t.start()
# prompt = "You have %d seconds to choose the correct answer...\n" % timeout
# c = event.waitKeys()
# responseTime = time.time()
# core.wait(10-(responseTime-startTime))
# t.cancel()
#
# print(time.time()-startTime)
# win.close()


# import time
# from threading import Thread
#
# answer = None
#
# def check():
#     time.sleep(2)
#     if answer != None:
#         return
#     print("Too Slow")
#
# startTime = time.time()
# Thread(target = check).start()
# answer = input("Input something: ")
# print(time.time()-startTime)
