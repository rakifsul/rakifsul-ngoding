# Belajar Python 3 Penanganan File

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_python_3/tree/main/contoh_python3_file

## Pendahuluan

Dalam dunia pemrograman, istilah "file" merujuk pada unit penyimpanan data yang dapat diakses dan dikelola oleh sistem komputer.

Sebagai dasar dari manajemen data dalam pengembangan perangkat lunak, pemahaman tentang file menjadi krusial bagi programmer.

Mari kita jelaskan secara rinci.

### Definisi File:

Sebuah file adalah kumpulan data yang disimpan di dalam suatu penyimpanan persisten, seperti hard drive, solid-state drive, atau perangkat penyimpanan lainnya. Setiap file memiliki nama unik dan alamat (path) yang membedakannya dari yang lain. File dapat berisi berbagai jenis informasi, termasuk teks, gambar, audio, video, atau kode program.

### Struktur Dasar File:

Dari sudut pandang pemrograman, file sering kali memiliki struktur dasar, yaitu header dan data.

Header biasanya berisi informasi yang mendefinisikan file, seperti tipe data, ukuran file, dan atribut lainnya.

Data adalah bagian utama yang berisi konten atau informasi yang ingin disimpan.

### Tipe-tipe File:

-   Teks: Berisi data yang dapat dibaca oleh manusia, seperti kode sumber atau dokumen teks.
-   Binary: Berisi data yang hanya dapat dibaca oleh mesin, seperti file eksekusi program atau file gambar.
-   Database: File yang menyimpan data dalam format terstruktur, biasanya digunakan oleh sistem manajemen basis data (DBMS).
-   Konfigurasi: File berisi pengaturan atau konfigurasi untuk program tertentu.
-   Media: File yang berisi data audio, video, atau gambar.

### Operasi Dasar pada File:

-   Membaca (Read): Proses membaca konten dari file ke dalam program.
-   Menulis (Write): Proses menulis atau menyimpan data dari program ke dalam file.
-   Pembuatan (Create): Membuat file baru di sistem.
-   Penghapusan (Delete): Menghapus file dari sistem.
-   Pembaruan (Update): Mengubah atau menambahkan data dalam file yang sudah ada.

Penanganan file adalah skill dasar programmer Python 3 yang harus dikuasai.

Itu karena, file hampir selalu digunakan di berbagai aplikasi.

Mulai dari untuk keperluan konfigurasi hingga hal-hal lainnya.

Penanganan file di Python 3 bisa dibilang memiliki sintaks yang sederhana.

Kata kuncinya adalah "open", "read", "write", dan "close".

Adalah kebiasaan yang baik untuk selalu men-close file setelah di-open.

Selain itu, dalam pengembangan perangkat lunak, pemahaman tentang file sangat penting.

File digunakan untuk menyimpan data, mengelola konfigurasi, dan menyimpan informasi penting lainnya.

Operasi dasar seperti membaca, menulis, membuat, dan menghapus file adalah bagian integral dari banyak aplikasi.

Setiap bahasa pemrograman menyediakan mekanisme untuk bekerja dengan file, dan programmer perlu memahami konsep-konsep dasar seperti pengelolaan akses, pengelolaan kesalahan, dan tipe file yang berbeda.

Pemahaman ini memungkinkan programmer untuk efektif menyimpan, mengelola, dan berinteraksi dengan data melalui file dalam pengembangan perangkat lunak.

Sekarang, saya akan membahasnya.

## Tujuan

Tujuan dari tutorial ini adalah:

-   Pembaca mengenal cara penanganan file di Python 3.

## Prasyarat

Prasyarat dari tutorial ini adalah:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Telah meng-install Python versi 3.10.0 dan dapat menjalankannya dari folder manapun.
-   Telah memahami dan bisa mempraktekkan pembuatan project Python 3.

## Langkah-Langkah

Langkah pertama untuk membuat project ini adalah dengan membuat project baru bernama "contoh_python3_file".

Caranya sudah dijelaskan di "[Belajar Python 3 Cara Membuat Project](https://github.com/rakifsul/belajar_coding_python_3/blob/main/Belajar-Python-3-Cara-Membuat-Project.md)".

Sekarang, seharusnya di folder project sudah ada file "main.py".

Isi "main.py" dengan kode ini:

```
# membuka file dengan parameter bawaan, yakni "rt"
print("open default")

file = open("filename.txt")
print(file.read())
file.close()

# membuka file dengan parameter bawaan, yakni "rt" ditulis secara eksplisit
print("")
print("open read, text")

file = open("filename.txt", "rt")
print(file.read())
file.close()

# membuka file dan membaca dalam bentuk binary
print("")
print("open read, binary")

file = open("filename.txt", "rb")
print(file.read())
file.close()

# menambahkan baris tambahan
file = open("filename.txt", "a")
file.write("\nbaris tambahan")
file.close()

print("")
print("ada baris tambahan")

file = open("filename.txt", "rt")
print(file.read())
file.close()

# menimpa isi file
f = open("filename.txt", "w")
f.write("baris pertama\nbaris kedua\nbaris ketiga\nbaris keempat")
f.close()

print("")
print("replace isi file")

file = open("filename.txt", "rt")
print(file.read())
file.close()
```

Selanjutnya, buatlah file teks bernama "filename.txt" yang isinya:

```
baris pertama
baris kedua
baris ketiga
baris keempat
```

Sekarang, jalankan:

```
python main.py
```

Output-nya:

```
open default
baris pertama
baris kedua
baris ketiga
baris keempat

open read, text
baris pertama
baris kedua
baris ketiga
baris keempat

open read, binary
b'baris pertama\r\nbaris kedua\r\nbaris ketiga\r\nbaris keempat'

ada baris tambahan
baris pertama
baris kedua
baris ketiga
baris keempat
baris tambahan

replace isi file
baris pertama
baris kedua
baris ketiga
baris keempat
```

## Pembahasan

Pada bagian ini, kita membaca file dengan parameter default, yakni "rt".

Karena default, maka "rt" tidak harus ditulis:

```
# membuka file dengan parameter bawaan, yakni "rt"
print("open default")

file = open("filename.txt")
print(file.read())
file.close()
```

Bisa juga ditulis "rt" secara eksplisit seperti ini:

```
# membuka file dengan parameter bawaan, yakni "rt" ditulis secara eksplisit
print("")
print("open read, text")

file = open("filename.txt", "rt")
print(file.read())
file.close()
```

Jika ingin membacanya sebagai binary:

```
# membuka file dan membaca dalam bentuk binary
print("")
print("open read, binary")

file = open("filename.txt", "rb")
print(file.read())
file.close()
```

Adapun, jika ingin menambahkan ujungnya:

```
# menambahkan baris tambahan
file = open("filename.txt", "a")
file.write("\nbaris tambahan")
file.close()

print("")
print("ada baris tambahan")

file = open("filename.txt", "rt")
print(file.read())
file.close()
```

Perhatikan bahwa "\n" pada "\nbaris tambahan" adalah karakter newline.

Sekarang, file kita sudah ditambahkan isinya.

Lalu, bagaimana caranya supaya kembali seperti semula? Begini:

```
# menimpa isi file
f = open("filename.txt", "w")
f.write("baris pertama\nbaris kedua\nbaris ketiga\nbaris keempat")
f.close()

print("")
print("replace isi file")

file = open("filename.txt", "rt")
print(file.read())
file.close()
```

Secara lengkap, parameter kedua dari fungsi open bisa kombinasi dari karakter di bawah ini.

Sebelah kiri:

```
"r" - Read - nilai bawaan. membuka untuk membaca.
"w" - Write - membuka untuk menulis, akan membuat file jika file-nya belum ada.
"a" - Append - membuka untuk menambahkan, akan membuat file jika file-nya belum ada.
"x" - Create - membuat file, mengembalikan error jika file sudah ada.
```

Sebelah kanan:

```
"t" - Text - nilai bawaan. untuk mode teks.
"b" - Binary - untuk mode binary.
```

## Penutup

Sekarang seharusnya Anda mengenal cara penanganan file di Python 3.

Selanjutnya, pelajari lebih banyak lagi tentang file.
