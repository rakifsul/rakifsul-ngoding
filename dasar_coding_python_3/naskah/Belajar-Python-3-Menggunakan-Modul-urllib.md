# Belajar Python 3 Menggunakan Modul urllib

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_python_3/tree/main/contoh_python3_urllib

## Pendahuluan

Di Python 3, untuk menangani URL diperlukan sebuah modul.

Modul itu adalah urllib.

Selain untuk menangani URL, urllib juga bisa digunakan untuk membuat request.

Dengan kata lain kita bisa mendownload content dari suatu URL untuk diterima oleh aplikasi yang mengirimkan request-nya.

Di tutorial ini, kita akan menggunakan urllib untuk melakukan request ke:

https://quotes.toscrape.com

Kemudian mem-print response-nya.

## Lebih Lanjut tentang Modul urllib

Modul urllib adalah modul bawaan (built-in module) dalam Python yang menyediakan fungsionalitas untuk berinteraksi dengan URL (Uniform Resource Locator) dan melakukan berbagai operasi terkait dengan protokol HTTP (Hypertext Transfer Protocol).

Berikut adalah beberapa poin penting tentang modul urllib di Python 3:

-   Akses ke URL: Modul urllib memungkinkan untuk membuka dan membaca konten dari URL. Ini termasuk mengambil data dari halaman web, API, atau sumber data lain yang tersedia secara online.
-   Protokol HTTP: Modul urllib mendukung berbagai operasi terkait protokol HTTP, seperti GET, POST, PUT, DELETE, dan lain-lain. Ini memungkinkan untuk mengirim permintaan HTTP ke server dan menerima respons dari server sesuai dengan metode yang diinginkan.
-   Operasi Pengambilan Data: Modul urllib memungkinkan untuk mengambil data dari URL menggunakan fungsi-fungsi seperti urllib.request.urlopen(). Ini memungkinkan untuk membuka dan membaca konten dari URL yang diberikan dengan mudah dalam kode Python.
-   Manajemen Permintaan dan Respons: Modul urllib juga menyediakan kemampuan untuk mengelola permintaan dan respons HTTP. Ini termasuk menambahkan header ke permintaan, menangani kode status respons, membaca konten respons, dan melakukan operasi terkait dengan respons HTTP.
-   Kemampuan Penanganan URL: Modul urllib dapat digunakan untuk memanipulasi URL dengan berbagai cara. Ini termasuk memecah URL menjadi bagian-bagian yang berbeda, mengonversi karakter-karakter URL yang bersifat khusus, dan membangun kembali URL dari bagian-bagian yang terpisah.
-   Dukungan untuk Proxy: Modul urllib juga menyediakan dukungan untuk konfigurasi dan penggunaan proxy saat melakukan akses ke URL. Ini memungkinkan untuk mengakses sumber daya online melalui server proxy dengan mudah dalam kode Python.
-   Keamanan dan Validasi URL: Modul urllib juga dapat digunakan untuk melakukan validasi dan penanganan URL yang aman. Ini termasuk memastikan bahwa URL yang digunakan valid, menghindari ancaman keamanan seperti serangan injeksi, dan menangani URL yang bersifat dinamis dengan benar.

Secara keseluruhan, modul urllib di Python 3 adalah alat yang sangat penting dan serbaguna untuk berinteraksi dengan URL dan melakukan berbagai operasi terkait dengan protokol HTTP dalam pengembangan aplikasi Python.

Dengan fungsionalitasnya yang luas dan fleksibilitasnya yang tinggi, modul urllib membantu dalam mengakses dan memanipulasi sumber daya online dengan mudah dan aman.

## Tujuan

Tujuan dari tutorial ini adalah:

-   Pembaca mampu melakukan request dengan urllib.
-   Pembaca mampu mem-print response dari request tersebut.

## Prasyarat

Prasyarat dari tutorial ini adalah:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Telah meng-install Python versi 3.10.0 dan dapat menjalankannya dari folder manapun.
-   Telah memahami dan bisa mempraktekkan pembuatan project Python 3.

## Langkah-Langkah

Langkah pertama untuk membuat project ini adalah dengan membuat project baru bernama "contoh_python3_urllib".

Anda bisa menggunakan project yang dibuat di "[Belajar Python 3 Cara Membuat Project](https://github.com/rakifsul/belajar_coding_python_3/blob/main/Belajar-Python-3-Cara-Membuat-Project.md)".

Sekarang, seharusnya di folder project sudah ada file main.py.

Replace isinya sedemikan rupa sehingga menjadi seperti ini:

```
# file: contoh_modul_urllib.py

# begin: import modules
import urllib.request
# end: import modules

# memprint teks: "mulai contoh 1"
print("mulai contoh 1")

# membuka halaman homepage dari https://quotes.toscrape.com
html = urllib.request.urlopen('https://quotes.toscrape.com').read()
# memprint outputnya.
print(html)

# memprint teks: "mulai contoh 2"
print("mulai contoh 2")

# begin: memberi nilai pada http header, dalam hal ini user agent nya
headers = {}
# nilai user agent browser saya. bisa dicari di google
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36"
# end: memberi nilai pada http header, dalam hal ini user agent nya

# membuka halaman homepage dari https://quotes.toscrape.com
# kali ini disertai header
req = urllib.request.Request('https://quotes.toscrape.com', headers = headers)
html = urllib.request.urlopen(req).read()
# memprint outputnya.
print(html)
```

Sekarang, aktifkan virtual environment, kemudian jalankan:

```
python main.py
```

Nanti, outputnya akan berupa HTML dari situs quotes tadi ( https://quotes.toscrape.com ).

## Pembahasan

urllib adalah modul bawaan Python 3, sehingga tidak diperlukan pip install untuk menggunakannya.

Di bagian ini:

```
# begin: import modules
import urllib.request
# end: import modules
```

Kita meng-import modul urllib.request.

Kenapa?

Karena kita akan mengirimkan request ke target URL kita.

Jika istilah-istilah tadi masih asing, saya sarankan Anda belajar dulu tentang konsep HTTP di sumber lainnya.

Pada bagian ini:

```
# membuka halaman homepage dari https://quotes.toscrape.com
html = urllib.request.urlopen('https://quotes.toscrape.com').read()
# memprint outputnya.
print(html)
```

Kita membuka halaman denganURL berupa https://quotes.toscrape.com .

Selanjutnya, responnya akan di-assign ke variabel html.

Selanjutnya, isi variabel html akan ditampilkan pada command line.

Adapun, pada bagian ini:

```
# begin: memberi nilai pada http header, dalam hal ini user agent nya
headers = {}
# nilai user agent browser saya. bisa dicari di google
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36"
# end: memberi nilai pada http header, dalam hal ini user agent nya

# membuka halaman homepage dari https://quotes.toscrape.com
# kali ini disertai header
req = urllib.request.Request('https://quotes.toscrape.com', headers = headers)
html = urllib.request.urlopen(req).read()
# memprint outputnya.
print(html)
```

Kita melakukan hal yang tidak berbeda jauh dengan yang sebelumnya.

Namun, ini adalah versi yang lebih kompleks.

Pada kode tadi, kita membuat variabel headers yang diisi User-Agent:

```
# begin: memberi nilai pada http header, dalam hal ini user agent nya
headers = {}
# nilai user agent browser saya. bisa dicari di google
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36"
# end: memberi nilai pada http header, dalam hal ini user agent nya
```

Karena disertai headers, maka pemanggilan method urlopen menjadi lebih kompleks dikarenakan juga oleh input parameter yang lebih banyak:

```
# membuka halaman homepage dari https://quotes.toscrape.com
# kali ini disertai header
req = urllib.request.Request('https://quotes.toscrape.com', headers = headers)
html = urllib.request.urlopen(req).read()
# memprint outputnya.
print(html)
```

Walaupun secara prinsip sama dengan yang sebelum ini.

Lihat kode ini:

```
req = urllib.request.Request('https://quotes.toscrape.com', headers = headers)
```

Variabel req-nya dimasukkan ke parameter dari method urlopen:

```
html = urllib.request.urlopen(req).read()
```

Kemudian hasil method read akan dimasukkan ke variabel html.

Kemudian variabel html di-print:

```
# memprint outputnya.
print(html)
```

Kira-kira seperti itu.

## Penutup

Sekarang Anda telah dijelaskan tentang modul urllib.

Masih banyak method dari urllib yang tidak dibahas di sini.

Anda bisa mengecek dokumentasinya dan melakukan eksperimen sendiri.
