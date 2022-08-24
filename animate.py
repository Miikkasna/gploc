import glob
import cv2

cv2.namedWindow('mahMovie')

# Assumes an ordered sequence of filenames (001.jpg, 002.jpg, etc)
while True:
    for filename in sorted(glob.glob('./animate/*.png')):
        img = cv2.imread(filename)
        cv2.imshow('mahMovie', img)
        cv2.waitKey(30)

cv2.destroyAllWindows()