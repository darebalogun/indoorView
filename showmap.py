import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import webview
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def ros_to_matplotlib(coord):
    return (coord[0]/0.05 + 80, -1*coord[1]/0.05 + 80)


fig, ax = plt.subplots()
plt.gca().invert_yaxis()
img = mpimg.imread('/home/darebalogun/Desktop/maps/map.pgm')
imgplot = plt.imshow(img, cmap='gray', origin='upper', aspect='auto')
coord = (-0.0250, -1.0413)
coord1 = (0.005006, 1.37167)
x,y = ros_to_matplotlib(coord)
x1, y1 = ros_to_matplotlib(coord1)
plt.axis('off')
plt.subplots_adjust(left=0, bottom=0, top=1.0, right=1.0)
plt.scatter(x, y, s=50, c='red', marker='o', picker=5)
plt.scatter(x1, y1, s=50, c='red', marker='o', picker=5)
fig.canvas.toolbar.pack_forget()
chrome_options = Options()
chrome_options.add_argument(
    "--app=http://127.0.0.1:8887/index.html")
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

    url = 'http://127.0.0.1:8887/index.html'

    driver.get(url)


fig.canvas.mpl_connect('pick_event', onpick)

plt.show()
