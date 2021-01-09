import cv2
import numpy


class Camera:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

    def encode_image(self):
        ret, frame = self.capture.read()
        result, encoded_image = cv2.imencode('.jpg', frame, self.encode_param)
        camera_array = numpy.array(encoded_image).tolist()
        return camera_array
