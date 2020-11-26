import numpy as np
import cv2

daisy = cv2.imread("img/daisy.jpg", 1)
cv2.imshow("Daisy", daisy)
cv2.moveWindow("Daisy",0,0)
print(daisy.shape)
height,width,channels = daisy.shape

b,g,r = cv2.split(daisy)
rgb_split = np.empty([height,width*3, 3], 'uint8')

rgb_split[:, 0:width] = cv2.merge([b,b,b])
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])

cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)

cv2.waitKey(0)
cv2.destroyAllWindows()