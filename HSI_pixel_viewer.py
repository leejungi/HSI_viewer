import numpy as np
import matplotlib.pyplot as plt
from utils import open_file
import cv2 
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

abs_path = 'Datasets/20210201_HSI_datasets/'
dir_name = 'abalone_hairN/'
path = abs_path + dir_name

im = cv2.imread(path+'image.png')
HSI_data = open_file(path+'data.hdr',path+'data')


def MouseLeftClick(event, x, y, flags, param):
	# 왼쪽 마우스가 클릭되면 (x, y) 좌표를 저장한다.
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([y,x])
        
#        plt.close()
#        for _, point in enumerate(points):
#            y, x = point
        pixel = HSI_data[y:y+1,x:x+1,:]
        pixel_squeezed = np.squeeze(pixel)
        plt.plot(bands, pixel_squeezed)
        

        plt.draw()
#        plt.show()
        
points = []
cv2.namedWindow("image")
cv2.setMouseCallback("image", MouseLeftClick)
bands = np.arange(0,372)

#plt.figure()
plt.xlabel('밴드')
plt.ylabel('반사도')
plt.ylim(0,23000)
plt.grid()

while True:
    cv2.imshow("image", im)
    key = cv2.waitKey(0)
    
    if key == ord('q'):
        break
    
    
cv2.destroyAllWindows()