# Belajar Node JS Mengenal bcryptjs

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_bcryptjs

## Pendahuluan

Dalam aplikasi web yang dibuat dengan Node.js, sangat wajar jika terdapat fitur login.

Dengan fitur login, maka aplikasi web dapat memfilter siapa yang berhak atas konten apa.

Biasanya fitur login tersebut disandingkan dengan fitur register atau yang semacamnya.

Saat register, biasanya user dihadapkan dengan pengisian password-nya.

Di backend, data password tersebut biasanya di-hash dengan algoritma tertentu.

Nanti, data password yang tersimpan di database adalah versi ter-hash-nya.

Saat login, input password dengan password yang ter-hash tadi akan dibandingkan.

Jika cocok, maka user akan lolos untuk login.

Sederhananya kira-kira begitu.

Untuk melakukan hash itu sendiri saya biasanya menggunakan sebuah package bernama bcryptjs.

Di sini saya akan memperlihatkan sebagian cara penggunaannya.

## Lebih Lanjut tentang bcryptjs dan bcrypt

bcrypt dan bcryptjs adalah kedua library yang digunakan untuk hashing password di berbagai bahasa pemrograman, termasuk JavaScript.

Keduanya berfungsi untuk mengamankan password dengan menghasilkan hash yang sulit untuk dipecahkan kembali menjadi password aslinya.

Namun, ada beberapa perbedaan antara keduanya:

### bcrypt

#### Asal

bcrypt adalah library native yang tersedia di banyak bahasa pemrograman, termasuk Node.js. Ini adalah implementasi dari algoritma bcrypt yang ditulis dalam bahasa C.

#### Instalasi

Untuk menggunakan bcrypt, seringkali diperlukan untuk menginstal modul tambahan yang tergantung pada versi platform yang digunakan. Misalnya, di Node.js, Anda perlu menginstal modul bcrypt dengan npm.

#### Kinerja

Karena bcrypt ditulis dalam bahasa C, ini dapat memiliki kinerja yang lebih baik daripada bcryptjs, terutama dalam kasus volume besar hashing.

### bcryptjs

#### Asal

bcryptjs adalah alternatif pure JavaScript untuk bcrypt. Ini ditulis sepenuhnya dalam JavaScript dan tidak bergantung pada modul tambahan.

#### Instalasi

Karena tidak bergantung pada modul tambahan, bcryptjs dapat diinstal langsung dengan npm tanpa kebutuhan untuk membangun atau menginstal dependensi tambahan.

#### Portabilitas

Karena tidak bergantung pada bahasa C atau modul tambahan, bcryptjs dapat digunakan di berbagai platform tanpa masalah kompatibilitas.

#### Kinerja

bcryptjs mungkin memiliki kinerja yang sedikit lebih lambat daripada bcrypt, terutama dalam kasus hashing besar volume, karena berjalan di atas mesin virtual JavaScript.

#### Dengan kata lain

-   bcrypt adalah library native yang efisien dan sering digunakan dalam lingkungan produksi.
-   bcryptjs adalah alternatif pure JavaScript yang mudah digunakan dan portabel di berbagai platform.
-   Pemilihan antara keduanya sering tergantung pada kebutuhan spesifik aplikasi, preferensi pengembang, dan kebijakan keamanan. Jika kinerja dan efisiensi sangat penting, bcrypt mungkin menjadi pilihan yang lebih baik. Namun, jika portabilitas dan kemudahan penggunaan lebih penting, bcryptjs dapat menjadi pilihan yang baik.

## Tujuan

Berikut ini adalah tujuan dari tutorial ini:

-   Pembaca mampu membuat hash dengan bcryptjs.
-   Pembaca mampu membandingkan password yang diinputkan dengan yang ter-hash.

## Prasyarat

Berikut ini adalah prasyarat dari tutorial ini:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Men-download dan meng-install Node.js dan NPM.
-   Bisa meng-akses Node.js dan NPM dari PowerShell di folder manapun.

## Langkah-Langkah

Pertama, buatlah project Node.js bernama "contoh_nodejs_bcryptjs" dengan cara yang telah dijelaskan di "[Belajar Node JS Cara Membuat Project](https://github.com/rakifsul/belajar_coding_node_js/blob/main/Belajar-Node-JS-Cara-Membuat-Project.md)".

Selanjutnya, ubah file "package.json" menjadi seperti ini:

```
{
  "name": "contoh_nodejs_bcryptjs",
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
    "bcryptjs": "^2.4.3"
  }
}
```

Selanjutnya, isi file "index.js" dengan kode ini:

```
const bcrypt = require("bcryptjs");
const password = "password";

const theHash = bcrypt.hashSync("password");
console.log(theHash);

let isMatch = bcrypt.compareSync(password, theHash);
console.log(isMatch);

isMatch = bcrypt.compareSync(password + "123", theHash);
console.log(isMatch);
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
$2a$10$yS8MyiaY0guoKlQbh16kPO4yRlkCzvi2MzHb66FHOuCkCK4Amc4KW
true
false
```

## Pembahasan

Pertama-tama, kita membuat project Node.js dan mengisinya dengan beberapa script.

Selanjutnya, kita menjalankan perintah npm install tanpa diikuti nama package.

Itu maksudnya adalah untuk meng-install seluruh dependencies yang tertulis di "package.json", dalam hal ini hanya bcryptjs.

Pada "index.js", kita mulai dari mengimpor modul bcryptjs:

```
const bcrypt = require("bcryptjs");
```

Pada kode di atas, kita mengimpor modul bcryptjs dan menyimpannya dalam const bcrypt.

Node.js menyediakan function require untuk meng-import modul.

Jika modul yang di-import adalah modul pihak ke-3, maka kita perlu meng-install-nya terlebih dahulu dengan npm. Kita telah melakukannya dengan npm install tadi.

Selain itu, jika modul yang di-import bukan modul buatan sendiri, kita tidak perlu menggunakan path pada require, cukup nama modulnya saja

Langkah selanjutnya, kita membuat konstanta dari password, yakni "password":

```
const password = "password";
```

Kemudian, kita membuat hash dari konstanta tersebut, lalu tampilkan:

```
const theHash = bcrypt.hashSync("password");
console.log(theHash);
```

Di komputer saya, console.log tadi menghasilkan ini:

```
$2a$10$yS8MyiaY0guoKlQbh16kPO4yRlkCzvi2MzHb66FHOuCkCK4Amc4KW
```

Kemudian, kita membandingkan antara input dengan yang di-hash tadi:

```
let isMatch = bcrypt.compareSync(password, theHash);
console.log(isMatch);
```

Di situ hasilnya true, karena memang cocok.

Jika kita ubah dengan menambahkan "123":

```
isMatch = bcrypt.compareSync(password + "123", theHash);
console.log(isMatch);
```

Maka hasilnya akan false, karena tidak cocok.

## Penutup

Sekarang, seharusnya tujuan tutorial ini telah tercapai.
