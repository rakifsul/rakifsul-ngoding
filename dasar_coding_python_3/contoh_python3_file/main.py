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