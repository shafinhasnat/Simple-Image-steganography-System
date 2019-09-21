import cv2
import numpy as np
def decrypt():
    decodedTxt=[]
    a=[]
    b=[]
    length=int(input('enter password:\n'))

    original_img=cv2.imread('pic.png')
    flat_orig_img=original_img.flatten()
    img=cv2.imread('encoded.png')
    flat_img=img.flatten()
##    print(flat_orig_img[:50])
##    print(flat_img[:50])


    sub=np.subtract(flat_orig_img[:length],flat_img[:length])
    for i in range(int(length)):
        if i%2==0:
##            print(sub[i],end='')
            decodedTxt.append(str(sub[i]))

##    print()
##    print(''.join(decodedTxt))
    txt=''.join(decodedTxt)
    rev=txt[:1]+'b'+txt[1:]
##    print(rev)
    n = int(rev, 2)
    print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
    

decrypt()
