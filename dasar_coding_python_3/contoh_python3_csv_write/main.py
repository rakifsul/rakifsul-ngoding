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