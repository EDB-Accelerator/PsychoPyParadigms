@setlocal enableextensions
@cd /d "%~dp0"
"C:\Program Files\VideoLAN\VLC\vlc.exe" music --loop --random

"C:\Program Files\VideoLAN\VLC\vlc.exe" -I telnet --telnet-password test

"C:\Program Files\VideoLAN\VLC\vlc.exe" -I rc

"C:\Program Files\VideoLAN\VLC\vlc.exe" -I ncurses


import os

vlc_path = "C:\Program Files\VideoLAN\VLC\vlc.exe "
net_stream = "http://host[:port]/file " # You can use other protocols too

os.chdir(vlc_path)
os.system(f"{net_stream}")