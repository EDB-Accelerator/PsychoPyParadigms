import subprocess,sys
p = subprocess.Popen([sys.executable, 'testMusic3.py'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)

p.terminate()

# import pygame
#
# # loop = asyncio.get_event_loop()
# # t = threading.Thread(target=PlayMusicStart, args=(params['musicList'],))
# # t.start()