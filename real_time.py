from paddleocr import PaddleOCR
import cv2
import numpy as np

print("Loading model..........................")
ocr = PaddleOCR(lang="en") 
print("Reading camera.........................")
cap = cv2.VideoCapture(0)
if (cap.isOpened()== False):
    print("Error opening video file")

for i in range(10):
    ret, frame = cap.read()
    
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        result = ocr.ocr(frame)
        print(result)
        if len(result) != 0:
            for line in result:
                # print(line[0][1])
                for box in line:
                    print(box[1][0])
                    x1, y1 = int(box[0][0][0]) , int(box[0][0][1])
                    x4, y4 = int(box[0][2][0]) , int(box[0][2][1])
                    cv2.rectangle(frame,(x1,y1), (x4,y4),(0,255,0),2)
                    cv2.putText(frame, str(box[1][0]),(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()