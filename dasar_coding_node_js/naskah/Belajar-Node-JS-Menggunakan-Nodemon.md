# Belajar Node JS Menggunakan Nodemon

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_nodemon

## Pendahuluan

Dalam membangun aplikasi Node.js, bukan tidak mungkin akan ada perubahan dalam script Node.js yang kita buat.

Akan tetapi, perubahan kode tersebut hanya bisa dilihat jika aplikasi Node.js-nya di-restart.

Mungkin tidak masalah jika aplikasi yang kita buat berjalan selewat saja, seperti misalnya aplikasi command line.

Namun, dalam aplikasi web, biasanya akan ada infinite loop untuk melakukan listen port tertentu.

Artinya, jika aplikasi semacam tadi mengalami perubahan kode, kita harus menghentikan aplikasi tersebut, kemudian menjalankannya lagi.

Jika itu dilakukan manual dan secara sering, tentunya akan merepotkan.

Di sinilah nodemon dapat membantu kita.

nodemon adalah salah satu package NPM yang fungsinya mengawasi script-script dalam project Node.js.

Setelah nodemon dijalankan, maka jika ada script yang diawasinya berubah, kemudian di-save, maka nodemon akan secara otomatis me-restart aplikasi.

## Lebih Lanjut tentang Nodemon

Nodemon adalah alat pengembangan (development tool) yang berguna untuk memonitor perubahan pada berkas dalam proyek Node.js dan secara otomatis memulai ulang server atau aplikasi Node.js ketika ada perubahan.

Berikut adalah beberapa poin penting tentang Nodemon:

-   Memantau Perubahan Berkas: Nodemon secara terus-menerus memantau berkas dalam proyek Node.js, seperti berkas JavaScript atau JSON. Ini dilakukan dengan memeriksa waktu modifikasi (timestamp) pada berkas-berkas tersebut.
-   Pemulihan Otomatis: Ketika Nodemon mendeteksi perubahan pada berkas, seperti penyimpanan baru atau penyuntingan, ia akan secara otomatis memulai ulang server Node.js atau aplikasi yang sedang berjalan. Ini memungkinkan untuk melihat perubahan secara langsung tanpa perlu memulai ulang server secara manual setiap kali ada perubahan pada kode.
-   Mempercepat Proses Pengembangan: Nodemon membantu meningkatkan produktivitas pengembangan dengan mempercepat siklus pengembangan. Pengembang tidak perlu lagi menghentikan dan memulai ulang server secara manual setiap kali ada perubahan pada kode, yang dapat menghemat waktu dan mengurangi gangguan.
-   Konfigurasi Mudah: Nodemon dapat dikonfigurasi dengan mudah menggunakan berkas konfigurasi atau opsi baris perintah. Ini memungkinkan untuk menyesuaikan perilaku Nodemon sesuai dengan kebutuhan proyek, seperti menambahkan pengecualian untuk berkas tertentu atau menyesuaikan interval pemantauan.
-   Dukungan untuk Berbagai Jenis Proyek: Nodemon dapat digunakan dengan berbagai jenis proyek Node.js, termasuk proyek aplikasi web, server API, atau aplikasi terpisah lainnya. Ini membuatnya menjadi alat yang serbaguna untuk pengembangan Node.js.

Secara keseluruhan, Nodemon adalah alat yang berguna dan populer dalam ekosistem pengembangan Node.js karena kemampuannya untuk memantau perubahan kode secara otomatis dan memulai ulang server dengan cepat.

Ini membantu meningkatkan produktivitas pengembangan dan memudahkan proses pengembangan aplikasi Node.js.

## Tujuan

Berikut ini adalah tujuan dari tutorial ini:

-   Pembaca mampu menggunakan nodemon.
-   Pembaca mengenal nodemon.

## Prasyarat

Berikut ini adalah prasyarat dari tutorial ini:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Men-download dan meng-install Node.js dan NPM.
-   Bisa meng-akses Node.js dan NPM dari PowerShell di folder manapun.

## Langkah-Langkah

Pertama, buatlah project Node.js bernama "contoh_nodejs_nodemon" dengan cara yang telah dijelaskan di "[Belajar Node JS Cara Membuat Project](https://github.com/rakifsul/belajar_coding_node_js/blob/main/Belajar-Node-JS-Cara-Membuat-Project.md)".

Selanjutnya, ubah file "package.json" menjadi seperti ini:

```
{
  "name": "contoh_nodejs_nodemon",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev": "nodemon -e js,html -w ./ index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Selanjutnya, isi file "index.js" dengan kode ini:

```
const express = require("express");
const app = express();

app.get("/", (req, res, next) => {
    res.sendFile(__dirname + "/views/" + "index.html");
});

app.listen(3000, () => {
    console.log("Server berjalan di port 3000");
});
```

Selanjutnya buat folder "views" yang di dalamnya ada file "index.html".

Isi file "index.html" adalah seperti ini:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Belajar Nodemon</title>
</head>

<body>
    <h1>Belajar Nodemon</h1>
</body>

</html>
```

Selanjutnya, install express:

```
npm install express
```

Dan install nodemon sebagai dev dependencies:

```
npm install nodemon --save-dev
```

Nanti, di "package.json" akan ada tambahan entry:

```
"dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "nodemon": "^2.0.7"
  }
```

Catat bahwa versinya mungkin berbeda dengan "package.json" milik saya.

Sekarang, jalankan aplikasi ini:

```
npm run dev
```

Selanjutnya, ubah file "index.js", kemudian save, kemudian perhatikan command line, akan terlihat bahwa aplikasi ini di-restart

Itu juga akan terjadi jika kita mengubah dan men-save "index.html".

## Pembahasan

Pertama-tama, kita membuat project Node.js dan mengisinya dengan beberapa script.

Karena kita telah menginstall nodemon, maka perintah node diganti dengan nodemon, sesuai dengan yang ada di "package.json":

```
"dev": "nodemon -e js,html -w ./ index.js"
```

Menurut kode itu, saat perintah npm run dev dijalankan, semua file berekstensi ".js" dan ".html" yang ada di folder project dan subfoldernya akan diawasi.

Jika terjadi perubahan, maka aplikasi akan di-restart.

Dengan kata lain, parameter "-e" menentukan ekstensi apa yang diawasi dan parameter "-w" menentukan folder mana yang diawasi.

## Penutup

Sekarang, seharusnya Anda telah mengenal nodemon dan cara menggunakannya.
