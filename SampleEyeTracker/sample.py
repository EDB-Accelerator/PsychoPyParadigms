import pygame
import pygame.mixer
import pygame.event
import pygame.image
import pygame.draw
import pygame.mouse
import array

import Image
import pylink
from pygame.constants import *





class EyeLinkCoreGraphicsPyGame(pylink.EyeLinkCustomDisplay):
    def __init__(self,w,h, tracker):
        pylink.EyeLinkCustomDisplay.__init__(self)
        pygame.init()
        pygame.display.init()
        pygame.mixer.init()
        pygame.display.set_mode((w, h), FULLSCREEN |DOUBLEBUF |RLEACCEL,32)
        pygame.mouse.set_visible(False)
        self.__target_beep__ = pygame.mixer.Sound("type.wav")
        self.__target_beep__done__ = pygame.mixer.Sound("qbeep.wav")
        self.__target_beep__error__ = pygame.mixer.Sound("error.wav")
        self.imagebuffer = array.array('l')
        self.pal = None
        self.size = (0,0)
        if(not pygame.font.get_init()):
            pygame.font.init()
        self.fnt = pygame.font.Font("cour.ttf",25)
        self.fnt.set_bold(1)
        self.setTracker(tracker)
        self.last_mouse_state = -1




    def setTracker(self, tracker):
        self.tracker = tracker
        self.tracker_version = tracker.getTrackerVersion()
        if(self.tracker_version >=3):
            self.tracker.sendCommand("enable_search_limits=YES")
            self.tracker.sendCommand("track_search_limits=YES")
            self.tracker.sendCommand("autothreshold_click=YES")
            self.tracker.sendCommand("autothreshold_repeat=YES")
            self.tracker.sendCommand("enable_camera_position_detect=YES")




    def setup_cal_display (self):
        surf = pygame.display.get_surface()
        surf.fill((255,255,255,255))
        pygame.display.flip()


    def exit_cal_display(self):
        self.clear_cal_display()

    def record_abort_hide(self):
        pass

    def clear_cal_display(self):
        surf = pygame.display.get_surface()
        surf.fill((255,255,255,255))
        pygame.display.flip()
        surf.fill((255,255,255,255))

    def erase_cal_target(self):
        surf = pygame.display.get_surface()
        surf.fill((255,255,255,255))


    def draw_cal_target(self, x, y):
        outsz=10
        insz=4
        surf = pygame.display.get_surface()
        rect = pygame.Rect(x-outsz,y-outsz,outsz*2,outsz*2)
        pygame.draw.ellipse(surf,(0,0,0), rect)
        rect = pygame.Rect(x-insz,y-insz,insz*2,insz*2)
        pygame.draw.ellipse(surf,(255,255,255), rect)
        pygame.display.flip()

    def play_beep(self,beepid):
        if beepid == pylink.DC_TARG_BEEP or beepid == pylink.CAL_TARG_BEEP:
            self.__target_beep__.play()
        elif beepid == pylink.CAL_ERR_BEEP or beepid == pylink.DC_ERR_BEEP:
            self.__target_beep__error__.play()
        else:#  CAL_GOOD_BEEP or DC_GOOD_BEEP
            self.__target_beep__done__.play()


    def draw_line(self,x1,y1,x2,y2,colorindex):
        imr = self.__img__.get_rect()
        x1=int((float(x1)/float(self.size[0]))*imr.w)
        x2=int((float(x2)/float(self.size[0]))*imr.w)
        y1=int((float(y1)/float(self.size[1]))*imr.h)
        y2=int((float(y2)/float(self.size[1]))*imr.h)

        if colorindex   ==  pylink.CR_HAIR_COLOR:          color = (255,255,255,255)
        elif colorindex ==  pylink.PUPIL_HAIR_COLOR:       color = (255,255,255,255)
        elif colorindex ==  pylink.PUPIL_BOX_COLOR:        color = (0,255,0,255)
        elif colorindex ==  pylink.SEARCH_LIMIT_BOX_COLOR: color = (255,0,0,255)
        elif colorindex ==  pylink.MOUSE_CURSOR_COLOR:     color = (255,0,0,255)
        else: color =(0,0,0,0)
        pygame.draw.line(self.__img__,color,(x1,y1),(x2,y2))


    def get_input_key(self):
        ky=[]
        v = pygame.event.get()
        for key in v:
            if key.type != KEYDOWN:
                continue
            keycode = key.key
            if keycode == K_F1:  keycode = pylink.F1_KEY
            elif keycode ==  K_F2:  keycode = pylink.F2_KEY
            elif keycode ==   K_F3:  keycode = pylink.F3_KEY
            elif keycode ==   K_F4:  keycode = pylink.F4_KEY
            elif keycode ==   K_F5:  keycode = pylink.F5_KEY
            elif keycode ==   K_F6:  keycode = pylink.F6_KEY
            elif keycode ==   K_F7:  keycode = pylink.F7_KEY
            elif keycode ==   K_F8:  keycode = pylink.F8_KEY
            elif keycode ==   K_F9:  keycode = pylink.F9_KEY
            elif keycode ==   K_F10: keycode = pylink.F10_KEY

            elif keycode ==   K_PAGEUP: keycode = pylink.PAGE_UP
            elif keycode ==   K_PAGEDOWN:  keycode = pylink.PAGE_DOWN
            elif keycode ==   K_UP:    keycode = pylink.CURS_UP
            elif keycode ==   K_DOWN:  keycode = pylink.CURS_DOWN
            elif keycode ==   K_LEFT:  keycode = pylink.CURS_LEFT
            elif keycode ==   K_RIGHT: keycode = pylink.CURS_RIGHT

            elif keycode ==   K_BACKSPACE:    keycode = ord('\b')
            elif keycode ==   K_RETURN:  keycode = pylink.ENTER_KEY
            elif keycode ==   K_ESCAPE:  keycode = pylink.ESC_KEY
            elif keycode ==   K_TAB:     keycode = ord('\t')
            elif(keycode==pylink.JUNK_KEY): keycode= 0
            ky.append(KeyInput(keycode))
        return ky

    def exit_image_display(self):
        self.clear_cal_display()

    def alert_printf(self,msg):
        print "alert_printf"




    def setup_image_display(self, width, height):
        self.size = (width,height)
        self.clear_cal_display()
        self.last_mouse_state = -1

    def image_title(self, threshold, text):
        text = text + " " +str(threshold)

        sz = self.fnt.size(text[0])
        txt = self.fnt.render(text,len(text),(0,0,0,255), (255,255,255,255))
        surf = pygame.display.get_surface()
        imgsz=(self.size[0]*3,self.size[1]*3)
        topleft = ((surf.get_rect().w-imgsz[0])/2,(surf.get_rect().h-imgsz[1])/2)
        imsz=(topleft[0]+imgsz[0]/2,topleft[1]+imgsz[1]+10)
        surf.blit(txt, imsz)
        pygame.display.flip()
        surf.blit(txt, imsz)


    def draw_image_line(self, width, line, totlines,buff):
        #print "draw_image_line", len(buff)
        i =0
        while i <width:
            self.imagebuffer.append(self.pal[buff[i]])
            i= i+1


        if line == totlines:
            imgsz = (self.size[0]*3,self.size[1]*3)
            bufferv = self.imagebuffer.tostring()
            img =Image.new("RGBX",self.size)
            img.fromstring(bufferv)
            img = img.resize(imgsz)


            img = pygame.image.fromstring(img.tostring(),imgsz,"RGBX");

            self.__img__ = img
            self.draw_cross_hair()
            self.__img__ = None
            surf = pygame.display.get_surface()
            surf.blit(img,((surf.get_rect().w-imgsz[0])/2,(surf.get_rect().h-imgsz[1])/2))
            pygame.display.flip()
            self.imagebuffer = array.array('l')



    def set_image_palette(self, r,g,b):
        self.imagebuffer = array.array('l')
        self.clear_cal_display()
        sz = len(r)
        i =0
        self.pal = []
        while i < sz:
            rf = int(b[i])
            gf = int(g[i])
            bf = int(r[i])
            self.pal.append((rf<<16) | (gf<<8) | (bf))
            i = i+1

