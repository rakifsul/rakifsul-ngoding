# Belajar Node JS Menggunakan Express Router

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_express_router

## CATATAN

Perhatikan bahwa awalan "/" dalam tutorial ini berarti root folder. Ini akan diikuti dengan nama file, baik untuk di root folder maupun sub folder-nya.

## Pendahuluan

Menangani request dan memberi response dari user merupakan hal yang sangat sering dilakukan dengan Express.

Sebenarnya, tanpa router sekalipun, kita tetap bisa membuat server dan meng-handle request dengan Express.

Namun, ketika aplikasi semakin besar dan semakin banyak request handler-nya, tentunya satu file script akan semakin panjang karena request handler tadi.

Agar routes dalam aplikasi yang menggunakan Express lebih rapi, maka digunakan Router.

Dengan router, request handler bisa dipisahkan ke file-file script terpisah sehingga lebih rapi.

## Lebih Lanjut tentang Express Router

Express.js, sebagai salah satu kerangka kerja web paling populer untuk Node.js, memperkenalkan konsep router untuk membantu dalam pengelolaan dan pengorganisasian rute-rute aplikasi.

Router memungkinkan pengembang untuk mengelompokkan dan menangani rute-rute tertentu secara terorganisir.

Dalam bagian ini, kita akan menjelaskan router dalam Express.js tanpa menggunakan kode, memfokuskan pada pengertian dasar, fungsionalitas, dan manfaat yang ditawarkan oleh router.

### Pengertian Router

Router dalam Express.js adalah modul yang digunakan untuk mengelola rute-rute atau endpoint-endpoint dalam aplikasi web. Rute-rute ini mencakup URL atau URI yang dapat diakses oleh pengguna melalui permintaan HTTP. Dengan menggunakan router, pengembang dapat membagi logika aplikasi menjadi bagian-bagian terpisah, membuat kode lebih terstruktur, dan meningkatkan skalabilitas.

### Fungsionalitas Utama Router

#### Pemisahan Logika Aplikasi

Router memungkinkan pemisahan logika aplikasi berdasarkan rute. Ini mempermudah pengembangan dan pemeliharaan kode dengan mengorganisirnya ke dalam modul-modul terpisah.

#### Manajemen Endpoint

Router mengelola endpoint-endpoint atau rute-rute tertentu dalam aplikasi. Setiap router dapat menangani satu atau lebih rute, dan setiap rute dapat diarahkan ke logika pengendali yang berbeda.

#### Skema Rute yang Jelas

Router membantu dalam menyusun skema rute yang jelas dan terstruktur. Ini membuat mudah untuk memahami dan mengelola semua rute yang tersedia dalam aplikasi.

#### Kemampuan Pengelompokan

Router memungkinkan pengelompokan rute-rute terkait. Ini berguna ketika ada beberapa rute yang memerlukan logika atau penanganan yang serupa.

#### Middleware Khusus Router

Setiap router dapat memiliki middleware khusus yang hanya berlaku untuk rute-rute dalam router tersebut. Hal ini memberikan fleksibilitas tambahan dalam menangani permintaan yang terkait dengan router tertentu.

#### Pemetaan Rute ke Fungsi Pengendali

Router memetakan setiap rute ke fungsi pengendali (handler) yang bertanggung jawab untuk menangani permintaan yang sesuai. Ini memungkinkan logika bisnis terpisah dari definisi rute.

### Manfaat Router dalam Express.js

#### Pemeliharaan Kode yang Lebih Mudah

Dengan menggunakan router, pengembang dapat memisahkan logika aplikasi ke dalam modul-modul terpisah berdasarkan fungsionalitas atau fitur tertentu. Ini membuat pemeliharaan kode lebih mudah karena setiap modul dapat fokus pada satu aspek tertentu dari aplikasi.

#### Organisasi Terstruktur

Router membantu dalam menyusun struktur yang terorganisir untuk rute-rute dalam aplikasi. Struktur yang jelas memudahkan pemahaman dan navigasi melalui kode.

#### Skalabilitas yang Lebih Baik

Saat aplikasi tumbuh, router memungkinkan pengembang untuk menangani kompleksitas dengan cara yang terstruktur. Rute-rute dapat diorganisir ke dalam router-ruter terpisah, memfasilitasi pengelolaan proyek yang besar.

#### Pengelompokan Middleware

Router memungkinkan pengelompokan middleware tertentu untuk digunakan hanya dalam konteks router tersebut. Hal ini memungkinkan penanganan permintaan yang terkait dengan router tertentu memiliki middleware yang khusus dan terpisah dari middleware lainnya.

#### Penggunaan Middleware Global dan Lokal

Router memungkinkan pengembang untuk menggunakan middleware secara global, yang berlaku untuk seluruh aplikasi, dan juga middleware lokal yang hanya berlaku untuk rute-rute tertentu dalam router.

### Struktur Dasar Penggunaan Router

#### Pendefinisian Router

Pertama, router perlu didefinisikan menggunakan metode express.Router(). Ini menciptakan instance router yang dapat digunakan untuk menangani rute-rute tertentu.

#### Definisi Rute pada Router

Rute-rute ditambahkan ke router menggunakan metode seperti router.get(), router.post(), atau metode lainnya sesuai dengan metode HTTP yang diinginkan.

#### Pengelompokan dan Penggunaan Router

Router dapat dikelompokkan untuk menangani rute-rute tertentu. Setiap router kemudian dapat digunakan sebagai middleware dalam aplikasi utama dengan menggunakan app.use().

#### Pemetaan Rute ke Fungsi Pengendali

Setiap rute pada router dapat diarahkan ke fungsi pengendali yang akan menangani permintaan yang sesuai dengan rute tersebut.

#### Penanganan Error pada Router

Router dapat memiliki middleware penanganan kesalahan sendiri untuk menangani kesalahan yang terjadi dalam konteks router tersebut.
Router dalam Express.js adalah alat yang kuat untuk mengelola dan mengorganisir rute-rute dalam aplikasi web.

Dengan memungkinkan pemisahan logika, pengelompokan, dan definisi rute yang terstruktur, router membantu dalam mengelola kompleksitas pengembangan aplikasi.

Keuntungan pemeliharaan kode yang lebih mudah, struktur yang terorganisir, dan kemampuan pengelompokan membuat router menjadi komponen kunci dalam pembangunan aplikasi web yang skalabel dan mudah dikelola.

Dengan pemahaman yang baik tentang penggunaan router, pengembang dapat meningkatkan efisiensi dan keterbacaan kode mereka, mendukung pengelolaan proyek yang besar, dan membangun aplikasi yang tangguh dan mudah dipelihara.

## Tujuan

Berikut ini adalah tujuan dari tutorial ini:

-   Pembaca mengenal router dalam Express.
-   Pembaca mampu menggunakan router dengan Express.

## Prasyarat

Berikut ini adalah prasyarat dari tutorial ini:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Men-download dan meng-install Node.js dan NPM.
-   Bisa meng-akses Node.js dan NPM dari PowerShell di folder manapun.

## Langkah-Langkah

Pertama, buatlah project Node.js bernama "contoh_nodejs_express_router" dengan cara yang telah dijelaskan di "[Belajar Node JS Cara Membuat Project](https://github.com/rakifsul/belajar_coding_node_js/blob/main/Belajar-Node-JS-Cara-Membuat-Project.md)".

Selanjutnya, ubah file "/package.json" menjadi seperti ini:

```
{
    "name": "contoh_nodejs_express_router",
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

Selanjutnya, isi file "/index.js" dengan kode ini:

```
// import module express
const express = require("express");

// inisialisasi express
const app = express();

// begin: import routers
const indexRouter = require("./routes/index.js");
const aboutRouter = require("./routes/about.js");
// end: import routers

// begin: gunakan sebagai routers. parameter pertama adalah path prefix nya
app.use("/", indexRouter);
app.use("/about", aboutRouter);
// end: gunakan sebagai routers. parameter pertama adalah path prefix nya

// jalankan server di port 3000
app.listen(3000, () => {
    console.log("Server berjalan di port 3000");
});
```

Selanjutnya, buat file "/routes/index.js", kemudian isi dengan kode ini:

```
// import express
const express = require("express");

// buat routernya
const router = express.Router();

// handle request "/"
router.get("/", (req, res) => {
    // kirim teks bertuliskan "INDEX"
    res.send("INDEX");
});

// export modul ini
module.exports = router;
```

Selanjutnya, buat file "/routes/about.js", kemudian isi dengan kode ini:

```
// import express
const express = require("express");

// buat routernya
const router = express.Router();

// handle request /about.
// di parameternya tertulis "/" karena saat
// di-use di root index.js sudah ada path "/about"
router.get("/", (req, res) => {
    // kirim teks bertuliskan "ABOUT"
    res.send("ABOUT");
});

// export module ini
module.exports = router;
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

Nanti akan muncul output di browser:

```
INDEX
```

Buka web browser Anda di:

http://localhost:3000/about

Nanti akan muncul output di browser:

```
ABOUT
```

## Pembahasan

Pertama-tama, kita membuat project Node.js dan mengisinya dengan beberapa script.

Selanjutnya, kita menjalankan perintah npm install tanpa diikuti nama package.

Itu maksudnya adalah untuk meng-install seluruh dependencies yang tertulis di "/package.json", dalam hal ini hanya Express.

Pada "/index.js", kita mulai dari mengimpor modul express:

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

Selanjutnya, kita mengimpor routers yang ada di folder "/routes", yakni "/routes/index.js" dan "/routes/about.js":

```
// begin: import routers
const indexRouter = require("./routes/index.js");
const aboutRouter = require("./routes/about.js");
// end: import routers
```

Mengimpor router saja tidak cukup.

Harus di-use juga.

Kode ini mendaftarkan kedua routers tadi:

```
// begin: gunakan sebagai routers. parameter pertama adalah path prefix nya
app.use("/", indexRouter);
app.use("/about", aboutRouter);
// end: gunakan sebagai routers. parameter pertama adalah path prefix nya
```

Perhatikan bahwa parameter pertama adalah path untuk prefix dari masing-masing request di masing-masing router.

Karena router index prefix-nya "/" maka tidak perlu ada tambahan path saat mengaksesnya.

http://localhost:3000/ akan mengakses "/"-nya index.

Adapun router about prefix-nya "/about", maka untuk mengakses "/" di about harus ditambahkan "/about".

http://localhost:3000/about akan mengakses "/"-nya about.

Ini adalah isi dari script "/routes/index.js":

```
// import express
const express = require("express");

// buat routernya
const router = express.Router();

// handle request "/"
router.get("/", (req, res) => {
    // kirim teks bertuliskan "INDEX"
    res.send("INDEX");
});

// export modul ini
module.exports = router;
```

Dan ini adalah isi dari script "/routes/about.js":

```
// import express
const express = require("express");

// buat routernya
const router = express.Router();

// handle request /about.
// di parameternya tertulis "/" karena saat
// di-use di root index.js sudah ada path "/about"
router.get("/", (req, res) => {
    // kirim teks bertuliskan "ABOUT"
    res.send("ABOUT");
});

// export module ini
module.exports = router;
```

Tidak ada hal yang aneh pada kedua script di atas kecuali:

```
// export module ini
module.exports = router;
```

Maksud dari kode tersebut adalah untuk meng-export script sebagai modul, sehingga dapat di-require seperti yang telah kita lakukan di "/index.js".

## Penutup

Sekarang, seharusnya Anda telah mengenal dan mampu menggunakan Express router.
