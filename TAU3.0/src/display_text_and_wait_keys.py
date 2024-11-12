from psychopy import visual, event

# Function to display the input dialog and return the results
def display_text_and_wait_keys(win,text,keys):
    # Create a text stimulus
    hello_text = visual.TextStim(win, text=text, color=(1, 1, 1), colorSpace='rgb', pos=(0, 0),wrapWidth=2)

    # Draw the text stimulus to the window
    hello_text.draw()

    # Flip the window (i.e., display the stimulus)
    win.flip()

    # Wait for a key press
    if keys == "any":
        keys = event.waitKeys()  # Wait for any key press
    else:
        keys = event.waitKeys(keyList=keys)  # Wait for specific keys