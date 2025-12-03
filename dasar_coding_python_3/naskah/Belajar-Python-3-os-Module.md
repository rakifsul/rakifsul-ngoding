# Belajar Python 3 os Module

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_python_3/tree/main/contoh_python3_os_module

## Pendahuluan

os module atau modul os di Python 3 berperan dalam mendapatkan info seputar operating system.

Mulai dari mem-print current working directory hingga me-rename file.

Modul os merupakan modul bawaan dari Python 3 sehingga tidak diperlukan penginstalan package tambahan.

Modul os kemungkinan akan sangat terasa manfaatnya ketika kita sedang membangun aplikasi desktop.

## Lebih Lanjut tentang os Module

Modul os adalah modul bawaan (built-in module) dalam Python yang menyediakan fungsionalitas untuk berinteraksi dengan sistem operasi (Operating System).

Berikut adalah beberapa poin penting tentang modul os di Python 3:

-   Manajemen File dan Direktori: Modul os memungkinkan untuk melakukan berbagai operasi terkait file dan direktori dalam sistem operasi. Ini termasuk pembuatan, penghapusan, pemindahan, penggantian nama, dan pengecekan keberadaan file dan direktori.
-   Manipulasi Path (Jalur): Modul os menyediakan fungsi-fungsi untuk bekerja dengan jalur file dalam sistem operasi yang berbeda. Ini termasuk menggabungkan jalur, memperoleh nama direktori dan nama berkas dari jalur, serta memeriksa keberadaan dan tipe objek yang terkait dengan jalur.
-   Akses Lingkungan Sistem: Modul os memungkinkan untuk mengakses dan memanipulasi variabel-variabel lingkungan sistem. Ini termasuk mengambil nilai variabel lingkungan, menetapkan nilai variabel lingkungan, dan mengatur variabel lingkungan untuk proses-proses Python yang berjalan.
-   Operasi pada Proses: Modul os menyediakan fungsi-fungsi untuk melakukan operasi pada proses-proses yang berjalan dalam sistem operasi. Ini termasuk mendapatkan dan mengatur identifikasi proses (PID), menunggu proses untuk menyelesaikan eksekusi, dan melakukan operasi pada proses seperti mengirim sinyal.
-   Interaksi dengan Sistem Operasi: Modul os memungkinkan untuk berinteraksi dengan sistem operasi dengan berbagai cara, termasuk menjalankan perintah eksternal, mengakses informasi tentang sistem operasi seperti nama host dan informasi jaringan, serta mengontrol perilaku program Python di bawah sistem operasi tertentu.
-   Portabilitas: Modul os dirancang untuk portabilitas lintas-platform, yang berarti kode yang menggunakan modul ini dapat berfungsi di berbagai sistem operasi, termasuk Windows, macOS, dan Linux, tanpa perlu memodifikasi kode secara signifikan.
-   Fungsionalitas Tambahan: Modul os juga menyediakan berbagai fungsi tambahan untuk berbagai tugas, seperti mengatur izin file, mengelola perangkat blok dan karakter, serta melakukan operasi dasar pada sistem berkas.

Secara keseluruhan, modul os di Python 3 adalah alat yang sangat penting dan serbaguna untuk berinteraksi dengan sistem operasi dan melakukan berbagai operasi terkait file, direktori, dan proses dalam pengembangan aplikasi Python.

Dengan fungsionalitasnya yang luas dan portabilitas lintas-platform, modul os membantu dalam pengembangan aplikasi yang dapat berjalan di berbagai lingkungan sistem operasi.

## Tujuan

Tujuan dari tutorial ini adalah:

-   Pembaca mengenal modul os dan dapat menggunakannya sesuai contoh yang diberikan.

## Prasyarat

Prasyarat dari tutorial ini adalah:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Telah meng-install Python versi 3.10.0 dan dapat menjalankannya dari folder manapun.
-   Telah memahami dan bisa mempraktekkan pembuatan project Python 3.

## Langkah-Langkah

Langkah pertama untuk membuat project ini adalah dengan membuat project baru bernama "contoh_python3_os_module".

Anda bisa menggunakan project yang dibuat di "[Belajar Python 3 Cara Membuat Project](https://github.com/rakifsul/belajar_coding_python_3/blob/main/Belajar-Python-3-Cara-Membuat-Project.md)".

Sekarang, seharusnya di folder project sudah ada file main.py.

Replace isinya sedemikan rupa sehingga menjadi seperti ini:

```
# file: main.py

# begin: import modules
import os
# end: import modules

# memprint nama OS
print("os name: ", os.name)

# memprint current working directory
print("current working directory: ", os.getcwd())

# memprint absolute path dari directory saat ini
print("absolute path: ", os.path.abspath('.'))

# melisting files dan sub-directory di directory saat ini
print("list directory: ", os.listdir('.'))

# me-rename file
if os.path.isfile("sample.txt") :
    os.rename("sample.txt","renamed.txt")
elif os.path.isfile("renamed.txt") :
    os.rename("renamed.txt","sample.txt")
```

Selanjutnya, buatlah sebuah file teks bernama "sample.txt" yang tidak harus ada isinya.

Sekarang, jalankan script itu dengan perintah:

```
python main.py
```

Nanti akan tampil output:

```
os name:  nt
current working directory:  D:\Local\Produk\RAKIFSUL\PYTHON\contoh_python3_os_module
absolute path:  D:\Local\Produk\RAKIFSUL\PYTHON\contoh_python3_os_module
list directory:  ['main.py', 'renamed.txt']
```

Hasilnya bisa beda di komputer Anda.

Dan jika Anda perhatikan folder project ini, sample.txt berubah menjadi renamed.txt atau sebaliknya.

## Pembahasan

Kode project tutorial ini dimulai dari mengimpor modul os:

```
# begin: import modules
import os
# end: import modules
```

Kemudian mem-print nama os:

```
# memprint nama OS
print("os name: ", os.name)
```

Kemudian mem-print current working directory:

```
# memprint current working directory
print("current working directory: ", os.getcwd())
```

Kemudian mem-print absolute path dari directory saat ini:

```
# memprint absolute path dari directory saat ini
print("absolute path: ", os.path.abspath('.'))
```

Kemudian me-listing isi dari directory saat ini:

```
# melisting files dan sub-directory di directory saat ini
print("list directory: ", os.listdir('.'))
```

Kemudian me-rename file secara bolak balik (di setiap kali script ini dijalankan):

```
# me-rename file
if os.path.isfile("sample.txt") :
    os.rename("sample.txt","renamed.txt")
elif os.path.isfile("renamed.txt") :
    os.rename("renamed.txt","sample.txt")
```

## Penutup

Sekarang Anda telah diperkenalkan dengan modul os.

Masih banyak method dari modul os yang belum dibahas.

Cek dokumentasinya, kemudian coba sendiri.
