# Belajar Python 3 Mengenal Package pipreqs

Di Python 3, pipreqs adalah package yang berguna untuk membuat requirements.txt dalam scope project.

Artinya, berbeda dengan pip freeze yang juga memasukkan daftar modul Python yang tidak digunakan dalam project secara langsung.

Untuk menginstall pipreqs:

```
pip install pipreqs
```

Untuk membuat requirements.txt, masuk ke dalam folder project kemudian (perhatikan ada tanda titik di sebelah pipreqs. Itu maksudnya adalah folder Anda saat ini):

```
pipreqs .
```

Nanti requirements akan dimasukkan ke requirements.txt.

Selanjutnya, saat project akan dikerjakan di komputer lain, Anda tinggal masuk ke dalam folder di mana ada requirements.txt dan jalankan perintah:

```
pip install -r requirements.txt
```
