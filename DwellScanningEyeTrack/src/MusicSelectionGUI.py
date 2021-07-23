# Refernece:
# https://www.blog.pythonlibrary.org/2013/02/27/wxpython-adding-checkboxes-to-objectlistview/
# OLVcheckboxes2.py
import sys

import wx
from ObjectListView import ObjectListView, ColumnDefn, OLVEvent
import glob
from mutagen.easyid3 import EasyID3
import pandas as pd
import numpy as np

class Results(object):
    """"""

    def __init__(self, title, Artist, Album, Genre, ReleaseDate):
        """Constructor"""
        self.title = title
        self.Artist = Artist
        self.Album = Album
        self.Genre = Genre
        self.ReleaseDate = ReleaseDate

class OLVCheckPanel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        logSizer = wx.BoxSizer(wx.HORIZONTAL)

        musicList = glob.glob("music/*.mp3")
        self.fileNames = {}
        self.test_data = []
        for musicFile in musicList:
            audio = EasyID3(musicFile)
            self.fileNames[audio['title'][0]] = musicFile
            self.test_data.append(Results(audio['title'][0],audio['artist'][0],audio['album'][0],audio['genre'][0],
                                          audio['date'][0]))
        self.resultsOlv = ObjectListView(self,
                                         style=wx.LC_REPORT | wx.SUNKEN_BORDER)

        self.setResults()

        checkBtn = wx.Button(self, label="Select all")
        checkBtn.Bind(wx.EVT_BUTTON, self.onCheck)
        btnSizer.Add(checkBtn, 0, wx.ALL, 5)

        uncheckBtn = wx.Button(self, label="Unselect all")
        uncheckBtn.Bind(wx.EVT_BUTTON, self.onUncheck)
        btnSizer.Add(uncheckBtn, 0, wx.ALL, 5)

        self.exitBtn = wx.Button(self, label="Confirm")
        self.exitBtn.Bind(wx.EVT_BUTTON, self.wxQuit)
        btnSizer.Add(self.exitBtn, 0, wx.ALL, 5)

        self.resultsOlv.Bind(OLVEvent.EVT_ITEM_CHECKED, self.on_item_checked)

        mainSizer.Add(self.resultsOlv, 1, wx.EXPAND | wx.ALL, 5)
        mainSizer.Add(btnSizer, 0, wx.CENTER | wx.ALL, 5)

        self.log = wx.TextCtrl(self,style=wx.TE_READONLY)
        logSizer.Add(self.log,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        mainSizer.Add(logSizer, 0, wx.EXPAND, 5)

        self.SetSizer(mainSizer)

    def on_item_checked(self, event):
        # a = self.resultsOlv.GetCheckedObjects()
        # if len(a)>=0:
        #     print(a[0].ReleaseDate)
        obj = self.resultsOlv.GetCheckedObjects()
        # checked = 'Checked' if self.resultsOlv.IsChecked(obj) else 'Unchecked'
        # print('{} row is {}'.format(obj.ReleaseDate, checked))
        # print(len(a), ' music file(s) selected')
        # self.title = str(len(a)) + ' music file(s) selected'
        self.log.Clear()
        self.log.AppendText(str(len(obj)) + ' music file(s) selected')

    def onCheck(self, event):
        """"""
        objects = self.resultsOlv.GetObjects()

        for obj in objects:
            self.resultsOlv.SetCheckState(obj, True)
        self.resultsOlv.RefreshObjects(objects)

    def onUncheck(self, event):
        """"""
        objects = self.resultsOlv.GetObjects()

        for obj in objects:
            self.resultsOlv.SetCheckState(obj, False)
        self.resultsOlv.RefreshObjects(objects)

    def wxQuit(self, event):
        obj = self.resultsOlv.GetCheckedObjects()
        if len(obj) < 10:
            self.log.Clear()
            self.log.AppendText('At least 10 music files need to be selected. Only ' + str(len(obj)) + ' music file(s) selected.')
            return

        df = pd.DataFrame()
        for musicObj in obj:
            musicInfo = []
            musicFileName = self.fileNames[musicObj.title]
            musicFileName = musicFileName.replace("mp3","wav")

            # musicInfo.append(self.fileNames[musicObj.title])
            musicInfo.append(musicFileName)
            musicInfo.append(musicObj.title)
            musicInfo.append(musicObj.Artist)
            musicInfo.append(musicObj.Album)
            musicInfo.append(musicObj.Genre)
            musicInfo.append(musicObj.ReleaseDate)
            musicInfoPD = (np.array(musicInfo).flatten()).reshape(1, len(musicInfo))
            musicInfoPD = pd.DataFrame(musicInfoPD, columns=["fileName","Title","Artist","Album","Genre","Release Date"])
            df = df.append(musicInfoPD,ignore_index = True)

        df.to_csv("userMusicSelection.csv", mode='w', sep=',', encoding='utf-8')

        wx.CallAfter(frame.Close)

    def setResults(self):

        """"""
        self.resultsOlv.SetColumns([
            ColumnDefn("♫ title", "left", 300, "title"),
            ColumnDefn("Artist", "left", 150, "Artist"),
            ColumnDefn("Album", "left", 100, "Album"),
            ColumnDefn("Genre", "left", 150, "Genre"),
            ColumnDefn("Release Date", "left", 150, "ReleaseDate")
        ])
        self.resultsOlv.CreateCheckStateColumn()
        self.resultsOlv.SetObjects(self.test_data)

class OLVCheckFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        title = "Select Music Files"
        wx.Frame.__init__(self, parent=None, title=title, size=(1024, 728))
        panel = OLVCheckPanel(self)


if __name__ == "__main__":
    app = wx.App(False)
    frame = OLVCheckFrame()
    frame.Show()
    app.MainLoop()


