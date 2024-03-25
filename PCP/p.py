import cv2
import datetime as dt
x = dt.datetime.now()
print(x)

# Ini adalah komentar pada baris python
# Mencetak ke layar menggunakan perintah 'print'
print("hello world")

#Mendefinisikan variabel
x =5
y =6
#Operasi aritmatika sederhana
hasil = x*y+2*x-2*y

#mencetak hasil ke keluaran
print("hasil dari operasi adalah", hasil)


#variabel juga dapat didefinisikan sekaligus, dipisahkan oleh tanda koma
var1,var2, = 23.5, "ini adalah isi var2"

print("isi var 1:",var1, "\n var2", var2)

#Tipe data pada python didefinisikan pada saat variabel dibuat
x = 5       #int
y = 6.5     #float
z  = "Bahasa ular"  #string

hasil = x + y   #penjumlahan antara int dan float
print(hasil)    #mencetak hasil
print(type(hasil)) #Mencetak type data hasil

#cell berikut hanya akan bisa dijalankan
#apanila cell di atas sudah dijalankan sebelumnya

hasil = x + z

#Beberapa tipe data lain pada Python
# Tipe data boolean
trueOrFalse = True
print(trueOrFalse)

#Tipe data arraylist
ar = ['blue','green','red']
print(ar[0]) #array pada Python dimulai dari urutan nol (0)

#Type data dictionary
dic = {'nama buah':'durian',
       'Nama ilmiah':'Durio Zibethinus',
       'asal':'Malaysia',
       'Persebaran':'Asia Tenggara'
       }
print(dic['nama buah'])


# Pernyataan kondisional 
if 5 > 2:
    print("lima lebih dari dua anjay")


# Operand (operasi pengujian) untuk persamaan menggunakan dua tanda sama dengan (==)
x =4
y = (8-x)
if x == y:
    print("x dan y sama")
else:
    print("x dan y beda")

#contoh iterasi. cell di atas (no9) harus dijalankan terlebih dahulu
# agar variabel 'ar' didefinisikan

for isi in ar:
    print(isi)

    


