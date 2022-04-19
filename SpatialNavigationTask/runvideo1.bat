@setlocal enableextensions
@cd /d "%~dp0"
"C:\Program Files\VideoLAN\VLC\vlc.exe" --fullscreen --mouse-hide-timeout=0 --quiet --intf dummy --dummy-quiet --video-on-top --no-interact --no-sub-autodetect-file --no-video-title "./img/Version1/Video/video.mp4" vlc://quit