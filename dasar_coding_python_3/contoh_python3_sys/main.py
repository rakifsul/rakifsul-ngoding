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