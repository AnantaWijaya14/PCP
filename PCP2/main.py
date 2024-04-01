# memanggil library opencv
import cv2
from cv2 import waitKey

# menyimpan gambar dengan fungsi imread dari OpenCV
img = cv2.imread("gambar/lena.png") 

# sesuaikan dengan nama file yang diunggah pada cell sebelumnya
# menampilkan gambar dengan fungsi cv2_imshow
cv2.imshow('Lena', img)
waitKey(0)

# lihat tipe data img. disimpan sebagai apa?
print(type(img))
print(img.shape) #menampilkan resolusi
print(img.size) #menampilkan ukuran data pada media penyimpan
print(img.dtype) #image datatype (kedalaman bit)

# Band blue, green dan red masng-masing disimpan pada variabel b,g,r
b, g, r = cv2.split(img)
b = img[...,0] # blue channel
g = img[...,1] # green channel
r = img[...,2] # red channel

cv2.imshow("biru", b); # menampilkan band biru
cv2.imshow("hijau", g); # menampilkan band biru
cv2.imshow("Merah", r); # menampilkan band biru
import cv2
from cv2 import waitKey
img = cv2.imread("gambar/lena.png") 

# konversi BGR dari variable img ke colorspace HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);

# memisahkan hue, saturation dan value
h, s, v = cv2.split(hsv)

# menampilkan band hue
cv2.imshow('Citra HSV', hsv)
waitKey(0)
cv2.imshow('Hasil', img)
waitKey(0)
