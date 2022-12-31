import cv2
import numpy as np


cap = cv2.VideoCapture(0)


def PIX(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        r, g, b = rgbimg.getpixel((x,y))
        txt = str(r)+","+str(g)+","+str(b)
        bg = np.zeros((200, 400, 3), np.uint8)
        bg[:,0:400] = (b,g,r)
        font = cv2.FONT_ITALIC
        cv2.putText(bg, txt, (10,100), font, 1, (255,255,255), 2, cv2.LINE_AA)
        cv2.imshow('rgb',bg)

while(True):
    ret, frame = cap.read()
    flipped = cv2.flip(frame, 1)
    cv2.imshov('vid', flipped)
    
    if cv2.waitKey(1) & 0xFF == ord('c'): #press 'c' to capture the 
        cv2.imwrite('1.png',flipped)
        imge = Image.open('1.png')
        rgbimg = imge.convert('RGB')
        cv2.imshow('pic',flipped)
        cv2.setMouseCallback('pic', PIX) #function that captures the current pixel and displays on a window
        
    elif cv2.waitKey(1) & 0xFF == ord(' '): #hit space to quit
        break
cap.release()
cv2.destroyAllWindows()

