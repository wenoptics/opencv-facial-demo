import cv2
import time


class calc_time():
    def __init__(self, ):
        self.reset()

    def reset(self):
        self.starttime = 0
        self.endtime = 0

    def start(self):
        self.starttime = time.time()

    def end(self):
        self.endtime = time.time()
        return self.endtime - self.starttime

    def end_and_print(self, _label):
        self.end()
        d = self.endtime - self.starttime
        print('[calc_time "%s"] %f \t fps %.2f' % (_label, d, 1/d))


def resize(mat, dst_width=None, dst_height=None):
    if dst_height is None and dst_width is None:
        raise AttributeError('at least one of the dst args (height and/or width) should be specified')

    h, w, d = mat.shape
    if dst_width is not None and dst_height is None:
        r = dst_width / w
        dst_height = h * r

    elif dst_height is not None and dst_width is None:
        r = dst_height / h
        dst_width = w * r

    else:
        pass

    dst_height = int(dst_height)
    dst_width = int(dst_width)
    return cv2.resize(mat, (dst_width, dst_height))
