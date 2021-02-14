import cv2
import numpy
import imutils
import csv

if __name__ == '__main__':
    WINDOW_NAME = "track view"
    acc = 25
    with open("raw_data.txt", "w") as raw_file:
        points = []

        # def nothing(*arg):
        #     pass

        cv2.namedWindow(WINDOW_NAME)
        vs = cv2.VideoCapture("src.mp4")
        zero_point = None
        RATE = 0  # pixels2micrometer
        print("Start program...")

        while True:
            flag, img = vs.read()
            if not flag:
                print("Final of the video", "\n" * 3)
                break

            low_green = numpy.array((55, 120, 255), numpy.uint8)
            high_green = numpy.array((65, 125, 255), numpy.uint8)
            try:
                img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                mask_blue = cv2.inRange(img_hsv, low_green, high_green)

                moments = cv2.moments(mask_blue, 1)

                dM01 = moments['m01']
                dM10 = moments['m10']
                dArea = moments['m00']

                x = 0
                # print(dArea)
                if dArea > 300:
                    x = int(dM10 / dArea)
                    y = int(dM01 / dArea)
                    if not (zero_point):
                        zero_point = (x, y)
                        print("program started")
                    else:
                        if abs(y - prev[1]) < acc and abs(y - zero_point[1]) > 35:
                            if not RATE:
                                RATE = 10 / abs(zero_point[1] - y)
                                # print(x, y)
                                print("Successful calibration!")
                            elif not (points):
                                points.append((x, y))
                            elif abs(points[-1][1] - y) > acc:
                                print(abs(points[-1][1] - y))
                                points.append((x, y))

                    prev = x, y

                    raw_file.write(f"{zero_point[0] - x}\t{zero_point[1] - y}\n")
                    cv2.circle(img, (x, y), 10, (0, 0, 255), -1)

                img = imutils.resize(img, 720, 480)
                cv2.imshow(WINDOW_NAME, img)
            except:
                vs.release()
                raise

            ch = cv2.waitKey(50)

            # close application on esc button pressed
            if ch == 27:
                break
        vs.release()
        cv2.destroyAllWindows()
    if RATE == 0:
        print("You have finished program before calibration.")
        print("Data is invalid")
    print(f"zero point: {zero_point}, coefficient: {RATE}")
    # print(points)

    with open("output.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, ("start_coords", "end_coords", "coefficient", "data"))  #
        writer.writerow(
            {"start_coords": zero_point,
             "end_coords": prev,
             "coefficient": RATE,
             "data": list(map(lambda x: (abs(x[0] - zero_point[0]) * RATE, abs(x[1] - zero_point[1]) * RATE), points))

             }
        )

        """
        
        with open("output.txt", "w") as file:
            file.writelines(
                list(
                    map(
                        lambda x: str(abs(x[0] - zero_point[0]) * RATE) + "\t" + str(
                            abs(x[1] - zero_point[1]) * RATE) + "\n",
                        points)
                )
            )
        """
