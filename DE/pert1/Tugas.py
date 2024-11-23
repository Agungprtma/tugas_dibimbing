import time
from abc import ABC, abstractmethod
from multiprocessing import Process

# produk
class Produk(ABC):
    def __init__(self, nama, harga, jumlah):
        self._nama = nama
        self._harga = harga
        self._jumlah = jumlah

    @abstractmethod
    def hitung_total(self):
        pass

    def tampilkan_info(self):
        """Menampilkan informasi produk"""
        print(f"{self._nama} - Harga: {self._harga} x Jumlah: {self._jumlah}")

# Barang
class Barang(Produk):
    def __init__(self, nama, harga, jumlah, kategori):
        super().__init__(nama, harga, jumlah)
        self.kategori = kategori

    def hitung_total(self):
        """Menghitung total harga barang"""
        return self._harga * self._jumlah

# Layanan
class Layanan(Produk):
    def __init__(self, nama, harga, jumlah, durasi):
        super().__init__(nama, harga, jumlah)
        self.durasi = durasi

    def hitung_total(self):
        """Menghitung total harga layanan berdasarkan durasi"""
        return self._harga * self._jumlah * self.durasi

# transaksi
class MesinKasir:
    def __init__(self):
        self.keranjang = []

    def tambah_produk(self, produk):
        """Menambahkan produk ke dalam keranjang belanja"""
        self.keranjang.append(produk)

    def hitung_total(self):
        """Menghitung total harga dari semua produk dalam keranjang"""
        total = sum(produk.hitung_total() for produk in self.keranjang)
        return total

    def cetak_struk(self):
        """Mencetak struk belanja"""
        print("\nStruk Belanja:")
        for produk in self.keranjang:
            produk.tampilkan_info()
        print(f"Total Belanja: {self.hitung_total()}")
        print("-------------------------\n")



# ================================================================
def transaksi_kasir(mesin_kasir, produk):
    mesin_kasir.tambah_produk(produk)
    mesin_kasir.cetak_struk()


def main():
    mesin_kasir = MesinKasir()

    produk1 = Barang("Laptop", 15000000, 2, "Elektronik")
    produk2 = Layanan("Jasa Pemasangan", 500000, 1, 3) 

    p1 = Process(target=transaksi_kasir, args=(mesin_kasir, produk1))
    p2 = Process(target=transaksi_kasir, args=(mesin_kasir, produk2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()
