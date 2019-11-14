import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import webview
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def ros_to_matplotlib(coord):
    return (coord[0]/0.05 + 80, coord[1]/0.05 + 80)


fig, ax = plt.subplots()
img = mpimg.imread('/home/darebalogun/Desktop/maps/map.pgm')
imgplot = plt.imshow(img, cmap='gray', origin='upper')
coord = (0.325365936796, -0.180220022798)
x,y = ros_to_matplotlib(coord)
plt.scatter(x, y, s=50, c='red', marker='o', picker=5)
chrome_options = Options()
chrome_options.add_argument(
    "--app=https://developers.google.com/vr/develop/web/vrview-web")
chrome_options.add_argument("--window-size=1920,640")
chrome_options.add_experimental_option(
    "excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(
    executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)

html = """<!DOCTYPE html>
<html>
<head>
<script src="https://storage.googleapis.com/vrview/2.0/build/vrview.min.js"></script>
</head>
<body>
<h1> Hello </h1>
<img src='https://www.w3schools.com/images/w3schools_green.jpg'>
<iframe src='https://storage.googleapis.com/vrview/2.0/embed?image=https://www.camera-rumors.com/wp-content/uploads/2015/09/Ricoh-Theta-S-sample-images.jpg&is_stereo=true">
</iframe>
</body>
</html>
"""


def onpick(event):
    print(str(event.ind) + " clicked!")

    url = 'https://developers.google.com/vr/develop/web/vrview-web'

    driver.get(url)


fig.canvas.mpl_connect('pick_event', onpick)

plt.show()
