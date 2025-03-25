import webbrowser
import os

# Path to your HTML file
html_file = "FortuneWheel/index16.html"
file_url = f"file://{os.path.abspath(html_file)}"

# Open in Edge with kiosk mode (hides URL bar)
os.system(f'start msedge --kiosk "{file_url}" --edge-kiosk-type=fullscreen')
