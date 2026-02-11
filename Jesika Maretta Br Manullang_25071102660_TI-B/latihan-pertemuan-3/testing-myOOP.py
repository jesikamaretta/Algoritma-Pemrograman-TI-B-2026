from myOOP import ProdukElektronik, ProdukMakanan, Email, SMS, Mahasiswa

# Inheritance
produk1 = ProdukElektronik("Kipas", "500.000", 3)
produk2 = ProdukMakanan("Martabak", "25.000", "14-02-2026")

print(produk1.info_produk())
print(produk2.info_produk())

# Polymorphism
notif1 = Email()
notif2 = SMS()

print(notif1.kirim())
print(notif2.kirim())

# Encapsulation
mhs = Mahasiswa()

print(mhs.set_nilai(46))
print(mhs.get_nilai())

print(mhs.set_nilai(110))
