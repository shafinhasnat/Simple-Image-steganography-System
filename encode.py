import cv2
import numpy as np
##import AtoB
def encrypt():
    text=cvtToB()
    a=[]
    img=cv2.imread('pic.png')
    row,col,ch=img.shape
    ##img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    ##print(img.shape)
    flat_img=img.flatten()
    ##print(flat_img[:50])


    for i in text:
        c=[int(i)]
        c.append(0)
        a.append(c)

    flat_txt=np.array(a).flatten()
    print('password:',len(flat_txt))
    zeros=np.zeros((len(flat_img)-len(flat_txt),),dtype=int)
    encoded_txt=np.append(flat_txt,zeros)
    ##print((encoded_txt[:50]))


    encoded_img_flat=np.subtract(flat_img,encoded_txt)
    encoded_img=np.reshape(encoded_img_flat,(row,col,ch))
    cv2.imwrite("encoded.png", encoded_img)
    
def cvtToB():
    text=(input('input your text:\n'))
    txt=bin(int.from_bytes(text.encode(), 'big')).replace('b', '')
##    print(txt)
    return txt

encrypt()
