from paddleocr import PaddleOCR, draw_ocr
import cv2
import string
import numpy as np
# Also switch the language by modifying the lang parameter
ocr = PaddleOCR(lang="en") # The model file will be downloaded automatically when executed for the first time
img_path ='aqua_1.jpg'
result = ocr.ocr(img_path)
# Recognition and detection can be performed separately through parameter control
# result = ocr.ocr(img_path, det=False)  Only perform recognition
# result = ocr.ocr(img_path, rec=False)  Only perform detection
# Print detection frame and recognition result
print("================================================")
for res in result:
    print(res)
array = np.array(result)
text = []
for i in range(array.shape[1]):
    res = str(array[:,i,1])
    start = '('
    end = ','
    text.append(res[res.find(start)+len(start):res.rfind(end)])

print(text)

# img = cv2.imread("bienxe.jpg", cv2.IMREAD_COLOR)

# cv2.rectangle(img, )

