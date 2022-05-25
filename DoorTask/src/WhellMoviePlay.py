from moviepy.editor import *
import pygame

pygame.display.set_caption('Hello World!')

clip = VideoFileClip('16-3.mov')
clip.preview()

pygame.quit()