#Tugas Praktikum2 - Memunculkan satu angka terbesar dari 3 angka

a = int(input ("Masukkan nilai A : "))
b = int(input ("Masukkan nilai B : "))
c = int(input ("Masukkan nilai C : "))
if a > b and  a > c :
    print ("Angka Terbesar adalah A : ",a)
elif b > c :
    print ("Angka Terbesar adalah B : ",b)
else :
    print ("Angka Terbesar adalah C : ",c)