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