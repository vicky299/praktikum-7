#membuka dan mau membaca file d:/data.txt
file = open("d:/data.txt","r")

#baca baris pertama dari file
#simpan ke dalam fariabel bil1 sbg integer
bil1 = int(file.readline())

#baca baris pertama dari file
#simpan sebagai bil2 sbg integer
bil2 = int(file.readline())

# hitung dan tampilkan hasil bagi
try:
    hasil = bil1/bil2
    print(bil1,' dibagi ',bil2, ' sama dengan ',hasil)
except FileNotFoundError:
    print('file tidak ditemukan')
except ZeroDivisionError:
    print('tidak boleh pembagian dengan nol')
