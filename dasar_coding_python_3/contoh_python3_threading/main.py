# file: main.py

# begin: import modules
import threading
import time
# end: import modules

# buat class PenampungThreading
# kali ini kita meng-extend nya dari threading.Thread
class PenampungThreading(threading.Thread):
    # class constructor
    # inputnya: nama, jeda, dan berapa kali counter berjalan
    def __init__(self, nama, jeda, berapa_kali):
        # panggil constructor parent class: threading.Thread
        threading.Thread.__init__(self)
        # assign nama
        self.nama = nama
        # assign jeda
        self.jeda = jeda
        # assign berapa kali
        self.berapa_kali = berapa_kali

    # override method dari threading.Thread
    def run(self):
        # memprint "Thread Dimulai: namanya"
        print ("Thread Dimulai: " + self.nama)

        # selama berapa_kali lebih besar dari nol
        while self.berapa_kali:
            # terapkan jeda sebesar jeda
            time.sleep(self.jeda)
            # print nama dan berapa kali yang sedang berjalan
            print(self.nama, ":", str(self.berapa_kali))
            # kurangi berapa_kali dengan 1
            self.berapa_kali -= 1
        # setelah keluar dari while
        print ("Thread Selesai: " + self.nama)

# begin: membuat objek PenampungThreading
th1 = PenampungThreading("Thread-1", 2, 5)
th2 = PenampungThreading("Thread-2", 1, 6)
# end: membuat objek PenampungThreading

# begin: mulai thread
th1.start()
th2.start()
# end: mulai thread

# join di sini, tujuannya adalah agar main thread
# atau blok utama dari kode menunggu masing-masing thread selesai
th1.join()
th2.join()

# sekarang kedua thread sudah selesai, ayo keluar dari program.
print ("Keluar dari Main Thread....")

# catatan: Anda boleh coba disable kedua join di atas
# dan lihat efeknya