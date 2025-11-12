# Belajar Node JS Hello World Tanpa Framework

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_hello_world_tanpa_framework

## Pendahuluan

Pada umumnya, saat kita akan membuat aplikasi web dengan Node.js, maka setidaknya kita akan menyiapkan package-package 3rd party dari NPM.

Misalnya saja, Express.

Namun, dengan menggunakan Express, sebenarnya kita telah banyak menyembunyikan cara kerja Node.js di belakang layar.

Walaupun sebenarnya aplikasi hello world bisa dibuat dengan menggunakan Express, ada baiknya juga jika kita tahu caranya tanpa menggunakan framework apapun.

Pada aplikasi ini, kita akan belajar cara meng-import modul, membuat server http, merespons http request dan mengakhirinya, serta membuat server tadi untuk berjalan di port tertentu.

## Manfaat Membuat Hello World tanpa Framework di Node.js

Membuat program "Hello, World!" tanpa menggunakan framework di Node.js memiliki beberapa manfaat:

-   Pemahaman Dasar Node.js: Membuat program sederhana tanpa menggunakan framework memungkinkan untuk memahami dasar-dasar Node.js dengan lebih baik. Ini termasuk memahami bagaimana membuat, menjalankan, dan mengelola proses Node.js secara langsung tanpa adanya lapisan abstraksi yang ditambahkan oleh framework.
-   Kontrol Penuh: Tanpa menggunakan framework, pengembang memiliki kontrol penuh atas kode yang ditulis. Ini memungkinkan untuk menyesuaikan kode sesuai dengan kebutuhan proyek secara spesifik, tanpa terikat oleh keputusan desain atau struktur yang diberlakukan oleh framework tertentu.
-   Keterampilan Pemrograman Umum: Membuat program sederhana tanpa menggunakan framework memungkinkan untuk fokus pada keterampilan pemrograman umum, seperti manipulasi string, manipulasi array, logika pengaturan aliran, dan lain-lain. Ini merupakan fondasi yang kuat untuk memahami dan mengembangkan keterampilan pemrograman Node.js secara lebih luas.
-   Pengenalan Proses Asinkron: Node.js terkenal karena model pemrograman asinkronnya yang kuat. Dengan membuat program "Hello, World!" tanpa framework, pengembang dapat memahami dasar-dasar pemrograman asinkron di Node.js, termasuk penggunaan callback, promise, atau async/await secara langsung.
-   Ringan dan Efisien: Tanpa menggunakan framework, program "Hello, World!" cenderung lebih ringan dan efisien karena tidak ada lapisan abstraksi tambahan yang perlu dimuat atau dieksekusi. Ini membuat program lebih cepat untuk dijalankan dan membutuhkan sumber daya yang lebih sedikit.

Meskipun membuat program "Hello, World!" tanpa framework mungkin terlihat sederhana, namun itu memberikan kesempatan yang berharga untuk memahami dasar-dasar Node.js secara lebih mendalam dan membangun dasar yang kuat untuk pengembangan aplikasi yang lebih kompleks di masa depan.

## Tujuan

Berikut ini adalah tujuan dari tutorial ini:

-   Pembaca mampu membuat aplikasi hello world tanpa menggunakan framework.
-   Pembaca mengenal modul http milik Node.js.

## Prasyarat

Berikut ini adalah prasyarat dari tutorial ini:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Men-download dan meng-install Node.js dan NPM.
-   Bisa meng-akses Node.js dan NPM dari PowerShell di folder manapun.

## Langkah-Langkah

Pertama, buatlah project Node.js bernama "contoh_nodejs_hello_world_tanpa_framework" dengan cara yang telah dijelaskan di "[Belajar Node JS Cara Membuat Project](https://github.com/rakifsul/belajar_coding_node_js/blob/main/Belajar-Node-JS-Cara-Membuat-Project.md)".

Selanjutnya, ubah file "package.json" menjadi seperti ini:

```
{
  "name": "contoh_nodejs_hello_world_tanpa_framework",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev": "node index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Selanjutnya, isi file "index.js" dengan kode ini:

```
// import module http
const http = require("http");

// buat server. dan apapun request nya...
const server = http.createServer((req, res) => {
    // response dengan teks hello world. kemudian akhiri
    res.write("Hello World!");
    res.end();
});

// jalankan server di port 3000
server.listen(3000, () => {
    console.log("Server berjalan di port 3000.");
});
```

Sekarang, jalankan aplikasi ini:

```
npm run dev
```

Buka web browser Anda di:

http://localhost:3000

Nanti akan muncul output:

```
Hello World!
```

Di browser Anda.

## Pembahasan

Pertama-tama, kita membuat project Node.js dan mengisinya dengan beberapa script.

Pada "index.js", kita mulai dari mengimpor modul http:

```
// import module http
const http = require("http");
```

Pada kode di atas, kita mengimpor modul http dan menyimpannya dalam const http.

Node.js menyediakan function require untuk meng-import modul.

Jika modul yang di-import adalah modul bawaan, maka kita tidak perlu meng-install-nya terlebih dahulu dengan npm.

Selain itu, jika modul yang di-import bukan modul buatan sendiri, kita tidak perlu menggunakan path pada require, cukup nama modulnya saja

Kemudian, kita membuat http server dengan cara ini:

```
// buat server. dan apapun request nya...
const server = http.createServer((req, res) => {
    // response dengan teks hello world. kemudian akhiri
    res.write("Hello World!");
    res.end();
});
```

req merupakan parameter untuk request.

res merupakan parameter untuk response.

Berhubung response-nya adalah sama untuk request apapun, maka, di sini saya tidak melakukan filtering terhadap request yang bisa dilakukan menggunakan parameter req.

Selanjutnya, kita menjalankan server tersebut dengan cara melakukan listen di port 3000:

```
// jalankan server di port 3000
server.listen(3000, () => {
    console.log("Server berjalan di port 3000.");
});
```

Dalam keadaan ini, port 3000 sedang digunakan oleh aplikasi ini.

Jadi, jika Anda menjalankan aplikasi lain yang harus menggunakan port 3000, maka kemungkinan aplikasi lain tersebut akan tidak berjalan.

Hal sebaliknya juga berlaku.

Jika sebelum aplikasi ini dijalankan port 3000 sedang digunakan, maka aplikasi ini juga tidak akan berjalan.

Lalu, kenapa kita mengakses aplikasi ini di:

http://localhost:3000

?

Itu karena, port 3000 adalah port yang kita gunakan untuk server http di aplikasi ini.

Adapun domain dari komputer lokal kita adalah localhost.

Selain itu, kita juga menggunakan protokol http dalam aplikasi ini.

Maka, yang perlu diakses browser untuk melihat output aplikasi ini adalah:

http://localhost:3000

## Penutup

Sekarang, seharusnya Anda telah mengenal modul http dan cara menggunakannya.
