import cv2
import numpy as np
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-o","--original",required=True, help="original image file")
ap.add_argument("-e","--encoded",required=True, help="encoded image file")

args=vars(ap.parse_args())
def decrypt():
    decodedTxt=[]
    a=[]
    b=[]
    length=int(input('enter password:\n'))

    original_img=cv2.imread(args["original"])
    flat_orig_img=original_img.flatten()
    img=cv2.imread(args["encoded"])
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
