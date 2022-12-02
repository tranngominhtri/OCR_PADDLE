
from paddleocr import PaddleOCR
import cv2
import numpy as np
# Also switch the language by modifying the lang parameter
ocr = PaddleOCR(lang="en") # The model file will be downloaded automatically when executed for the first time
img_path ='bienxe.jpg'
img = cv2.imread("bienxe.jpg", cv2.IMREAD_COLOR)
result = ocr.ocr(img_path)
# Recognition and detection can be performed separately through parameter control
# result = ocr.ocr(img_path, det=False)  Only perform recognition
# result = ocr.ocr(img_path, rec=False)  Only perform detection
# Print detection frame and recognition result
for line in result:
    print(line[0][1])
    for box in line:
        print(box[1][0])
        x1, y1 = int(box[0][0][0]) , int(box[0][0][1])
        x4, y4 = int(box[0][2][0]) , int(box[0][2][1])
        cv2.rectangle(img,(x1,y1), (x4,y4),(0,255,0),2)
        cv2.putText(img, str(box[1][0]),(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)




cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# boxes = result
# point_1 = boxes[0][0][0]
# point_2 = boxes[0][0][1]
# point_3 = boxes[0][0][2]
# point_4 = boxes[0][0][3]

# # txts = [line[1][0] for line in result]
# # scores = [line[1][1] for line in result]
 
# # for box in boxes:    
# #     top_left     = (int(box[0]), int(box[1]))
# #     bottom_right = (int(box[2]), int(box[3]))
# #     cv2.rectangle(mat, top_left, bottom_right, (0, 255, 0), 2)
# cv2.circle(mat,(int(point_1[0]), int(point_1[1])),2,(0,255,0),2)
# cv2.circle(mat,(int(point_2[0]), int(point_2[1])),2,(0,255,0),2)
# cv2.circle(mat,(int(point_3[0]), int(point_3[1])),2,(0,255,0),2)
# cv2.circle(mat,(int(point_4[0]), int(point_4[1])),2,(0,255,0),2)


