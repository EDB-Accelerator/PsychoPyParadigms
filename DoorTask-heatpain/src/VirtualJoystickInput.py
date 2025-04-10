import platform

if platform.system() == 'Windows':
    import sys
    sys.path.append('libs')
    import keyboard  # Only works on Windows

    class VirtualJoystick:
        """
        A virtual joystick that uses arrow keys for movement and space as a button (Windows only).
        """
        def __init__(self):
            self.x = 0.0
            self.y = 0.0
            self.button_pressed = False

        def update(self):
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

            if keyboard.is_pressed('space'):
                self.button_pressed = True

        def get_input(self):
            return {
                'x': self.x,
                'y': self.y,
                'buttons_text': 'space' if self.button_pressed else ' '
            }

    def JoystickInput():
        joystick = VirtualJoystick()
        joystick.update()
        return joystick.get_input()

else:
    # macOS / Linux fallback using pygame
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    pygame.display.set_caption("Virtual Joystick (macOS/Linux)")

    class VirtualJoystick:
        def __init__(self):
            self.x = 0.0
            self.y = 0.0
            self.button_pressed = False

        def update(self):
            self.x, self.y = 0.0, 0.0
            self.button_pressed = False

            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.x = -1.0
            elif keys[pygame.K_RIGHT]:
                self.x = 1.0
            if keys[pygame.K_UP]:
                self.y = -1.0
            elif keys[pygame.K_DOWN]:
                self.y = 1.0
            if keys[pygame.K_SPACE]:
                self.button_pressed = True

        def get_input(self):
            return {
                'x': self.x,
                'y': self.y,
                'buttons_text': 'space' if self.button_pressed else ' '
            }

    def JoystickInput():
        joystick = VirtualJoystick()
        joystick.update()
        return joystick.get_input()
