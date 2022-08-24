import glob
import cv2

cv2.namedWindow('mahMovie')

# Assumes an ordered sequence of filenames (001.jpg, 002.jpg, etc)
while True:
    for i in range(50, 10000):
        filename = 'animate/{}.png'.format(i)
        img = cv2.imread(filename)
        cv2.imshow('mahMovie', img)
        cv2.waitKey(100)

cv2.destroyAllWindows()