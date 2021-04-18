import module1
def garis():
    print("=====================================================")
def datang(pelanggan):
    print(f"Selamat Datang di Supermarket {pelanggan}")
    print("Selamat anda adalah pelanggan kami ke-sejuta!!")
    print("Anda dapat memilih 2 dari 5 barang kami")



pelanggan = input("Masukkan nama Anda: ")
garis ()
datang(pelanggan)
garis ()
sabun = module1.barang("1", "1 box Sabun","Lux", "Rp. 50.000")
garis ()
sapu = module1.barang("2", "1 buah Sapu","Nagoya", "Rp. 37.000")
garis ()
panci = module1.barang("3", "1 buah Panci","Maxim", "Rp. 118.000")
garis ()
es_krim = module1.barang("4", "8 liter Es Krim","Campina", "Rp. 206.000")
garis ()
minyak = module1.barang("5", "2 Liter Minyak","Sunco", "Rp. 60.000")
garis ()



n= 0
while n<= 1 :
    kode1 = int(input("Masukkan nomer urutan barang yang ingin anda pilih  : "))
    if kode1 == 1 : 
        print ("Barang yang anda pilih adalah sabun")
        garis ()
        sabun = module1.barang("1", "1 box Sabun","Lux", "Rp. 50.000")
        garis ()
    elif kode1 == 2 :
        print ("Barang yang anda pilih adalah sapu")
        garis ()
        sapu = module1.barang("2", "1 Sapu","Nagoya", "Rp. 37.000")
        garis ()
    elif kode1 == 3 :
        print ("Barang yang anda pilih adalah panci")
        garis ()
        panci = module1.barang("3", "1 buah Panci","Maxim", "Rp. 118.000")
        garis ()
    elif kode1 == 4 :
        print ("Barang yang anda pilih adalah Es Krim")
        garis ()
        es_krim = module1.barang("4", "8 liter Es Krim","Campina", "Rp. 206.000")
        garis ()
    elif kode1 == 5 :
        print ("Barang yang anda pilih adalah Minyak")
        garis ()
        minyak = module1.barang("5", "2 Liter Minyak","Sunco", "Rp. 60.000")
        garis ()
    n = n+1
print ("Terimakasih telah mengunjungi toko kami")


