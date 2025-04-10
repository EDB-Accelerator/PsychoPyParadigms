import platform

if platform.system() == 'Windows':
    # Import original Windows-only JoystickInput
    from JoystickInput_Windows import JoystickInput
else:
    # Define a macOS-compatible JoystickInput fallback
    import pygame

    pygame.init()
    pygame.joystick.init()


    def JoystickInput():
        if pygame.joystick.get_count() == 0:
            return {'x': 0, 'y': 0, 'lt': 0, 'rx': 0, 'ry': 0, 'rt': 0, 'buttons_text': '', 'erase': '',
                    "OEM name:": '', "Driver name:": ''}

        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        pygame.event.pump()

        x = joystick.get_axis(0)
        y = joystick.get_axis(1)
        rx = joystick.get_axis(2) if joystick.get_numaxes() > 2 else 0
        ry = joystick.get_axis(3) if joystick.get_numaxes() > 3 else 0
        lt = joystick.get_axis(4) if joystick.get_numaxes() > 4 else 0
        rt = joystick.get_axis(5) if joystick.get_numaxes() > 5 else 0

        buttons_text = ''
        for i in range(joystick.get_numbuttons()):
            if joystick.get_button(i):
                buttons_text += f'btn{i} '

        res = {
            'x': x,
            'y': y,
            'lt': lt,
            'rx': rx,
            'ry': ry,
            'rt': rt,
            'buttons_text': buttons_text,
            'erase': '',
            "OEM name:": 'Generic Joystick',
            "Driver name:": 'pygame'
        }

        return res
