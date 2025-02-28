import sys
sys.path.append('libs')
import keyboard  # For capturing keyboard input when no joystick is available

class VirtualJoystick:
    """
    A virtual joystick that uses arrow keys for movement and space as a button.
    """

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.button_pressed = False  # Simulates button press (space key)

    def update(self):
        """
        Updates the virtual joystick state based on keyboard input.
        """
        self.x, self.y = 0.0, 0.0
        self.button_pressed = False

        if keyboard.is_pressed('left'):
            self.x = -1.0
        elif keyboard.is_pressed('right'):
            self.x = 1.0
        if keyboard.is_pressed('up'):
            self.y = -1.0
        elif keyboard.is_pressed('down'):
            self.y = 1.0

        # Simulate button press with spacebar
        if keyboard.is_pressed('space'):
            self.button_pressed = True

    def get_input(self):
        """
        Returns joystick-like input in dictionary format.
        """
        return {
            'x': self.x,
            'y': self.y,
            'buttons_text': ' ' if not self.button_pressed else 'space'
        }

def JoystickInput():
    """
    Returns a dictionary-like joystick input, ensuring compatibility with existing code.
    """
    joystick = VirtualJoystick()  # Create an instance
    joystick.update()  # Update the state
    return joystick.get_input()  # Return dictionary directly
