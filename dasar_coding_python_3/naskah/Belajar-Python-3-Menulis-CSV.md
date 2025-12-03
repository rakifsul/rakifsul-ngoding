# Belajar Python 3 Menulis CSV

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_python_3/tree/main/contoh_python3_csv_write

## Pendahuluan

CSV adalah comma separated values yang formatnya berbentuk tabel.

Untuk mengolahnya di Python 3, digunakan modul csv.

Kali ini kita akan menggunakan modul csv untuk menulis csv.

Modul csv yang akan kita gunakan nanti adalah csv.writer dan csv.DictWriter.

Seperti halnya yang read, csv.writer menggunakan array dan csv.DictWriter menggunakan dictionary.

## Lebih Lanjut tentang Menulis CSV

Modul csv di Python menyediakan fungsi-fungsi untuk membaca dan menulis file CSV (Comma Separated Values), yang merupakan format umum untuk menyimpan data dalam bentuk tabel.

Dua kelas yang umum digunakan untuk menulis file CSV adalah csv.writer dan csv.DictWriter.

-   csv.writer: Kelas ini digunakan untuk menulis baris-baris data ke file CSV. Ini memungkinkan Anda menulis baris-baris yang diwakili sebagai daftar (list) ke file CSV. Metode writerow() digunakan untuk menulis baris baru ke file CSV.

-   csv.DictWriter: Kelas ini digunakan untuk menulis baris-baris data ke file CSV menggunakan kamus (dictionary) sebagai input. Setiap baris data direpresentasikan sebagai kamus, di mana kunci (keys) kamus sesuai dengan nama kolom dalam file CSV. Metode writeheader() digunakan untuk menulis baris header, dan writerow() digunakan untuk menulis baris data.

## Tujuan

Tujuan dari tutorial ini adalah:

-   Pembaca mengenal modul csv.writer dan csv.DictWriter di Python 3.
-   Pembaca dapat menggunakan modul csv untuk menulis isi file csv.

## Prasyarat

Prasyarat dari tutorial ini adalah:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Telah meng-install Python versi 3.10.0 dan dapat menjalankannya dari folder manapun.
-   Telah memahami dan bisa mempraktekkan pembuatan project Python 3.

## Langkah-Langkah

Langkah pertama untuk membuat project ini adalah dengan membuat project baru bernama "contoh_python3_csv_write".

Anda bisa menggunakan project yang dibuat di "[Belajar Python 3 Cara Membuat Project](https://github.com/rakifsul/belajar_coding_python_3/blob/main/Belajar-Python-3-Cara-Membuat-Project.md)".

Sekarang, seharusnya di folder project sudah ada file main.py.

Replace isinya sedemikan rupa sehingga menjadi seperti ini:

```
# file: main.py

import csv

# cara pertama
# buka contoh-write-0.csv untuk ditulis
with open('contoh-write-0.csv', mode='w') as csvf:
    # gunakan csv.writer
    # quotechar di-set untuk double quote : '"'
    # csv.QUOTE_MINIMAL: hanya quote yang memiliki special character seperti delimiter (misal: koma), quotechar.
    csvw = csv.writer(csvf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # tulis row
    csvw.writerow(['id', 'active', 'ip_address'])
    csvw.writerow(['1', 'True', '127.0.0.1'])

#cara kedua
with open('contoh-write-1.csv', mode='w') as csvf:
    # kali ini nama kolom dibuat terlebih dahulu
    namaKolom = ['id', 'active', 'ip_address']

    # gunakan dictionary writer (map writer)
    # nama kolom digunakan di sini
    csvw = csv.DictWriter(csvf, fieldnames=namaKolom)
    # nama kolom ditulis di sini
    csvw.writeheader()
    # tulis row
    csvw.writerow({'id': '1', 'active' : 'False', 'ip_address' : '192.168.0.1'})
```

Selanjutnya, jalankan:

```
python main.py
```

Nanti akan ada 2 file csv muncul di folder project.

-   File "contoh-write-0.csv" menggunakan csv.writer.
-   File "contoh-write-1.csv" menggunakan csv.DictWriter.

## Pembahasan

Kita memulai aplikasi ini dengan mengimpor modul csv:

```
import csv
```

Selanjutnya, kita menulis file .csv dengan csv.writer:

```
# cara pertama
# buka contoh-write-0.csv untuk ditulis
with open('contoh-write-0.csv', mode='w') as csvf:
    # gunakan csv.writer
    # quotechar di-set untuk double quote : '"'
    # csv.QUOTE_MINIMAL: hanya quote yang memiliki special character seperti delimiter (misal: koma), quotechar.
    csvw = csv.writer(csvf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # tulis row
    csvw.writerow(['id', 'active', 'ip_address'])
    csvw.writerow(['1', 'True', '127.0.0.1'])
```

Yang hasilnya adalah "contoh-write-0.csv".

Sekarang, giliran csv.DictWriter:

```
#cara kedua
with open('contoh-write-1.csv', mode='w') as csvf:
    # kali ini nama kolom dibuat terlebih dahulu
    namaKolom = ['id', 'active', 'ip_address']

    # gunakan dictionary writer (map writer)
    # nama kolom digunakan di sini
    csvw = csv.DictWriter(csvf, fieldnames=namaKolom)
    # nama kolom ditulis di sini
    csvw.writeheader()
    # tulis row
    csvw.writerow({'id': '1', 'active' : 'False', 'ip_address' : '192.168.0.1'})
```

Perhatikan kedua blok kode sebelumnya.

Di csv.writer, inputnya adalah array dan tidak ada writeHeader sehingga untuk menulis headernya digunakan writeRow.

Di csv.DictWriter, inputnya adalah dictionary dan ada writeHeader.

## Penutup

Sekarang, seharusnya Anda sudah memahami modul csv.writer dan csv.DictWriter di Python 3.

Selanjutnya, silakan coba sendiri.
