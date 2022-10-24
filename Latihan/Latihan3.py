#input nilai variabel
a=input("Masukkan nilai a:")
b=input("Masukkan nilai b:")

#cetak nili variabel
print("variabel a=",a)
print("variabel b=",b)

#cetak kedua hasil variabel dengan string format
print("hasil penggabungan {1} & {0}=%d" .format (a,b) %(a+b))

#konversi nilai variabel
a=int(a)
b=int(b)
print("hasil penjumlahan {1}+{0}=%d" .format (a,b) %(a+b))
print("hasil pembagian {1}/{0}=%d" .format (a,b) %(a/b))