# Belajar Python 3 Modul \_thread

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_python_3/tree/main/contoh_python3_thread

## Pendahuluan

Pada penerapannya, seringkali terjadi bahwa aplikasi desktop harus mengerjakan lebih dari satu task secara bersamaan.

Sebagai contoh, dalam aplikasi text editor, sistem harus mengecek spelling error sementara user tetap mengetik.

Python 3 memilik solusi untuk ini, yakni dengan modul \_thread.

Bagaimana cara penggunaannya, mari simak...

## Lebih Lanjut tentang Modul \_thread

Modul \_thread adalah modul bawaan (built-in module) dalam Python yang menyediakan fungsionalitas untuk pemrograman konkuren atau multi-threading.

Berikut adalah beberapa poin penting tentang modul \_thread di Python 3:

-   Pendukung Multi-Threading: Modul \_thread menyediakan fungsionalitas untuk membuat dan mengelola thread-thread (utas-utas) dalam program Python. Thread-thread ini memungkinkan eksekusi konkuren dari beberapa tugas dalam program yang sama, meningkatkan responsifitas dan kinerja aplikasi.
-   API Dasar Thread: Modul \_thread menyediakan API dasar untuk membuat dan mengelola thread-thread dalam program Python. Ini termasuk fungsi start_new_thread() yang digunakan untuk membuat thread baru, serta fungsi-fungsi untuk mengontrol thread seperti exit(), allocate_lock(), dan lain-lain.
-   Kontrol Terhadap Penguncian (Locking): Modul \_thread juga menyediakan fungsionalitas untuk mengontrol penguncian (locking) dalam program Python menggunakan objek kunci (lock objects). Ini digunakan untuk menghindari persaingan antar thread terhadap sumber daya bersama yang digunakan dalam program.
-   Peringatan Penggunaan Langsung: Perlu diperhatikan bahwa modul \_thread cenderung menyediakan antarmuka yang lebih rendah tingkat (low-level interface) untuk pemrograman konkuren di Python. Oleh karena itu, biasanya disarankan untuk menggunakan modul threading, yang menyediakan antarmuka yang lebih tinggi tingkat (high-level interface), lebih aman, dan lebih mudah digunakan.
-   Keterbatasan pada Global Interpreter Lock (GIL): Perlu diingat bahwa Python memiliki Global Interpreter Lock (GIL) yang membatasi eksekusi konkuren dari kode Python dalam satu proses. Ini berarti bahwa meskipun menggunakan thread-thread, proses Python secara efektif hanya dapat menjalankan satu thread pada waktu tertentu.
-   Dukungan untuk Pengembangan Aplikasi Berskala Kecil: Modul \_thread berguna dalam pengembangan aplikasi kecil yang membutuhkan konkurensi sederhana, seperti aplikasi sederhana yang memperbarui tampilan GUI dalam thread terpisah atau aplikasi yang menangani permintaan HTTP dalam thread terpisah.

Secara keseluruhan, modul \_thread di Python 3 menyediakan fungsionalitas dasar untuk pemrograman konkuren atau multi-threading dalam program Python.

Meskipun dapat berguna dalam skenario tertentu, disarankan untuk menggunakan modul threading yang lebih aman dan mudah digunakan dalam pengembangan aplikasi Python modern.

## Tujuan

Tujuan dari tutorial ini adalah:

-   Pembaca mengenal modul \_thread dan dapat menggunakannya sesuai contoh yang diberikan.

## Prasyarat

Prasyarat dari tutorial ini adalah:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Telah meng-install Python versi 3.10.0 dan dapat menjalankannya dari folder manapun.
-   Telah memahami dan bisa mempraktekkan pembuatan project Python 3.

## Langkah-Langkah

Langkah pertama untuk membuat project ini adalah dengan membuat project baru bernama "contoh_python3_thread".

Anda bisa menggunakan project yang dibuat di "[Belajar Python 3 Cara Membuat Project](https://github.com/rakifsul/belajar_coding_python_3/blob/main/Belajar-Python-3-Cara-Membuat-Project.md)".

Sekarang, seharusnya di folder project sudah ada file main.py.

Replace isinya sedemikan rupa sehingga menjadi seperti ini:

```
# file: main.py

# begin: import modules
import _thread
import time
# end: import modules

# buat class PenampungThread
# walaupun kita tidak sedang menggunakan modul threading.Thread, ini juga bisa
class PenampungThread:

    # class constructor dengan input nama thread
    def __init__(self, nama_thread):
        # assign nama
        self.nama = nama_thread

    # method ini dijalankan dengan thread
    # jeda adalah waktu jedanya
    def run(self, jeda):
        # counter
        ctr = 0

        # sampai selama mungkin
        while 1:
            # terapkan jeda sebesar jeda
            time.sleep(jeda)
            # print nama thread dan counter nya
            print(self.nama, ":", str(ctr))
            # naikkan counter
            ctr+=1

# begin: membuat objek PenampungThread
th1 = PenampungThread("thread-a")
th2 = PenampungThread("thread-b")
# end: membuat objek PenampungThread

try:
      # begin: mulai thread
      _thread.start_new_thread(th1.run, (2,))
      _thread.start_new_thread(th2.run, (4,))
      # end: mulai thread
except:
      # kalau thread tidak bisa dijalankan
      print ("Error: tidak bisa memulai thread")

# mencegah program keluar sebelum thread berjalan
while 1:
      pass
```

Selanjutnya, jalankan:

```
python main.py
```

Nanti akan muncul output semacam ini:

```
thread-a : 0
thread-b : 0
thread-a : 1
thread-a : 2
thread-b : 1
thread-a : 3
thread-a : 4
thread-b : 2
thread-a : 5
thread-a : 6
thread-b : 3
thread-a : 7
thread-a : 8
thread-b : 4
thread-a : 9
thread-a : 10
thread-b : 5
thread-a : 11
thread-a : 12
thread-b : 6
thread-a : 13
```

Output tersebut akan terus berjalan hingga kita menekan control + c.

Jadi tekan key tersebut untuk menghentikannya.

Setelah berhenti, kita bisa membaca dari output bahwa thread-a dan thread-b berjalan bersamaan berdasarkan angka yang muncul.

Terlihat bahwa thread-a lebih cepat karena angkanya naik lebih dulu daripada thread-b.

## Pembahasan

Aplikasi ini bermula dari meng-import modul-modul ini:

```
# begin: import modules
import _thread
import time
# end: import modules
```

Modul \_thread untuk threading dan modul time untuk menerapkan jeda.

Selanjutnya, kita membuat class PenampungThread untuk membungkus task yang akan di-threading-kan:

```
# buat class PenampungThread
# walaupun kita tidak sedang menggunakan modul threading.Thread, ini juga bisa
class PenampungThread:
```

Pada constructor-nya, kita memberi nama pada thread tersebut:

```
# class constructor dengan input nama thread
    def __init__(self, nama_thread):
        # assign nama
        self.nama = nama_thread
```

Dan ini adalah tugasnya saat threading berjalan:

```
# method ini dijalankan dengan thread
    # jeda adalah waktu jedanya
    def run(self, jeda):
        # counter
        ctr = 0

        # sampai selama mungkin
        while 1:
            # terapkan jeda sebesar jeda
            time.sleep(jeda)
            # print nama thread dan counter nya
            print(self.nama, ":", str(ctr))
            # naikkan counter
            ctr+=1
```

while 1 artinya loop ini akan berjalan selama aplikasi belum dihentikan.

class berakhir di situ, sekarang di scope baru, kita membuat objek penampung thread dan menjalankan keduanya bersamaan:

```
# begin: membuat objek PenampungThread
th1 = PenampungThread("thread-a")
th2 = PenampungThread("thread-b")
# end: membuat objek PenampungThread

try:
      # begin: mulai thread
      _thread.start_new_thread(th1.run, (2,))
      _thread.start_new_thread(th2.run, (4,))
      # end: mulai thread
except:
      # kalau thread tidak bisa dijalankan
      print ("Error: tidak bisa memulai thread")
```

Terakhir, kita harus cegah aplikasi dihentikan secara otomatis:

```
# mencegah program keluar sebelum thread berjalan
while 1:
      pass
```

## Penutup

Sekarang seharusnya Anda telah memahami cara threading dengan modul \_thread.

Selanjutnya terserah Anda...
