from psychopy import visual, event, core,gui
import sys
sys.path.insert(1,'src')

# Function to display the input dialog and return the results
def get_user_input():
    info = {'Subject Number': '', 'Session Number': '', 'Stimuli Set': ['A', 'B']}
    order = ['Subject Number', 'Session Number', 'Stimuli Set']
    dlg = gui.DlgFromDict(dictionary=info, title='Experiment Startup', order=order)
    if dlg.OK:
        return info
    else:
        core.quit()  # the user hit cancel so exit

def display_text_and_wait_keys(win,text,keys):
    # Create a text stimulus
    hello_text = visual.TextStim(win, text=text, color=(1, 1, 1), colorSpace='rgb', pos=(0, 0),wrapWidth=2)

    # Draw the text stimulus to the window
    hello_text.draw()

    # Flip the window (i.e., display the stimulus)
    win.flip()

    # Wait for a key press (specifically the spacebar)
    keys = event.waitKeys(keyList=keys)

def display_text_and_wait_given_sec(win,text,wait_time):
    # Create a text stimulus
    hello_text = visual.TextStim(win, text=text, color=(1, 1, 1), colorSpace='rgb', pos=(0, 0),wrapWidth=2)

    # Draw the text stimulus to the window
    hello_text.draw()

    # Flip the window (i.e., display the stimulus)
    win.flip()

    # Display the text and check for a key press within 1 second
    user_input = None
    timer = core.Clock()
    while timer.getTime() < wait_time:  # Run for 1 second
        keys = event.getKeys()
        if keys:
            user_input = keys[0]
            break
    return user_input

def display_check_scanner(win):
    info = {}
    gui.DlgFromDict(dictionary=info,title='Scanner Prepared?')
    # core.quit()  # the user hit cancel so exit

display_text_and_wait_keys(win,'Instructions\n\n'
                'In each trial, a + sign will appear in the center of the screen,\n'
                'followed by a pair of faces, and then by a target: < or >\n\n'
                'if the target is <, press the left button.\n'
                'if the target is >, press the right button.\n\n'
                'Respond as quickly as you can without making mistakes\n\n'
                'Press any button to start.', ['space'])

user_info = get_user_input()

# Create a window
win = visual.Window(size=(1024, 768), fullscr=False, color=(0, 0, 0), colorSpace='rgb')
key = display_text_and_wait_given_sec(win,"",1.0)
display_check_scanner(win)
display_text_and_wait_keys(win,'Waiting for the scanner..', ['4'])

# Close the window and quit PsychoPy
# win.close()
# core.quit()