# Image steganography system

This project is a steganography tool that can hide or encode a massage inside the pixels of an image that can be decoded without losing image quality. To have a user experience, visit here: [XELSTEG webapp](https://xelsteg.herokuapp.com)

## Download

Download the repository using the command below-

```
git clone https://github.com/shafinhasnat/Simple-Image-steganography-System.git
```

## Usage
This is a command line software. It needs a source image to be encoded, and an encoded image name. To encode any message, type- 
```
python encode.py --input <<input image name>> --output <<encoded image name>>
```
This will ask for your secret message and returns a password for decryption.


To decode the message, it needs the source image and the encoded image. To decode the message-
```
python decode.py --original <<original image name>> --encoded <<encoded image name>>
```
It will ask for the password. Then it will show the hidden message.



## Dependencies

```
pip install opencv-python
```
