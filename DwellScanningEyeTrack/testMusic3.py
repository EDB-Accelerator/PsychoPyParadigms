# Documentation http://www.pygame.org/docs/ref/music.html#pygame.mixer.music.play
import glob
import vlc
import pygame
# from vlc import Instance
playlist = glob.glob('./music/*.mp3')

pygame.mixer.init()
pygame.mixer.music.load ( playlist.pop() )
pygame.mixer.music.queue ( playlist.pop() )
pygame.mixer.music.set_endevent ( pygame.USEREVENT )
# pygame.mixer.music.play(loops=-1)
pygame.mixer.music.play(-1,0.0)

# pause
pygame.mixer.music.pause()

# play again
pygame.mixer.music.unpause()
a = 0

running = True
while a == 0:
   while running:
      for event in pygame.event.get():
         if event.type == pygame.USEREVENT:
            if len ( playlist ) >1:
               pygame.mixer.music.queue ( playlist.pop() )