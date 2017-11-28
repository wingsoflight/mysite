import cv2

cap = cv2.VideoCapture(0)
fcc = cv2.VideoWriter_fourcc(*'h264')
fw = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fh = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter('test.mp4', fcc, fps, (fw, fh), True)
while 1:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
