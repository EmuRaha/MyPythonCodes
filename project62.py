import cv2


image = cv2.imread("Emupic.jpg")

cv2.imshow("Emu",image)

cv2.waitKey(0)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:

    ret, frame = cap.read()
    cv2.imshow("image", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()





















