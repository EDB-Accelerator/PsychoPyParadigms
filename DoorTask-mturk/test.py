# from psychopy.hardware import keyboard
# from psychopy import core

# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses

# # during your trial
# kb.clock.reset()  # when you want to start the timer from
# keys = kb.getKeys(['right', 'left', 'quit'], waitRelease=True)
#
# while True:
#     keys = kb.getKeys(['right', 'left', 'quit'], waitRelease=False)
#     keys2 = kb.getKeys(['right', 'left', 'quit'], waitRelease=True)
#     for key in keys:
#         print("keys",key.name, key.rt, key.duration)
#     for key in keys2:
#         print("keys2",key.name, key.rt, key.duration)
#
#     print(keys)
#     core.wait(0.1)
#
# if 'quit' in keys:
#     core.quit()

# kb = KeyBoard()
# wait for keypresses here
# keys = kb.getKeys()
# for thisKey in keys:
#     if thisKey=='q':  # it is equivalent to the string 'q'
#         core.quit()
#     else:
#         print(thisKey.name, thisKey.tDown, thisKey.rt)
#
# while True:
#     kb = keyboard.Keyboard()
#     kb.clock.reset()
#     keys = kb.getKeys()
#     for thisKey in keys:
#         if thisKey == 'q':  # it is equivalent to the string 'q'
#             core.quit()
#         else:
#             print(thisKey.name, thisKey.tDown, thisKey.rt)

from pynput.keyboard import Key, Listener

def on_press(key):
    # print('{0} pressed'.format(
    #     key))
    print("pressed:",key)

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()