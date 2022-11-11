import cv2
from matplotlib import pyplot as plt
import time

# Connect to the capture device
def take_photo(camera):
    time_t = time.time()
    cv2.imwrite(f'photo{time_t}.jpg', camera)

def photo_capture():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()

        cv2.imshow('Webcam', frame)
        key = cv2.waitKey(1)

        if key == ord('s'):
            take_photo(frame)

        elif key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    photo_capture()
