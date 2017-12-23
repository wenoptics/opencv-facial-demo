import cv2
from detect_helper import detect_face_and_draw
from util.utils import CalcTime, resize

cap = cv2.VideoCapture(0)
ct = CalcTime()
first_run = True

while (True):
    # Reset the timer
    ct.start()

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Resize the frame
    img_rz = resize(frame.copy(), dst_width=480)
    if first_run:
        print('The size working on: %s' % (str(img_rz.shape[:2])))
        first_run = False

    img_face = detect_face_and_draw(img_rz)
    cv2.imshow('detection', img_face)

    # Display the resulting frame
    # cv2.imshow('origin frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Print FPS
    ct.end_and_print('total')

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
