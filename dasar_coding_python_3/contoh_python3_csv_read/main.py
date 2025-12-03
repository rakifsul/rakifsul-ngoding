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