class Hewan:
    def __init__(self, nama, sifat, ukuran, jumlah_kaki):
        self.nama = nama
        self.sifat = sifat
        self.ukuran = ukuran
        self.jumlah_kaki = jumlah_kaki

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Sifat: {self.sifat}")
        print(f"Ukuran: {self.ukuran}")
        print(f"Jumlah Kaki: {self.jumlah_kaki}")


class Mamalia(Hewan):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_jalan, jenis_mamalia):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_jalan = bisa_jalan
        self.jenis_mamalia = jenis_mamalia

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Bisa Jalan: {self.bisa_jalan}")
        print(f"Jenis Mamalia: {self.jenis_mamalia}")


class Aves(Hewan):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_terbang = bisa_terbang
        self.jenis_aves = jenis_aves

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Bisa Terbang: {self.bisa_terbang}")
        print(f"Jenis Aves: {self.jenis_aves}")


class Ayam(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves, jenis_ayam, bisa_diadu):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
        self.jenis_ayam = jenis_ayam
        self.bisa_diadu = bisa_diadu

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenis Ayam: {self.jenis_ayam}")
        print(f"Bisa Diadu: {self.bisa_diadu}")


# Perulangan untuk memasukkan data beberapa hewan
jumlah_hewan = int(input("Masukkan jumlah hewan yang ingin dimasukkan: "))
daftar_hewan = []

for i in range(jumlah_hewan):
    print(f"\nMasukkan data untuk Hewan ke-{i+1}:")
    nama = input("Nama: ")
    sifat = input("Sifat: ")
    ukuran = input("Ukuran: ")
    jumlah_kaki = int(input("Jumlah Kaki: "))
    bisa_terbang = input("Bisa Terbang (True/False): ").lower() == 'true'

    if bisa_terbang:
        jenis_aves = input("Jenis Aves: ")
        hewan = Aves(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
    else:
        jenis_mamalia = input("Jenis Mamalia: ")
        hewan = Mamalia(nama, sifat, ukuran, jumlah_kaki, True, jenis_mamalia)

    daftar_hewan.append(hewan)

# Menampilkan informasi setiap hewan
print("\nInformasi Hewan:")
for hewan in daftar_hewan:
    hewan.tampilkan_info()
    print("\n" + "="*30 + "\n")