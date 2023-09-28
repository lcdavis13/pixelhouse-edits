import cv2
import numpy as np
import pixelhouse as ph


canvas_args = {"width": 300, "height": 300, "extent": 4}


def simple_circles(C, time=0.0):
    n = 3
    t = np.arange(0, 2 * np.pi, 2 * np.pi / n) + np.pi / 6 + time
    x, y = np.cos(t), np.sin(t)

    C += ph.circle(x[0], y[0], 2, color=[0, 255, 0], mode="add")
    C += ph.circle(x[1], y[1], 2, color=[255, 0, 0], mode="add")
    C += ph.circle(x[2], y[2], 2, color=[0, 0, 255], mode="add")

    # An example of not saturating the images together
    C += ph.circle(0, 0, 0.50, color=[155, 155, 155])

    #return C


if __name__ == "__main__":
    img = ph.Canvas(**canvas_args)

    simple_circles(img, time=0.0)
    img.show(delay=-1)

    status = cv2.waitKey(5000)

    if status == 27:  # if ESC is pressed, exit loop
        cv2.destroyAllWindows()
        exit()

    if cv2.getWindowProperty(img.name, cv2.WND_PROP_VISIBLE) < 1:
        exit()

    simple_circles(img, time=10.0)
    img.show(delay=-1)

    status = cv2.waitKey(5000)

    # Bugs: if you exit the window instead of key press, it will close but it will continue to wait until the time expires