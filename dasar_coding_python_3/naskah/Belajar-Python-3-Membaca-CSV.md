# Belajar Python 3 Membaca CSV

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_python_3/tree/main/contoh_python3_csv_read

## Pendahuluan

CSV adalah comma separated values yang formatnya berbentuk tabel.

Untuk mengolahnya di Python 3, digunakan modul csv.

Kali ini kita akan menggunakan modul csv untuk membaca csv.

Modul csv yang akan kita gunakan nanti adalah csv.reader dan csv.DictReader.

Perbedaannya, csv.reader menghasilkan array dengan index, sedangkan csv.DictReader menghasilkan dictionary.

## Lebih Lanjut tentang Membaca CSV

Modul csv di Python juga menyediakan fungsi-fungsi untuk membaca file CSV.

Dua kelas yang umum digunakan untuk membaca file CSV adalah csv.reader dan csv.DictReader.

-   csv.reader: Kelas ini digunakan untuk membaca baris-baris dari file CSV sebagai daftar (list) string. Setiap baris diwakili sebagai daftar nilai, di mana setiap nilai merupakan kolom dalam baris tersebut. Dengan menggunakan csv.reader, Anda dapat membaca file CSV secara baris per baris dan mengakses nilai-nilai di setiap kolom.

-   csv.DictReader: Kelas ini digunakan untuk membaca file CSV sebagai daftar (list) kamus (dictionary). Dalam hal ini, setiap baris diwakili sebagai kamus, di mana kunci (keys) kamus sesuai dengan nama kolom dalam file CSV. Penggunaan csv.DictReader memungkinkan Anda untuk mengakses nilai-nilai dalam setiap baris menggunakan nama kolom daripada menggunakan indeks posisi.

Kedua kelas ini memungkinkan Anda membaca data dari file CSV dengan cara yang nyaman dan fleksibel, tergantung pada bagaimana Anda ingin mengolah data tersebut dalam kode Anda.

Jika Anda hanya memerlukan data mentah dalam bentuk daftar string, csv.reader akan menjadi pilihan yang baik.

Namun, jika Anda ingin mengakses data sebagai kamus dengan menggunakan nama kolom, maka csv.DictReader akan lebih berguna karena memungkinkan Anda untuk mengakses nilai-nilai dengan cara yang lebih deskriptif.

## Tujuan

Tujuan dari tutorial ini adalah:

-   Pembaca mengenal modul csv.reader dan csv.DictReader di Python 3.
-   Pembaca dapat menggunakan modul csv untuk membaca isi file csv.

## Prasyarat

Prasyarat dari tutorial ini adalah:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Telah meng-install Python versi 3.10.0 dan dapat menjalankannya dari folder manapun.
-   Telah memahami dan bisa mempraktekkan pembuatan project Python 3.

## Langkah-Langkah

Langkah pertama untuk membuat project ini adalah dengan membuat project baru bernama "contoh_python3_csv_read".

Anda bisa menggunakan project yang dibuat di "[Belajar Python 3 Cara Membuat Project](https://github.com/rakifsul/belajar_coding_python_3/blob/main/Belajar-Python-3-Cara-Membuat-Project.md)".

Sekarang, seharusnya di folder project sudah ada file main.py.

Replace isinya sedemikan rupa sehingga menjadi seperti ini:

```
# file: main.py

# begin: import modules
import csv
# end: import modules

# print judul
print("// dengan csv.reader")

# buka file contoh-read.csv
# dengan menggunakan with, tidak perlu fungsi close
# dengan menggunakan with, tidak perlu menerapkan exception handling
with open('contoh-read.csv') as csvf:
    # gunakan csv.reader untuk memparsing csv
    csvreader = csv.reader(csvf, delimiter=',')

    # counter
    ctr = 0

    # print row nya
    for baris in csvreader:
        print("id: " + baris[0] + ", active: " + baris[1] + ", IP: " + baris[2])
        ctr += 1

    # print total barisnya
    print("Total baris:" + str(ctr))

# beri jarak
print("")

# print judul
print("// dengan csv.DictReader")


# buka file contoh-read.csv
with open('contoh-read.csv') as csvf:
    # gunakan csv.DictReader untuk memparsing csv
    # dengan csv.DictReader, baris akan menjadi Dictionary
    csvreader = csv.DictReader(csvf, delimiter=',')

    # counter
    ctr = 0

    # print row nya
    for baris in csvreader:
        print("id: " + baris["id"] + ", active: " + baris["active"] + ", IP: " + baris["ip_address"])
        ctr += 1

    # print total barisnya
    print("Total baris:" + str(ctr))
```

Sekarang, siapkan sebuah file csv semacam ini:

```
id,active,ip_address
1,True,40.152.231.57
2,False,238.18.84.155
3,False,108.61.114.208
4,True,75.113.225.112
5,True,195.27.100.152
6,True,226.78.235.182
7,True,31.226.24.155
8,False,228.31.146.10
9,False,216.241.46.166
10,False,86.104.26.157
11,True,229.44.43.41
12,True,158.143.226.149
13,False,251.185.209.220
14,False,61.113.243.94
15,True,154.75.222.99
16,False,122.57.14.238
17,False,146.25.76.169
18,True,220.39.57.194
19,True,38.203.246.118
20,True,179.225.21.133
```

Simpan ke dalam file bernama "contoh-read.csv".

Selanjutnya jalankan:

```
python main.py
```

Nanti muncul output semacam ini:

```
// dengan csv.reader
id: id, active: active, IP: ip_address
id: 1, active: True, IP: 40.152.231.57
id: 2, active: False, IP: 238.18.84.155
```

## Pembahasan

Kita memulai aplikasi ini dengan mengimpor modul csv:

```
# begin: import modules
import csv
# end: import modules
```

Selanjutnya, print judul:

```
# print judul
print("// dengan csv.reader")
```

Selanjutnya, buka dan baca csv-nya:

```
# buka file contoh-read.csv
# dengan menggunakan with, tidak perlu fungsi close
# dengan menggunakan with, tidak perlu menerapkan exception handling
with open('contoh-read.csv') as csvf:
    # gunakan csv.reader untuk memparsing csv
    csvreader = csv.reader(csvf, delimiter=',')

    # counter
    ctr = 0

    # print row nya
    for baris in csvreader:
        print("id: " + baris[0] + ", active: " + baris[1] + ", IP: " + baris[2])
        ctr += 1

    # print total barisnya
    print("Total baris:" + str(ctr))
```

Parameter "delimiter" pada csv.reader adalah pemisahnya, dalam hal ini koma (,).

Perhatikan juga bahwa kita membacanya dari array yang menggunakan index dan karena itulah kurung siku diisi angka:

```
# print row nya
    for baris in csvreader:
        print("id: " + baris[0] + ", active: " + baris[1] + ", IP: " + baris[2])
```

Selanjutnya, saya akan membahas csv.DictReader.

Pada kode ini, kita beri newline kosong dan print judul agar perbedaannya lebih jelas di output:

```
# beri jarak
print("")

# print judul
print("// dengan csv.DictReader")
```

Kemudian, buka dan baca csv-nya:

```
# buka file contoh-read.csv
with open('contoh-read.csv') as csvf:
    # gunakan csv.DictReader untuk memparsing csv
    # dengan csv.DictReader, baris akan menjadi Dictionary
    csvreader = csv.DictReader(csvf, delimiter=',')

    # counter
    ctr = 0

    # print row nya
    for baris in csvreader:
        print("id: " + baris["id"] + ", active: " + baris["active"] + ", IP: " + baris["ip_address"])
        ctr += 1

    # print total barisnya
    print("Total baris:" + str(ctr))
```

Perhatikan bahwa kali ini dictionary digunakan dan karena itulah kurung siku diisi string:

```
# print row nya
    for baris in csvreader:
        print("id: " + baris["id"] + ", active: " + baris["active"] + ", IP: " + baris["ip_address"])
```

## Penutup

Sekarang, seharusnya Anda sudah memahami modul csv.reader dan csv.DictReader di Python 3.

Silakan eksplorasi lebih lanjut.
