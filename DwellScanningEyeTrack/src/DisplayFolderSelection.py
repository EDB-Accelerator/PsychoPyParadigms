# Reference:

# https://www.blog.pythonlibrary.org/2010/06/26/the-dialogs-of-wxpython-part-1-of-2/

import os
import wx
import wx.lib.agw.multidirdialog as MDD
from psychopy import visual
import glob

########################################################################
class MyForm(wx.Frame):

    #----------------------------------------------------------------------
    MusicFolder = ""
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "Music Folder.",size = (300,100))
        panel = wx.Panel(self, wx.ID_ANY)
        self.currentDirectory = os.getcwd()

        dirDlgBtn = wx.Button(panel, label="Select Your Music Folder",size = (200,20), pos = (150,150))
        dirDlgBtn.Bind(wx.EVT_BUTTON, self.onDir)

        # put the buttons in a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(dirDlgBtn, 0, wx.ALL|wx.CENTER, 0)

        panel.SetSizer(sizer)

    def onClose(self, event):
        """"""
        self.Close()
    def onDir(self, event):
        """
        Show the DirDialog and print the user's choice to stdout
        """
        dlg = wx.DirDialog(self, "Choose a music directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )

        if dlg.ShowModal() == wx.ID_OK:
            newFolder = dlg.GetPath()
            # print("You chose %s" % newFolder)
            self.MusicFolder = newFolder
        dlg.Destroy()

        self.Close()

def DisplayFolderSelection(params):
    win = visual.Window(params['screenSize'], monitor="testMonitor", color="white", winType='pyglet')
    message = visual.TextStim(win,
                              text="Press select your music folder.\n ",
                              units='norm', wrapWidth=2, color="black")
    message.draw()
    win.flip()

    import tkinter as tk
    import tkinter.filedialog as fd
    root = tk.Tk()
    musicList = fd.askopenfilenames(parent=root, title='Choose music files.')

    return musicList


