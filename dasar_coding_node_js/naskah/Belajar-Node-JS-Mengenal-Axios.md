# Belajar Node JS Mengenal Axios

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_axios

## Pendahuluan

Pada aplikasi tertentu, ada saat di mana aplikasi tersebut perlu mengakses suatu URL dengan sebuah request.

Misalnya, saat aplikasi tersebut akan mengonsumsi REST API target.

Untuk melakukannya, bisa tanpa library eksternal. Misalnya, dengan modul https bawaan Node.js.

Tapi, menurut saya, karena Axios cukup popular, saya lebih suka untuk menggunakannya.

Jadi, tidak ada salahnya mempelajari library tersebut.

## Lebih Lanjut tentang Axios

Axios adalah sebuah library JavaScript yang populer untuk melakukan HTTP requests dari browser atau Node.js. Ini adalah alat yang kuat dan mudah digunakan untuk berinteraksi dengan API dan mengambil data dari server.

Beberapa fitur dan keunggulan dari Axios termasuk:

-   Sintaks yang Mudah Dipahami: Axios menggunakan promise-based API yang membuatnya mudah untuk membuat HTTP requests dan menangani respons.
-   Dukungan untuk Browser dan Node.js: Axios dapat digunakan baik di browser maupun di server-side JavaScript (Node.js).
-   Intersepsi Request dan Response: Anda dapat dengan mudah mengintersep request dan response untuk melakukan transformasi atau menambahkan header secara dinamis.
-   Dukungan untuk Pembatalan Request: Axios memungkinkan Anda untuk membatalkan request yang sedang berlangsung, yang dapat berguna untuk meningkatkan kinerja dan menghindari request yang tidak perlu.
-   Dukungan untuk XSRF Protection: Axios menyediakan mekanisme bawaan untuk melindungi aplikasi Anda dari serangan XSRF (Cross-Site Request Forgery) dengan menggunakan token XSRF.
-   Dukungan untuk Berbagai Jenis Request: Axios mendukung berbagai jenis HTTP requests seperti GET, POST, PUT, DELETE, dan sebagainya.
-   Dukungan untuk Mengirim Data dalam Bentuk JSON: Axios secara otomatis mengubah data yang dikirim dalam bentuk objek JavaScript menjadi format JSON.

Karena keunggulan-keunggulannya ini, Axios menjadi pilihan yang populer bagi para pengembang untuk melakukan komunikasi dengan server dalam aplikasi web mereka.

Untuk mengetahui lebih lanjut tentang Axios, kunjungi:

https://axios-http.com/docs/intro

## Tujuan

Tujuan dari artikel ini adalah:

-   Pembaca mengenal Axios.
-   Pembaca mampu mencoba menggunakan Axios.

## Prasyarat

Berikut ini adalah prasyarat dari tutorial ini:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Men-download dan meng-install Node.js dan NPM.
-   Bisa mengakses Node.js dan NPM dari PowerShell di folder manapun.

## Langkah-Langkah

Pertama, buatlah project Node.js bernama "contoh_nodejs_axios" dengan cara yang telah dijelaskan di "[Belajar Node JS Cara Membuat Project](https://github.com/rakifsul/belajar_coding_node_js/blob/main/Belajar-Node-JS-Cara-Membuat-Project.md)".

Selanjutnya, ubah file "package.json" menjadi seperti ini:

```
{
  "name": "contoh_nodejs_axios",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "axios": "^1.6.8"
  }
}
```

Selanjutnya, isi file "index.js" dengan kode ini:

```
// import modul
const axios = require("axios");

// buat method async yang otomatis langsung dijalankan
(async () => {
    // gunakan axios dengan method get.
    // di sini bisa pakai await karena sudah dimasukkan kedalam method async.
    const ret = await axios.get("https://quotes.toscrape.com");

    // tampilkan hasilnya.
    console.log(ret);
})();
```

Selanjutnya, jalankan:

```
npm install
```

Sekarang, jalankan aplikasi ini:

```
node index.js
```

Nanti akan muncul output di command line:

```
{
  status: 200,
  statusText: 'OK',
  headers: Object [AxiosHeaders] {
    date: 'Tue, 07 May 2024 16:10:58 GMT',
    'content-type': 'text/html; charset=utf-8',
    'transfer-encoding': 'chunked',
    connection: 'keep-alive',
    'strict-transport-security': 'max-age=0; includeSubDomains; preload'
  },
... dan selanjutnya
```

## Pembahasan

Kode Node.js di bagian "Langkah-Langkah" adalah contoh sederhana penggunaan Axios untuk melakukan HTTP GET request ke URL https://quotes.toscrape.com dan menampilkan responsnya.

Mari kita jelaskan baris per baris:

-   `const axios = require("axios");`: Baris ini mengimpor modul Axios ke dalam kode. Ini memungkinkan kita untuk menggunakan semua fitur dan fungsi yang disediakan oleh Axios.
-   `(async () => { ... })();`: Ini adalah sebuah fungsi anonim yang didefinisikan dan langsung dieksekusi (self-invoking). Fungsi ini menggunakan async/await untuk mengelola asinkronitas. Dengan demikian, kita dapat menggunakan kata kunci await di dalamnya untuk menunggu hasil dari operasi asinkron seperti HTTP request.
-   `const ret = await axios.get("https://quotes.toscrape.com");`: Di dalam fungsi async, ini adalah langkah utama. Kami menggunakan metode `axios.get()` untuk membuat permintaan GET ke URL https://quotes.toscrape.com . Kata kunci await memungkinkan kode untuk menunggu sampai permintaan selesai dan hasilnya dikembalikan sebelum melanjutkan eksekusi.
-   `console.log(ret);`: Setelah permintaan selesai dan hasilnya diterima, responsnya disimpan dalam variabel `ret`. Kemudian, kita mencetak respons tersebut menggunakan `console.log()` untuk melihat apa yang telah diterima dari server.

Jadi, secara keseluruhan, kode ini menggunakan Axios untuk membuat permintaan GET ke https://quotes.toscrape.com secara asinkron dan menampilkan responsnya dalam konsol.

## Penutup

Begitulah contoh sederhana penggunaan Axios dalam project Node.js.

Anda boleh coba method-method lainnya seperti POST, PUT, DELETE, dan lain-lain.
