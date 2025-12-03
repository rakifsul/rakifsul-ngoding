# Belajar Python 3 Modul sys

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_python_3/tree/main/contoh_python3_sys

## Pendahuluan

Modul sys adalah modul yang berisi variabel dan fungsi yang berkaitan dengan interpreter Python.

## Lebih Lanjut tentang Modul sys

Modul sys adalah modul bawaan (built-in module) dalam Python yang menyediakan akses ke beberapa variabel dan fungsi yang berinteraksi dengan interpretasi Python dan sistem operasi yang mendasarinya.

Berikut adalah beberapa poin penting tentang modul sys di Python 3:

-   Akses ke Argumen Command Line: Modul sys memungkinkan untuk mengakses argumen yang diberikan pada command line saat menjalankan skrip Python. Variabel sys.argv adalah daftar argumen baris perintah yang diberikan, termasuk nama skrip itu sendiri.
-   Fungsi Interaksi dengan Interpreter: Modul sys menyediakan beberapa fungsi yang memungkinkan untuk berinteraksi dengan interpreter Python. Misalnya, fungsi sys.exit() digunakan untuk menghentikan eksekusi program secara instan dengan memberikan kode keluaran yang spesifik.
-   Akses ke Variabel dan Fungsi Penting: Modul sys menyediakan akses ke beberapa variabel dan fungsi yang penting untuk informasi dan kontrol eksekusi program. Misalnya, sys.version memberikan informasi tentang versi Python yang sedang digunakan, dan sys.platform memberikan informasi tentang platform sistem operasi yang sedang digunakan.
-   Fungsi Penanganan Eksepsi: Modul sys juga menyediakan beberapa fungsi untuk menangani eksepsi (exceptions). Misalnya, sys.exc_info() digunakan untuk mendapatkan informasi tentang eksepsi saat ini yang sedang ditangani.
-   Pengaturan Konfigurasi Sistem: Modul sys memungkinkan untuk mengatur dan mengakses konfigurasi sistem yang lebih dalam. Misalnya, sys.path adalah daftar direktori yang digunakan oleh Python untuk mencari modul yang diimpor.
-   Kontrol Terhadap Garis Besar Program: Modul sys juga memberikan beberapa fungsi dan variabel yang memungkinkan untuk mengontrol dan mengawasi perilaku program secara keseluruhan. Misalnya, sys.stdin, sys.stdout, dan sys.stderr adalah objek yang terkait dengan input standar, output standar, dan error standar dari sebuah program Python.

Secara keseluruhan, modul sys di Python 3 adalah alat yang sangat penting dan serbaguna yang menyediakan akses ke informasi sistem, kontrol eksekusi program, dan fungsi-fungsi penting lainnya yang diperlukan dalam pengembangan aplikasi Python.

## Tujuan

Tujuan dari tutorial ini adalah:

-   Pembaca mengenal modul sys.

## Prasyarat

Prasyarat dari tutorial ini adalah:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Telah meng-install Python versi 3.10.0 dan dapat menjalankannya dari folder manapun.
-   Telah memahami dan bisa mempraktekkan pembuatan project Python 3.

## Langkah-Langkah

Langkah pertama untuk membuat project ini adalah dengan membuat project baru bernama "contoh_python3_sys".

Caranya sudah dijelaskan di "[Belajar Python 3 Cara Membuat Project](https://github.com/rakifsul/belajar_coding_python_3/blob/main/Belajar-Python-3-Cara-Membuat-Project.md)".

Sekarang, seharusnya di folder project sudah ada file main.py.

Isi main.py dengan kode ini:

```
# begin: import module
import sys
# end: import module

# mem-print command line argument
print(sys.argv)

# mem-print versi Python
print(sys.version)

# mem-print versi Python yang lebih detail
print(sys.version_info)

# mem-print path pencarian dari modul
print(sys.path)

countRef = "sesuatu"

# mem-print jumlah referensi variabel "countRef"
print(sys.getrefcount(countRef))

# standard input
for row in sys.stdin:
	if "quit" == row.lstrip().rstrip():
		break
	print("input: ", row)

print("keluar")

# keluar aplikasi
sys.exit()

# karena sudah keluar aplikasi, teks di bawah tidak muncul
print("tidak muncul.")
```

Sekarang, jalankan:

```
python main.py
```

Output-nya:

```
['main.py']
3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)]
sys.version_info(major=3, minor=10, micro=11, releaselevel='final', serial=0)
['D:\\Local\\Produk\\RAKIFSUL\\PYTHON\\Dasar\\NEXT\\paket_project_python3_dasar_next\\contoh_python3_sys', 'C:\\Install\\Python\\WPy64-310111\\python-3.10.11.amd64\\python310.zip', 'C:\\Install\\Python\\WPy64-310111\\python-3.10.11.amd64\\DLLs', 'C:\\Install\\Python\\WPy64-310111\\python-3.10.11.amd64\\lib', 'C:\\Install\\Python\\WPy64-310111\\python-3.10.11.amd64', 'C:\\Install\\Python\\WPy64-310111\\python-3.10.11.amd64\\lib\\site-packages']
4
```

Jika di titik ini Anda meng-input-kan karakter, maka karakter tersebut akan di-print.

Jika di titik tadi Anda menulis "quit", maka aplikasi akan keluar.

## Pembahasan

Pada bagian ini, kita meng-import modul sys:

```
# begin: import module
import sys
# end: import module
```

Pada bagian ini, kita mem-print argumen dari command line:

```
# mem-print command line argument
print(sys.argv)
```

Jika kita menjalankan "python main.py" maka hanya keluar 1 elemen dari array di output-nya, yakni "main.py".

Jika kita menjalankan "python main.py 1 2 3" maka yang keluar adalah array berisi elemen ["main.py", "1", "2", "3"].

Pada bagian ini, kita mem-print versi Python:

```
# mem-print versi Python
print(sys.version)
```

Pada bagian ini, kita mem-print versi Python secara lebih detail:

```
# mem-print versi Python yang lebih detail
print(sys.version_info)
```

Pada bagian ini, kita memprint path pencarian dari modul:

```
# mem-print path pencarian dari modul
print(sys.path)
```

Pada bagian ini, kita mem-print jumlah referensi variabel "countRef":

```
countRef = "sesuatu"

# mem-print jumlah referensi variabel "countRef"
print(sys.getrefcount(countRef))
```

Tentu bukan hanya variabel yang bernama countRef. Variabel dengan nama lain juga bisa, asalkan disesuaikan dengan parameter dari method sys.getrefcount -nya.

Pada bagian ini, kita menerima input dan mem-print-nya. Jika input adalah "quit" maka keluar dari aplikasi:

```
# standard input
for row in sys.stdin:
	if "quit" == row.lstrip().rstrip():
		break
	print("input: ", row)
```

Pada bagian ini, kita keluar aplikasi secara paksa. Menyebabkan print terbawah tidak keluar output-nya:

```
# keluar aplikasi
sys.exit()

# karena sudah keluar aplikasi, teks di bawah tidak muncul
print("tidak muncul.")
```

## Penutup

Sekarang seharusnya Anda paham dengan apa yang saya jelaskan tadi.

Sekarang, cobalah buka dokumentasi Python 3 tentang modul sys dan coba method atau variabel yang belum dicontohkan di tutorial ini.
