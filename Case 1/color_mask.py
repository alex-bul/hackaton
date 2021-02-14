import cv2
import numpy
import imutils

if __name__ == '__main__':
    coordinates = []


    def nothing(*arg):
        pass


    cv2.namedWindow("out_window")
    vs = cv2.VideoCapture("src.mp4")

    while True:
        flag, img = vs.read()

        height, width = img.shape[:2]
        edge = 10

        low_green = numpy.array((60, 120, 255), numpy.uint8)
        high_green = numpy.array((70, 125, 255), numpy.uint8)
        try:
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask_blue = cv2.inRange(img_hsv, low_green, high_green)

            # result = cv2.bitwise_and(img_hsv,img_hsv,mask = mask_blue)
            # result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

            moments = cv2.moments(mask_blue, 1)

            dM01 = moments['m01']
            dM10 = moments['m10']
            dArea = moments['m00']

            x = 0
            print(dArea)
            if dArea > 300:
                x = int(dM10 / dArea)
                y = int(dM01 / dArea)
                coordinates.append((x, y))
                cv2.circle(img, (x, y), 10, (0, 0, 255), -1)

            """if (x > (width / 2 + edge)) and x != 0:
                cv2.rectangle(img, (0, 0), (30, height), (0, 255, 0), -1)
            if (x < (width / 2 - edge)) and x != 0:
                cv2.rectangle(img, (width - 30, 0), (width, height), (0, 255, 0), -1)"""

            img = imutils.resize(img, 720, 480)
            cv2.imshow("out_window", img)
        except:
            vs.release()
            raise

        ch = cv2.waitKey(50)

        # close application on esc button pressed
        if ch == 27:
            break
    vs.release()
    cv2.destroyAllWindows()
    print(len(coordinates))
