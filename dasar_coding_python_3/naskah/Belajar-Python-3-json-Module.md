# Belajar Python 3 json Module

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_python_3/tree/main/contoh_python3_json

## Pendahuluan

JSON adalah suatu format data yang saat ini banyak digunakan dalam web service.

Biasanya saat melakukan suatu request ke web service responnya berupa JSON.

Python bisa melakukan konversi dari atau ke JSON.

Maksudnya, Python bisa mengonversi data JSON ke key-value pair-nya Python (dictionary) atau sebaliknya.

Kali ini, saya akan membahas kedua fungsi tadi.

## Lebih Lanjut tentang json Module

Modul json adalah modul bawaan (built-in module) dalam Python yang menyediakan fungsionalitas untuk bekerja dengan format data JSON (JavaScript Object Notation).

Berikut adalah beberapa poin penting tentang modul json di Python 3:

-   Serialisasi dan Deserialisasi: Modul json memungkinkan untuk mengubah objek Python menjadi format JSON (serialisasi) dan sebaliknya, mengubah string JSON menjadi objek Python (deserialisasi). Ini memungkinkan untuk menyimpan dan memuat data Python ke dan dari format yang bersifat platform-agnostik dan mudah dibaca manusia.
-   Format Data JSON: JSON adalah format data yang ringan, mudah dibaca, dan mudah dipahami oleh manusia. Ini sering digunakan dalam pertukaran data antar sistem dan dalam komunikasi antara aplikasi web dan layanan web.
-   Fungsionalitas Serialisasi: Modul json menyediakan fungsi dump() dan dumps() untuk melakukan serialisasi data Python menjadi string JSON. Fungsi dump() digunakan untuk menulis data JSON ke objek file, sedangkan fungsi dumps() digunakan untuk menghasilkan string JSON langsung.
-   Fungsionalitas Deserialisasi: Modul json juga menyediakan fungsi load() dan loads() untuk melakukan deserialisasi string JSON menjadi objek Python. Fungsi load() digunakan untuk membaca data JSON dari objek file, sedangkan fungsi loads() digunakan untuk mengurai string JSON.
-   Dukungan untuk Tipe Data Python: Modul json mendukung berbagai tipe data Python standar, termasuk string, angka, daftar, tuple, kamus, dan nilai-nilai None. Ini memungkinkan untuk menyimpan dan memuat struktur data kompleks dalam format JSON dengan mudah.
-   Validasi JSON: Modul json juga menyediakan fungsi untuk memvalidasi string JSON, seperti json.JSONDecoder() yang digunakan untuk mem-parsing string JSON secara bertahap dengan kemampuan untuk memvalidasi JSON secara parsial.
-   Kemudahan Penggunaan: Modul json dirancang untuk mudah digunakan dengan antarmuka yang sederhana dan jelas. Ini membuatnya menjadi alat yang berguna untuk bekerja dengan data JSON dalam proyek-proyek Python.

Secara keseluruhan, modul json di Python 3 adalah alat yang penting dan serbaguna untuk bekerja dengan format data JSON dalam pengembangan aplikasi Python.

Dengan kemampuannya untuk melakukan serialisasi dan deserialisasi data dengan mudah, modul json membantu dalam pertukaran data antar sistem dan dalam pengolahan data dalam aplikasi Python.

## Tujuan

Tujuan dari tutorial ini adalah:

-   Pembaca mengenal modul json di Python 3.
-   Pembaca dapat mengonversi JSON ke dictionary Python dan sebaliknya.

## Prasyarat

Prasyarat dari tutorial ini adalah:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Telah meng-install Python versi 3.10.0 dan dapat menjalankannya dari folder manapun.
-   Telah memahami dan bisa mempraktekkan pembuatan project Python 3.

## Langkah-Langkah

Langkah pertama untuk membuat project ini adalah dengan membuat project baru bernama "contoh_python3_json".

Anda bisa menggunakan project yang dibuat di "[Belajar Python 3 Cara Membuat Project](https://github.com/rakifsul/belajar_coding_python_3/blob/main/Belajar-Python-3-Cara-Membuat-Project.md)".

Sekarang, seharusnya di folder project sudah ada file main.py.

Replace isinya sedemikan rupa sehingga menjadi seperti ini:

```
# file: main.py

# begin: import modules
import json
# end: import modules

# memprint teks "json ke python"
print("// json ke python")

# data dalam format json
data_json = '{"nama" : "toko buku", "produk":"buku", "jumlahProduk" : "3"}'

# data barusan dikonversi ke dictionary python
data_di_python = json.loads(data_json)

# print semuanya
print(data_di_python)

# print nama
print(data_di_python["nama"])

# print jumlahProduk
print(data_di_python["jumlahProduk"])

# memprint teks "python ke json"
print("// python ke json")

# data dalam dictionary python
data_python = {
  "nama": "suatu_aplikasi",
  "kode_versi": 40,
  "portable": True,
  "requirement": ("opencv","numpy")
}

# data barusan dikonversi menjadi json
data_di_json = json.dumps(data_python)

# mem-print hasilnya
print(data_di_json)
```

Selanjutnya, jalankan script tadi dengan perintah:

```
python main.py
```

Nanti outputnya akan seperti ini:

```
// json ke python
{'nama': 'toko buku', 'produk': 'buku', 'jumlahProduk': '3'}
toko buku
3
// python ke json
{"nama": "suatu_aplikasi", "kode_versi": 40, "portable": true, "requirement": ["opencv", "numpy"]}
```

## Pembahasan

Script tadi dimulai dari mengimpor modul json:

```
# begin: import modules
import json
# end: import modules
```

Kemudian mem-print judul bagian output:

```
# memprint teks "json ke python"
print("// json ke python")
```

Itu penanda agar output nantinya lebih jelas.

Kemudian, kita membuat string JSON dan memasukkannya ke variabel "data_json":

```
# data dalam format json
data_json = '{"nama" : "toko buku", "produk":"buku", "jumlahProduk" : "3"}'
```

Kemudian, kita mengonversinya ke dictionary Python:

```
# data barusan dikonversi ke dictionary python
data_di_python = json.loads(data_json)
```

Kemudian kita mem-print data tadi:

```
# print semuanya
print(data_di_python)

# print nama
print(data_di_python["nama"])

# print jumlahProduk
print(data_di_python["jumlahProduk"])
```

Sekarang kita melakukan sebaliknya, dari Python ke JSON.

Namun, print dulu judulnya:

```
# memprint teks "python ke json"
print("// python ke json")
```

Selanjutnya, definisikan data JSON dalam bentuk dictionary:

```
# data dalam dictionary python
data_python = {
  "nama": "suatu_aplikasi",
  "kode_versi": 40,
  "portable": True,
  "requirement": ("opencv","numpy")
}
```

Kemudian konversi:

```
# data barusan dikonversi menjadi json
data_di_json = json.dumps(data_python)
```

Kemudian print:

```
# mem-print hasilnya
print(data_di_json)
```

## Penutup

Sekarang, seharusnya Anda sudah memahami modul json di Python 3.

Selanjutnya, sebaiknya Anda mencoba mengonsumsi REST API gratisan dan gunakan method yang telah diajarkan tadi sebagai latihan.
