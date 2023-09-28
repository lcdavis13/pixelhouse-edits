import cv2
import numpy as np
import pixelhouse as ph


canvas_args = {"width": 300, "height": 300, "extent": 4}
delay = 1000
delta_t = 0.1

def simple_circles(time=0.0): # same as small_demos.py but with time argument
    C = ph.Canvas(**canvas_args)

    n = 3
    t = np.arange(0, 2 * np.pi, 2 * np.pi / n) + np.pi / 6 + time
    x, y = np.cos(t), np.sin(t)

    C += ph.circle(x[0], y[0], 2, color=[0, 255, 0], mode="add")
    C += ph.circle(x[1], y[1], 2, color=[255, 0, 0], mode="add")
    C += ph.circle(x[2], y[2], 2, color=[0, 0, 255], mode="add")

    # An example of not saturating the images together
    C += ph.circle(0, 0, 0.50, color=[155, 155, 155])

    return C


def imgshow(img):
    img.show(delay=-1)  # -1 means do not wait, so we can handle that ourselves

    status = cv2.waitKey(delay)

    if status == 27:  # ESC key
        cv2.destroyAllWindows()
        return True
    if cv2.getWindowProperty(img.name, cv2.WND_PROP_VISIBLE) < 1:  # exit button
        return True

    return False

if __name__ == "__main__":
    t = 0.0
    escape = False
    while not escape:
        img = simple_circles(time=t)
        escape = imgshow(img)
        t += delta_t

    # Bugs:
    # if you exit the window instead of key press, it will close but it will continue to wait until the time expires
    # if you press a key, it will immediately progress to the next full frame, instead of calculating actual time difference
    # if computation is long, framerate will effectively lower, and time is tied to framerate, so it will be slower than expected