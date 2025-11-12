# Belajar Node JS Menggunakan Express Middleware

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_express_middleware

## Pendahuluan

Dalam menangani request dan response, Express memberi kita kesempatan untuk melakukan sesuatu di antara keduanya.

Caranya adalah dengan menggunakan middleware.

Middleware merupakan perantara antara request yang masuk dan response yang keluar.

Pada prakteknya, middleware bisa digunakan untuk autentikasi, logging, validasi data, dan lain-lain.

Secara umum ada dua jenis middleware di Express.

-   Middleware global
-   Middleware lokal

Middleware global berlaku untuk seluruh request handler, sedangkan middleware lokal hanya berlaku pada request handler yang mendaftarkannya.

Dalam tutorial ini saya akan membahas keduanya.

## Lebih Lanjut tentang Express Middleware

Express.js, sebagai kerangka kerja web yang populer untuk Node.js, memperkenalkan konsep yang kuat yang dikenal sebagai middleware.

Middleware adalah serangkaian fungsi yang berurutan yang memiliki akses ke objek permintaan (request) dan objek tanggapan (response) dalam siklus hidup permintaan HTTP.

Dalam bagian ini, kita akan fokus pada konsep, jenis-jenis middleware, dan bagaimana mereka berinteraksi dengan proses pengelolaan permintaan.

### Pengertian Middleware

Middleware, dalam konteks Express.js, bertindak sebagai perantara antara permintaan yang diterima oleh server dan tanggapan yang dikirimkan oleh server. Middleware dapat digunakan untuk melakukan berbagai tugas, seperti memodifikasi objek permintaan atau objek tanggapan, menjalankan fungsi tertentu sebelum atau setelah pengolahan permintaan, atau bahkan menghentikan proses pengolahan permintaan.

### Urutan Eksekusi Middleware

Eksekusi middleware dalam Express.js mengikuti urutan tertentu.

Ketika server menerima permintaan, middleware dijalankan berdasarkan urutan yang didefinisikan dalam kode.

Setiap middleware dapat memutuskan untuk melanjutkan eksekusi ke middleware berikutnya atau menghentikan proses dan mengirimkan tanggapan.

### Fungsi Utama Middleware

#### Mengubah Objek Permintaan dan Tanggapan

Middleware dapat memodifikasi objek permintaan (request) dan objek tanggapan (response) sebelum atau setelah pengolahan permintaan utama.
Contohnya, middleware dapat menambahkan informasi tambahan ke objek permintaan atau menetapkan header khusus di objek tanggapan.

#### Melakukan Tugas Tertentu

Middleware dapat menjalankan tugas tertentu sebelum atau setelah pengolahan permintaan utama. Ini bisa termasuk verifikasi keamanan, autentikasi pengguna, atau logging.
Contohnya, middleware dapat memeriksa apakah pengguna telah mengautentikasi sebelum membiarkan mereka mengakses rute tertentu.

#### Manipulasi Aliran Kontrol

Middleware dapat memanipulasi aliran kontrol dalam proses pengolahan permintaan. Middleware dapat memutuskan apakah permintaan harus melanjutkan ke middleware berikutnya atau dihentikan.
Contohnya, middleware dapat menentukan apakah pengguna memiliki hak akses untuk mengakses sumber daya tertentu dan memutuskan apakah permintaan harus diizinkan atau ditolak.

#### Penanganan Error

Middleware dapat menangani kesalahan yang terjadi selama proses pengolahan permintaan. Middleware khusus yang disebut middleware penanganan kesalahan dapat menangkap dan mengelola kesalahan yang tidak tertangani.
Contohnya, middleware penanganan kesalahan dapat mengirim tanggapan kesalahan yang sesuai kepada klien.

### Jenis-jenis Middleware dalam Express.js

#### Middleware Tingkat Aplikasi (Application-level Middleware)

Middleware ini beroperasi pada seluruh aplikasi dan didefinisikan menggunakan app.use().
Contoh: Middleware logger yang mencatat setiap permintaan ke konsol.

#### Middleware Tingkat Router (Router-level Middleware)

Middleware ini beroperasi pada tingkat router dan didefinisikan menggunakan router.use().
Contoh: Middleware otentikasi yang memeriksa keaslian pengguna sebelum mengizinkan akses ke rute tertentu.

#### Middleware Tanggapan (Error-handling Middleware)

Middleware ini menangani kesalahan yang mungkin terjadi selama proses pengolahan permintaan.
Didefinisikan dengan fungsi yang menerima parameter kesalahan, permintaan, tanggapan, dan fungsi berikutnya (next).

#### Middleware Built-in (Built-in Middleware)

Express.js menyertakan beberapa middleware bawaan yang dapat digunakan tanpa instalasi tambahan.
Contoh: Middleware express.static untuk menyajikan berkas statis seperti gambar atau file CSS.

#### Middleware Pihak Ketiga (Third-party Middleware)

Middleware yang dibuat oleh pihak ketiga dan dapat diintegrasikan dengan Express.js.
Contoh: body-parser untuk menangani data yang dikirimkan melalui formulir HTML.

### Implementasi Umum Middleware dalam Express.js

#### Logger Middleware

Middleware logger dapat digunakan untuk mencatat informasi seperti metode HTTP, URL yang diminta, dan waktu permintaan.
Berguna untuk pemantauan dan debugging.

#### Middleware Otentikasi

Middleware otentikasi dapat memeriksa apakah pengguna telah diotentikasi sebelum membiarkan mereka mengakses rute tertentu.
Menawarkan perlindungan terhadap akses yang tidak sah.

#### Middleware Pengecekan Izin

Middleware ini dapat memeriksa izin pengguna sebelum mengizinkan mereka mengakses sumber daya tertentu.
Memastikan bahwa pengguna hanya dapat mengakses bagian dari aplikasi yang sesuai dengan izin mereka.

#### Middleware Penanganan Kesalahan

Middleware penanganan kesalahan dapat menangkap dan mengelola kesalahan yang terjadi selama proses pengolahan permintaan.
Memberikan tanggapan kesalahan yang baik kepada klien.

### Langkah-langkah Implementasi Middleware

#### Pengenalan Middleware

Identifikasi tujuan dan fungsionalitas middleware yang akan diimplementasikan.
Tentukan apakah middleware akan beroperasi pada tingkat aplikasi, tingkat router, atau sebagai penangan kesalahan.

#### Pendaftaran Middleware

Jika menggunakan middleware pihak ketiga, instal dan daftarkan middleware tersebut menggunakan npm atau cara instalasi yang sesuai.
Jika membuat middleware sendiri, definisikan fungsi middleware dan siapkan kode untuk pendaftaran middleware.

#### Pengaturan Middleware

Terapkan pengaturan middleware dengan menggunakan app.use() untuk middleware tingkat aplikasi atau router.use() untuk middleware tingkat router.
Tentukan urutan eksekusi jika relevan, karena urutan dapat memengaruhi hasil akhir.

#### Integrasi Middleware dengan Rute

Terapkan middleware pada rute tertentu dengan menggunakan app.use() atau router.use() pada tingkat yang sesuai.
Pastikan middleware diatur setelah endpoint tetapi sebelum penanganan rute utama jika diterapkan pada tingkat rute.

#### Pengujian dan Debugging

Jalankan aplikasi dan uji fungsionalitas middleware.
Gunakan alat debugging seperti logger atau pesan konsol untuk memastikan middleware beroperasi sesuai yang diharapkan.

### Keuntungan Penggunaan Middleware

#### Modularitas

Middleware memungkinkan pengembangan aplikasi yang modular dan dapat dikelola dengan memisahkan tugas dan tanggung jawab.

#### Reusabilitas

Middleware dapat digunakan kembali di seluruh aplikasi untuk melakukan tugas yang serupa, meningkatkan efisiensi pengembangan.

#### Ekstensibilitas

Ekosistem middleware yang luas dan beragam memungkinkan pengembang untuk memilih dan mengintegrasikan fungsionalitas tambahan sesuai kebutuhan.

#### Pemisahan Tanggung Jawab

Middleware memungkinkan pemisahan tanggung jawab dalam pengelolaan permintaan, mempermudah pemeliharaan dan debugging.

#### Penanganan Error yang Lebih Baik

Middleware penanganan kesalahan memastikan bahwa kesalahan yang tidak tertangani diatasi dengan baik dan memberikan tanggapan yang sesuai.
Middleware dalam Express.js adalah komponen kritis dalam pengelolaan permintaan dan tanggapan dalam aplikasi web.

Dengan memberikan cara untuk memodifikasi objek permintaan dan tanggapan, menjalankan tugas tertentu, dan mengelola aliran kontrol, middleware memberikan fleksibilitas dan kekuatan dalam pengembangan aplikasi.

Dengan memahami konsep, jenis-jenis, dan langkah-langkah implementasinya, pengembang dapat mengoptimalkan penggunaan middleware untuk meningkatkan modularitas, reusabilitas, dan ekstensibilitas aplikasi mereka.

Melalui integrasi middleware yang bijak, pengembang dapat membangun aplikasi yang tangguh, aman, dan mudah dikelola.

## Tujuan

Berikut ini adalah tujuan dari tutorial ini:

-   Pembaca mengenal middleware dalam Express.
-   Pembaca mampu menggunakan middleware dengan Express.

## Prasyarat

Berikut ini adalah prasyarat dari tutorial ini:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Men-download dan meng-install Node.js dan NPM.
-   Bisa meng-akses Node.js dan NPM dari PowerShell di folder manapun.

## Langkah-Langkah

Pertama, buatlah project Node.js bernama "contoh_nodejs_express_middleware" dengan cara yang telah dijelaskan di "[Belajar Node JS Cara Membuat Project](https://github.com/rakifsul/belajar_coding_node_js/blob/main/Belajar-Node-JS-Cara-Membuat-Project.md)".

Selanjutnya, ubah file "package.json" menjadi seperti ini:

```
{
    "name": "contoh_nodejs_express_middleware",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
        "dev": "node index.js"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "dependencies": {
        "express": "^4.17.1"
    }
}
```

Selanjutnya, isi file "index.js" dengan kode ini:

```
// import modules
const express = require("express");

// inisialisasi express
const app = express();

// middleware ini berjalan secara global
app.use((req, res, next) => {
    console.log("MIDDLEWARE 1");
    next();
});

// request get untuk "/" atau dengan kata lain halaman index
// tanpa middleware lokal
app.get("/", (req, res) => {
    console.log("INDEX");
    res.send("INDEX");
});

// request get untuk "/about" atau dengan kata lain halaman about
// dengan middleware lokal
// perhatikan bahwa parameter ke-2 diisi function. itu middleware nya
app.get(
    "/about",
    (req, res, next) => {
        console.log("MIDDLEWARE 2");
        next();
    },
    (req, res) => {
        console.log("ABOUT");
        res.send("ABOUT");
    }
);

// jalankan server di port 3000
app.listen(3000, () => {
    console.log("Server berjalan di port 3000");
});
```

Selanjutnya, jalankan:

```
npm install
```

Sekarang, jalankan aplikasi ini:

```
npm run dev
```

Buka web browser Anda di:

http://localhost:3000/

Nanti akan muncul output di command line:

```
MIDDLEWARE 1
INDEX
MIDDLEWARE 1
```

Kenapa ada 2 "MIDDLEWARE 1"? Nanti akan saya bahas di bagian pembahasan.

Jika Anda mengakses:

http://localhost:3000/about

Nanti akan muncul output di command line:

```
MIDDLEWARE 1
MIDDLEWARE 2
ABOUT
```

## Pembahasan

Pertama-tama, kita membuat project Node.js dan mengisinya dengan beberapa script.

Selanjutnya, kita menjalankan perintah npm install tanpa diikuti nama package.

Itu maksudnya adalah untuk meng-install seluruh dependencies yang tertulis di "package.json", dalam hal ini hanya Express.

Pada "index.js", kita mulai dari mengimpor modul express:

```
// import modules
const express = require("express");
```

Pada kode di atas, kita mengimpor modul express dan menyimpannya dalam const express.

Node.js menyediakan function require untuk meng-import modul.

Jika modul yang di-import adalah modul pihak ke-3, maka kita perlu meng-install-nya terlebih dahulu dengan npm. Kita telah melakukannya dengan npm install tadi.

Selain itu, jika modul yang di-import bukan modul buatan sendiri, kita tidak perlu menggunakan path pada require, cukup nama modulnya saja

Pada baris kode selanjutnya, kita menginisialisasi dan membuat objek express:

```
// inisialisasi express
const app = express();
```

Objek tersebut disimpan pada const app.

Selanjutnya, kita mendaftarkan middleware global:

```
// middleware ini berjalan secara global
app.use((req, res, next) => {
    console.log("MIDDLEWARE 1");
    next();
});
```

Dengan adanya middleware global tersebut, setiap kali ada request apapun yang masuk ke server, maka console.log akan memprint "MIDDLEWARE 1".

Selanjutnya, kode ini mendaftarkan halaman INDEX:

```
// request get untuk "/" atau dengan kata lain halaman index
// tanpa middleware lokal
app.get("/", (req, res) => {
    console.log("INDEX");
    res.send("INDEX");
});
```

Dalam contoh sebelumnya, "MIDDLEWARE 1" muncul dua kali saat mengakses INDEX.

Itu karena, jika kita mengakses server via web browser, maka biasanya web browser juga akan me-request favicon, jadi ada 2 request.

Adapun URL dari favicon beda dengan INDEX, sehingga teks "INDEX" hanya muncul satu kali.

Selanjutnya, kita mendaftarkan halaman ABOUT:

```
// request get untuk "/about" atau dengan kata lain halaman about
// dengan middleware lokal
// perhatikan bahwa parameter ke-2 diisi function. itu middleware nya
app.get(
    "/about",
    (req, res, next) => {
        console.log("MIDDLEWARE 2");
        next();
    },
    (req, res) => {
        console.log("ABOUT");
        res.send("ABOUT");
    }
);
```

Tampak bahwa ada "MIDDLEWARE 2" yang terpasang pada request handler.

Dengan demikian, outputnya, jika Anda belum membersihkan cache browser Anda adalah:

```
MIDDLEWARE 1
MIDDLEWARE 2
ABOUT
```

Kenapa "MIDDLEWARE 1" hanya ada satu?

Itu karena, favicon sudah di-request sebelumnya, sehingga browser tidak me-request-nya lagi.

Kecuali mungkin jika Anda telah menghapus cache browser Anda.

Selanjutnya, kita menjalankan server tersebut dengan cara melakukan listen di port 3000:

```
// jalankan server di port 3000
app.listen(3000, () => {
    console.log("Server berjalan di port 3000.");
});
```

Dalam keadaan ini, port 3000 sedang digunakan oleh aplikasi ini.

Jadi, jika Anda menjalankan aplikasi lain yang harus menggunakan port 3000, maka kemungkinan aplikasi lain tersebut akan tidak berjalan.

Hal sebaliknya juga berlaku.

Jika sebelum aplikasi ini dijalankan port 3000 sedang digunakan, maka aplikasi ini juga tidak akan berjalan.

## Penutup

Sekarang, seharusnya Anda telah mengenal dan mampu menggunakan middleware dalam Express.
