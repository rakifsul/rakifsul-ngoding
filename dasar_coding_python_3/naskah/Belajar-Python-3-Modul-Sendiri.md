# Belajar Python 3 Modul Sendiri

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_python_3/tree/main/contoh_python3_modul_sendiri

## Pendahuluan

Modul sendiri di sini artinya adalah modul yang ditulis oleh programmer yang menggunakannya.

Modul sendiri bermanfaat untuk memecah kode Python yang banyak menjadi bagian-bagian kecil.

Itu sangat membantu jika kita sedang mengembangkan aplikasi yang besar.

## Tujuan

Tujuan dari tutorial ini adalah:

-   Pembaca mengenal dan membuat modul sendiri.

## Prasyarat

Prasyarat dari tutorial ini adalah:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Telah meng-install Python versi 3.10.0 dan dapat menjalankannya dari folder manapun.
-   Telah memahami dan bisa mempraktekkan pembuatan project Python 3.

## Langkah-Langkah

Langkah pertama untuk membuat project ini adalah dengan membuat project baru bernama "contoh_python3_modul_sendiri".

Caranya sudah dijelaskan di "[Belajar Python 3 Cara Membuat Project](https://github.com/rakifsul/belajar_coding_python_3/blob/main/Belajar-Python-3-Cara-Membuat-Project.md)".

Sekarang, seharusnya di folder project sudah ada file main.py.

Rename file tersebut menjadi "contoh_modul_sendiri.py"

Replace isinya sedemikan rupa sehingga menjadi seperti ini:

```
# file: contoh_modul_sendiri.py

# buat fungsi untuk memprint "modul yang bagus"
def nama_modul_saya():
    print("modul yang bagus")

# jika ini program utama
if __name__ == "__main__":
    # jalankan fungsi nama_modul_saya()
    # coba anda jalankan langsung:
    # python contoh_modul_sendiri.py
    nama_modul_saya()
```

Selanjutnya, buat file baru bernama "pengguna_modul_sendiri.py".

Isi file tersebut dengan kode ini:

```
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
```

Sekarang, jalankan:

```
python pengguna_modul_sendiri.py
```

Output-nya:

```
modul yang bagus
```

Sekarang, jalankan:

```
python contoh_modul_sendiri.py
```

Output-nya:

```
modul yang bagus
```

## Pembahasan

Aplikasi ini dimulai dari pembuatan modul sendiri.

Di modul sendiri tersebut, yang nama file-nya "contoh_modul_sendiri.py", dibuat sebuah fungsi untuk mem-print teks:

```
# buat fungsi untuk memprint "modul yang bagus"
def nama_modul_saya():
    print("modul yang bagus")
```

Sementara itu, fungsi itu dipanggil dari file "pengguna_modul_sendiri.py", tapi import dulu modul tersebut:

```
# import modul sendiri: contoh_modul_sendiri
# kemudian ambil fungsi nama_modul_saya
from contoh_modul_sendiri import nama_modul_saya
```

Setelah diimport, lalu dipanggil:

```
nama_modul_saya()
```

Tentu output "modul yang bagus" keluar di console.

Akan tetapi, jika kita perhatikan di bagian bawah file "contoh_modul_sendiri.py", ada pemanggilan fungsi itu juga:

```
# jika ini program utama
if __name__ == "__main__":
    # jalankan fungsi nama_modul_saya()
    # coba anda jalankan langsung:
    # python contoh_modul_sendiri.py
    nama_modul_saya()
```

Lalu, kenapa outputnya cuma satu?

Ternyata jawabannya ada di if \_\_name\_\_ == "\_\_main\_\_".

\_\_name\_\_ akan menjadi "\_\_main\_\_" jika kita menjalankan kode dari file "contoh_modul_sendiri.py" secara langsung. Seperti ini:

```
python contoh_modul_sendiri.py
```

Namun jika tidak begitu maka \_\_name\_\_ pastinya bukan "\_\_main\_\_".

Akibatnya nama_modul_saya() di bagian bawah "contoh_modul_sendiri.py" tidak dijalankan.

## Penutup

Sekarang seharusnya Anda paham dengan apa yang saya jelaskan tadi.

Sekarang, cobalah membuah beberapa fungsi tambahan pada modul sendiri Anda dan coba panggil dari "pengguna_modul_sendiri.py".
