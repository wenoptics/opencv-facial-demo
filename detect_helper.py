import cv2

face_cascade_default = cv2.CascadeClassifier('etc/haarcascades/haarcascade_frontalface_default.xml')
face_cascade_alt = cv2.CascadeClassifier('etc/haarcascades/haarcascade_frontalface_alt.xml')
face_cascade_alt2 = cv2.CascadeClassifier('etc/haarcascades/haarcascade_frontalface_alt2.xml')
face_cascade_alt_tree = cv2.CascadeClassifier('etc/haarcascades/haarcascade_frontalface_alt_tree.xml')
face_cascade_lbp = cv2.CascadeClassifier('etc/lbpcascades/lbpcascade_frontalface.xml')
# eye_cascade = cv2.CascadeClassifier('etc/haarcascades/haarcascade_eye.xml')

cascade_list = [
    (face_cascade_default, '(haar)face_cascade_default'),
    (face_cascade_alt, '(haar)face_cascade_alt'),
    (face_cascade_alt2, '(haar)face_cascade_alt2'),
    (face_cascade_alt_tree, '(haar)face_cascade_alt_tree'),
    (face_cascade_lbp, '(lbp)face_cascade'),
]


def detect_face_and_draw(img):
    dst_img = img.copy()
    gray = cv2.cvtColor(dst_img, cv2.COLOR_BGR2GRAY)
    for i, (c, cname) in enumerate(cascade_list):
        color = (255, 0, 0)
        if cname == 'face_cascade_lbp':
            color = (0, 255, 0)

        # https://github.com/informramiz/Face-Detection-OpenCV
        faces = c.detectMultiScale(gray, 1.3, 5)

        # Just do some stats
        # print('"%s" found %d face(s)' % (cname, len(faces)))
        text_color = (0, 255, 0) if len(faces) > 0 else (111, 111, 111)
        cv2.putText(dst_img, cname, (3, i * 15 + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, text_color, 1, cv2.LINE_AA)

        for (x, y, w, h) in faces:
            cv2.rectangle(dst_img, (x, y), (x + w, y + h), color, 2)
            # roi_gray = gray[y:y + h, x:x + w]
            # roi_color = dst_img[y:y + h, x:x + w]
            # eyes = eye_cascade.detectMultiScale(roi_gray)
            # for (ex, ey, ew, eh) in eyes:
            #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    return dst_img
