'''
program menghitung luas dan keliling lingkaran menggunakan python
'''
pi = 3.14
r = float(input("Masukkan jari-jari lingkaran:"))
l = pi*(r*r)
k = 2*pi*r
print("Luas Lingkaran =","{:.3f}".format(l))
print("Keliling Lingkaran =","{:.3f}".format(k))