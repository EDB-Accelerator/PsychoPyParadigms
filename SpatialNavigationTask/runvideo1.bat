@setlocal enableextensions
@cd /d "%~dp0"
"C:\Program Files\VideoLAN\VLC\vlc.exe" --fullscreen --intf dummy --dummy-quiet --video-on-top --play-and-stop  --no-interact --play-and-exit "./img/Version1/Video/video.mp4" vlc://quit