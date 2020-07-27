import numpy as np
import cv2 as cv

good_ones = []
numOfLines = 25

Img = cv.imread('image Path', 0)
Img = cv.Canny(Img, 100, 300)
Img = cv.resize(Img, (1280,720))

h, w = Img.shape

thetas = np.linspace(0, 180, 181)

dist = int(pow((pow(h, 2) + pow(w, 2)), 0.5))

table = np.zeros((2 * dist, len(thetas)))

for x in range(w):
    for y in range(h):
        if Img[y, x] != 0:
            for theta in range(len(thetas)):
                d = round(x * np.cos(np.deg2rad(theta)) + y * np.sin(np.deg2rad(theta)))
                d += dist
                table[d, theta] += 1

Threshold = np.sort(table.flatten())[-numOfLines]

for d in range(2 * dist):
    for theta in range(len(thetas)):
        if table[d, theta] > Threshold:
            d -= dist
            good_ones.append([d, theta])
                
for [d, theta] in good_ones:
    x1 = 0
    y1 = round((d - x1 * np.cos(np.deg2rad(theta)))/(np.sin(np.deg2rad(theta)) + 0.00001))
    x2 = 1480
    y2 = round((d - x2 * np.cos(np.deg2rad(theta)))/(np.sin(np.deg2rad(theta)) + 0.00001))
    cv.line(Img, (x1, y1), (x2, y2), (255, 255, 255), 1, 8)

cv.imshow("Hough", Img)
