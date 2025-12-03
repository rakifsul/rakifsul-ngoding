# file: pengguna_modul_sendiri.py

# import modul sendiri: contoh_modul_sendiri
# kemudian ambil fungsi nama_modul_saya
from contoh_modul_sendiri import nama_modul_saya

# jalankan fungsi nama_modul_saya
# maka hanya ada satu baris teks,
# karena eksekusi kode di bagian terbawah script contoh_modul_sendiri.py
# terproteksi oleh:
# if __name__ == "__main__":
# pada script contoh_modul_sendiri.py
nama_modul_saya()