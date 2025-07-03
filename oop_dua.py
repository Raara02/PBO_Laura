class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm 
        self.nilai = {}

    def tambah_nilai(self, mata_kuliah, nilai):
        self.nilai[mata_kuliah] = nilai
        print(f"Nilai {mata_kuliah} untuk {self.nama} ({self.npm}) ditambahkan: {nilai}")

    def lihat_nilai(self):
        print(f"Nilai-nilai {self.nama} ({self.npm}):")
        for mata_kuliah, nilai in self.nilai.items():
            print(f"{mata_kuliah}: {nilai}")
    
class Dosen:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip

    def beri_nilai(self, mahasiswa, mata_kuliah, nilai):
        mahasiswa.tambah_nilai(mata_kuliah, nilai)
        print(f"Dosen {self.nama} ({self.nip}) memberikan nilai {nilai} untuk {mata_kuliah} kepada {mahasiswa.nama} ({mahasiswa.npm})")
        
class KartuRencanaStudi:
    def __init__(self, mata_kuliah, dosen, jumlah_sks):
        self.mata_kuliah = mata_kuliah
        self.dosen = dosen 
        self.jumlah_sks = jumlah_sks
        self.nilai = {}
    
    def ambil_krs(self, mahasiswa, mata_kuliah, jumlah_sks):
        mahasiswa.pilih_matkul(mata_kuliah, jumlah_sks)
        print(f"Mahasiswa {mahasiswa.nama} ({mahasiswa.npm}) mengambil mata kuliah {mata_kuliah} dengan jumlah sks {jumlah_sks} dan diampu dosen {self.dosen.nama}")

# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa("Reza", "2215061087")
mahasiswa2 = Mahasiswa("Laura", "2215061071")
mahasiswa3 = Mahasiswa("Dian", "2215061115")

# Membuat objek Dosen
dosen1 = Dosen("Pak Puput", "123456789")
dosen2 = Dosen("Pak Rio", "222333444")

# Interaksi: Dosen memberikan nilai kepada Mahasiswa
dosen1.beri_nilai(mahasiswa1, "Pemrograman Berorientasi Objek", 90)
dosen1.beri_nilai(mahasiswa2, "Pemrograman Berorientasi Objek", 90)
dosen1.beri_nilai(mahasiswa3, "Pemrograman Berorientasi Objek", 90)

# Mahasiswa melihat nilai mereka
mahasiswa1.lihat_nilai()
mahasiswa2.lihat_nilai()
mahasiswa3.lihat_nilai()

#Mahasiswa ambil krs
mahasiswa1.ambil_krs()
mahasiswa2.ambil.krs()