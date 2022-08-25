import glob
import cv2


while True:
    for i in range(2, 10000):
        try:
            filename = 'animate/{}.png'.format(i)
            print(filename)
            img = cv2.imread(filename)
            cv2.imshow('pic', img)
            cv2.waitKey(100)
        except:
            break

cv2.destroyAllWindows()