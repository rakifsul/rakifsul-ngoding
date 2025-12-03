# Belajar Python 3 Modul threading

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_python_3/tree/main/contoh_python3_threading

## Pendahuluan

Pada penerapannya, seringkali terjadi bahwa aplikasi desktop harus mengerjakan lebih dari satu task secara bersamaan.

Sebagai contoh, dalam aplikasi text editor, sistem harus mengecek spelling error sementara user tetap mengetik.

Python 3 memilik solusi untuk ini selain modul \_thread yang telah dijelaskan di tutorial ini, yakni dengan modul threading.

Bagaimana cara penggunaannya, mari simak...

## Lebih Lanjut tentang Modul threading

Modul threading di Python 3 menyediakan antarmuka tingkat tinggi untuk membuat dan mengelola thread.

Thread adalah unit kecil dari proses yang dapat berjalan secara bersamaan.

Penggunaan thread dalam Python memungkinkan program untuk melakukan tugas-tugas yang memerlukan waktu lama atau operasi I/O secara bersamaan, meningkatkan kinerja dan responsifitas aplikasi.

Beberapa fitur utama dari modul threading di Python 3 meliputi:

-   Pembuatan Thread: Modul threading memungkinkan Anda membuat thread baru dengan membuat objek Thread dan menentukan fungsi yang akan dieksekusi oleh thread tersebut.
-   Synchronizing Threads: Modul ini menyediakan berbagai mekanisme sinkronisasi seperti Locks, Semaphores, dan Conditions untuk menghindari race conditions ketika beberapa thread mengakses data bersama.
-   Daemon Threads: Anda dapat membuat thread sebagai "daemon" yang akan berhenti secara otomatis ketika program utama berhenti.
-   Joining Threads: Anda dapat menggunakan metode join() untuk menunggu sampai sebuah thread selesai dieksekusi sebelum melanjutkan eksekusi program utama.
-   Timer Threads: Modul ini juga menyediakan kelas Timer yang memungkinkan Anda menjadwalkan eksekusi suatu fungsi dalam waktu tertentu.
-   Thread Pooling: Anda dapat menggunakan kelas ThreadPoolExecutor untuk membuat pool thread yang dapat digunakan untuk mengeksekusi banyak tugas secara paralel.

## Tujuan

Tujuan dari tutorial ini adalah:

-   Pembaca mengenal modul threading dan dapat menggunakannya sesuai contoh yang diberikan.

## Prasyarat

Prasyarat dari tutorial ini adalah:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Telah meng-install Python versi 3.10.0 dan dapat menjalankannya dari folder manapun.
-   Telah memahami dan bisa mempraktekkan pembuatan project Python 3.

## Langkah-Langkah

Langkah pertama untuk membuat project ini adalah dengan membuat project baru bernama "contoh_python3_threading".

Anda bisa menggunakan project yang dibuat di "[Belajar Python 3 Cara Membuat Project](https://github.com/rakifsul/belajar_coding_python_3/blob/main/Belajar-Python-3-Cara-Membuat-Project.md)".

Sekarang, seharusnya di folder project sudah ada file main.py.

Replace isinya sedemikan rupa sehingga menjadi seperti ini:

```
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

# begin: membuat objek PenampungThread
th1 = PenampungThreading("Thread-1", 2, 5)
th2 = PenampungThreading("Thread-2", 1, 6)
# end: membuat objek PenampungThread

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
```

Selanjutnya, jalankan:

```
python main.py
```

Nanti akan muncul output semacam ini:

```
Thread Dimulai: Thread-1
Thread Dimulai: Thread-2
Thread-2 : 6
Thread-1 : 5
Thread-2 : 5
Thread-2 : 4
Thread-1 : 4
Thread-2 : 3
Thread-2 : 2
Thread-1 : 3
Thread-2 : 1
Thread Selesai: Thread-2
Thread-1 : 2
Thread-1 : 1
Thread Selesai: Thread-1
Keluar dari Main Thread....
```

Output tersebut akan terus berjalan hingga selesai dengan sendirinya.

Setelah berhenti, kita bisa membaca dari output bahwa Thread-1 dan Thread-2 berjalan bersamaan berdasarkan angka yang muncul.

Terlihat bahwa Thread-2 lebih cepat karena selesai lebih dulu.

## Pembahasan

Aplikasi ini bermula dari meng-import modul-modul ini:

```
# begin: import modules
import threading
import time
# end: import modules
```

Modul threading untuk threading dan modul time untuk menerapkan jeda.

Selanjutnya, kita membuat class PenampungThreading yang diturunkan dari threading.Thread untuk membungkus task yang akan di-threading-kan:

```
# buat class PenampungThreading
# kali ini kita meng-extend nya dari threading.Thread
class PenampungThreading(threading.Thread):
```

Pada constructor-nya, kita memberi nama thread, jeda, dan berapa kali hitungan task-nya akan berjalan:

```
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
```

Dan ini adalah tugasnya saat threading berjalan:

```
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
```

while self.berapa_kali artinya loop ini akan berjalan selama variabel berapa_kali belum mencapai nol. Ingat bahwa nilai berapa_kali dikurangi satu setiap loop.

class berakhir di situ, sekarang di scope baru, kita membuat objek penampung threading dan menjalankan keduanya bersamaan:

```
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
```

Karena join fungsinya analog dengan while 1 di pembahasan modul \_thread, maka kita tidak perlu menambahkan while 1 lagi di bagian terbawah script.

Sebagai pembanding, coba comment-kan kedua join di atas.

## Penutup

Sekarang seharusnya Anda telah memahami cara threading dengan modul threading.

Selanjutnya terserah Anda...
