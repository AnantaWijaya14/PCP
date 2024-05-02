import cv2

img1 = cv2.imread("Kotak.jpg")
print(img1.shape)
print(img1.dtype)
img2 = cv2.imread("Bundar.jpg")
print(img2.shape)
print(img2.dtype)

#Resize
width = 300
height =300
dim = (width, height)

img1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA)
img2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

#Gray Scaling
imgray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
imgray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Konversi ke Citra Biner
ret,bw1 = cv2.threshold(imgray1,125,255, cv2.THRESH_BINARY)
ret,bw2 = cv2.threshold(imgray2,125,255, cv2.THRESH_BINARY)


op_and = cv2.bitwise_and(bw1,bw2)
op_or = cv2.bitwise_or(bw1,bw2)
op_xor = cv2.bitwise_xor(bw1,bw2)
op_not = cv2.bitwise_not(bw1,bw2)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Hasil And', op_and)
cv2.imshow('Hasil OR', op_or)
cv2.imshow('Hasil XOR', op_xor)
cv2.imshow('Hasil NOT', op_not)
cv2.waitKey()