# Belajar Node JS Hello World Dengan Express

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_hello_world_dengan_express

## Pendahuluan

Membuat aplikasi server dengan Node.js tanpa framework itu memungkinkan.

Seperti apa yang dijelaskan pada "[Belajar Node JS Hello World Tanpa Framework](https://github.com/rakifsul/belajar_coding_node_js/blob/main/Belajar-Node-JS-Hello-World-Tanpa-Framework.md)".

Namun, dengan menggunakan Express, sebenarnya kita telah banyak menghemat waktu penulisan kode.

Itu karena dengan menggunakan Express, banyak hal yang kompleks dilakukan di balik layar.

Pada tutorial sebelumnya, aplikasi yang kita buat masih sederhana.

Jadi, mungkin saja kode yang ditulis hanya sedikit.

Lalu, bagaimana jika aplikasi yang kita buat cukup besar?

Tanpa menggunakan framework tentunya akan merepotkan.

Oleh karena itu, mempelajari framework Node.js seperti Express menurut saya cukup bermanfaat.

Pada tutorial ini, saya akan membahas cara membuat aplikasi hello world dengan Node.js dan Express.

## Tujuan

Berikut ini adalah tujuan dari tutorial ini:

-   Pembaca mampu membuat aplikasi hello world menggunakan Express.
-   Pembaca mengenal Express.

## Prasyarat

Berikut ini adalah prasyarat dari tutorial ini:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Men-download dan meng-install Node.js dan NPM.
-   Bisa meng-akses Node.js dan NPM dari PowerShell di folder manapun.

## Langkah-Langkah

Pertama, buatlah project Node.js bernama "contoh_nodejs_hello_world_dengan_express" dengan cara yang telah dijelaskan di "[Belajar Node JS Cara Membuat Project](https://github.com/rakifsul/belajar_coding_node_js/blob/main/Belajar-Node-JS-Cara-Membuat-Project.md)".

Selanjutnya, ubah file "package.json" menjadi seperti ini:

```
{
    "name": "contoh_nodejs_hello_world_dengan_express",
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
// import module express
const express = require("express");

// inisialisasi express
const server = express();

// handle request "/"
server.get("/", (req, res, next) => {
    // response dengan teks "Hello World!", kemudian akhiri
    res.write("Hello World!");
    res.end();
});

// jalankan server di port 3000
server.listen(3000, () => {
    console.log("Server berjalan di port 3000.");
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

Nanti akan muncul output:

```
Hello World!
```

Di browser Anda.

## Pembahasan

Pertama-tama, kita membuat project Node.js dan mengisinya dengan beberapa script.

Selanjutnya, kita menjalankan perintah npm install tanpa diikuti nama package.

Itu maksudnya adalah untuk meng-install seluruh dependencies yang tertulis di "package.json", dalam hal ini hanya Express.

Pada "index.js", kita mulai dari mengimpor modul express:

```
// import module express
const express = require("express");
```

Pada kode di atas, kita mengimpor modul express dan menyimpannya dalam const express.

Node.js menyediakan function require untuk meng-import modul.

Jika modul yang di-import adalah modul pihak ke-3, maka kita perlu meng-install-nya terlebih dahulu dengan npm. Kita telah melakukannya dengan npm install tadi.

Selain itu, jika modul yang di-import bukan modul buatan sendiri, kita tidak perlu menggunakan path pada require, cukup nama modulnya saja

Pada baris kode selanjutnya, kita menginisialisasi dan membuat objek express:

```
// inisialisasi express
const server = express();
```

Objek tersebut disimpan pada const server.

Selanjutnya, server melakukan filter terhadap request GET ke path "/" atau root:

```
// handle request "/"
server.get("/", (req, res, next) => {
    // response dengan teks "Hello World!", kemudian akhiri
    res.write("Hello World!");
    res.end();
});
```

Request tadi direspon dengan teks "Hello World!", kemudian diakhiri dengan res.end().

Yang perlu Anda ingat di kode tadi adalah bahwa kode tadi bersifat pasif.

Dengan kata lain, kita tidak memerintahkan server untuk membuka browser client dan menampilkan teks "Hello World!", melainkan menunggu ada request dari browser client, dan jika request itu datang, maka tangani dengan callback di parameternya, sehingga teks "Hello World!" akan tampil.

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

http://localhost:3000/

?

Itu karena, port 3000 adalah port yang kita gunakan untuk server express di aplikasi ini.

Adapun domain dari komputer lokal kita adalah localhost.

Selain itu, kita juga menggunakan protokol http dalam aplikasi ini.

Adapun penambahan "/" di akhir URL berarti browser melakukan request terhadap path "/" di server express.

Maka, yang perlu diakses browser untuk melihat output aplikasi ini adalah:

http://localhost:3000/

## Penutup

Sekarang, seharusnya Anda telah mengenal Express dan cara menggunakannya.
