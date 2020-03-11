import cv2 as cv
import numpy as np
import imutils
from matplotlib import pyplot as plt

method = 'cv.TM_CCOEFF_NORMED'


def localize(map_path, template_path):

    img = cv.imread(map_path, 0)
    img2 = img.copy()
    template = cv.imread(template_path, 0)
    w, h = template.shape[::-1]

    rot_angle = 0
    max_score = 0
    max_score_loc = (0, 0)
    template_w = 0
    template_h = 0

    for angle in np.arange(0, 360, 1):
        rotated_template = imutils.rotate(template, angle)

        # Crop photo to 1/3 original size
        cropped_template = rotated_template[(h/3):(2*h/3), (w/3):(2*w/3)]
        w1, h1 = cropped_template.shape[::-1]

        # Perform matching
        res = cv.matchTemplate(img, cropped_template, eval(method))
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        # If this the best score update
        if max_val > max_score:
            max_score = max_val
            max_score_loc = max_loc
            rot_angle = angle
            img2 = cropped_template
            template_w = w1
            template_h = h1

    # cv.imshow("rotated", img2)
    # cv.waitKey(5000)
    # print(method + ": " + str(max_score))
    # print("At loc: " + str(max_score_loc))
    # print("Angle: " + str(rot_angle))
    # top_left = max_score_loc
    # bottom_right = (top_left[0] + w1, top_left[1] + h1)
    # cv.rectangle(img, top_left, bottom_right, 255, 2)
    # plt.subplot(121), plt.imshow(res, cmap='gray')
    # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(img, cmap='gray')
    # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.suptitle(method)
    # plt.show()

    max_score_loc = (max_score_loc[0] + template_w/2,
                     max_score_loc[1] + template_h/2)

    return max_score, max_score_loc, rot_angle


if __name__ == "__main__":
    map_path = '../../frontend-webapp/maps/localization.pgm'
    template_path = '../../frontend-webapp/templates/localization_template.pgm'
    max_score, max_score_loc, rot_angle = localize(map_path, template_path)
