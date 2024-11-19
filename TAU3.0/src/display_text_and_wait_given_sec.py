from psychopy import visual, core, event


def display_text_and_wait_given_sec(win, text, wait_time):
    """
    Displays a text stimulus and waits for a given number of seconds,
    capturing the first keyboard input if provided.

    Parameters:
    win (psychopy.visual.Window): The PsychoPy window where the text will be displayed.
    text (str): The text to display.
    wait_time (float): The number of seconds to wait.

    Returns:
    str or None: The first key pressed by the user, or None if no key is pressed.
    """
    # Create a text stimulus
    hello_text = visual.TextStim(win, text=text, color=(1, 1, 1), colorSpace='rgb', pos=(0, 0), wrapWidth=2)

    # Draw the text stimulus to the window
    hello_text.draw()

    # Flip the window (i.e., display the stimulus)
    win.flip()

    # Initialize variables
    user_input = None
    timer = core.Clock()

    # Wait for the given time while checking for keyboard input
    while timer.getTime() < wait_time:
        keys = event.getKeys()
        if keys and user_input is None:  # Capture the first key press
            user_input = keys[0]

    return user_input
