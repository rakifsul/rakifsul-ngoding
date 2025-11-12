# Belajar Node JS Membaca Dan Menulis File

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_membaca_dan_menulis_file

## Pendahuluan

Kali ini, kita akan belajar membaca dan menulis file di Node.js.

Pada dasarnya, untuk melakukan itu ada beberapa metode:

-   Dengan cara asynchronous dan dengan callback.
-   Dengan cara asynchronous dan async await.
-   Dengan cara menggunakan versi synchronous dari API-nya.

Di bawah ini ada 4 script:

-   readfile.js dan readfilesync.js menunjukkan cara untuk membaca file.
-   writefile.js dan writefilesync.js menunjukkan cara untuk menulis file.

Yang memiliki akhiran “sync” menggunakan metode synchronous, sedangkan yang tidak menggunakan metode asynchronous.

## Lebih Lanjut tentang File Reading dan File Writing

File reading dan file writing adalah dua konsep penting dalam pengelolaan berkas (file) di Node.js:

### File Reading (Membaca Berkas):

Tujuan Utama:

-   File reading atau pembacaan berkas adalah proses membaca data dari berkas yang ada di sistem file.

Proses:

-   Node.js menyediakan metode dan fungsi untuk membaca berkas secara asinkron atau sinkron.
-   Dalam operasi asinkron, Node.js akan membaca berkas secara non-blokir, yang berarti kode akan terus berjalan tanpa menunggu pembacaan berkas selesai. Callback akan dipanggil ketika pembacaan selesai.
-   Dalam operasi sinkron, Node.js akan membaca berkas secara blokir, yang berarti kode akan menunggu pembacaan berkas selesai sebelum melanjutkan eksekusi kode berikutnya.

Penggunaan:

-   File reading digunakan ketika aplikasi perlu membaca konfigurasi, data, atau teks dari berkas untuk diproses lebih lanjut, seperti dalam aplikasi web untuk membaca template HTML atau dalam aplikasi server untuk membaca file konfigurasi.

### File Writing (Menulis Berkas):

Tujuan Utama:

-   File writing atau penulisan berkas adalah proses menulis data ke dalam berkas yang ada di sistem file.

Proses:

-   Node.js menyediakan metode dan fungsi untuk menulis data ke berkas secara asinkron atau sinkron.
-   Seperti file reading, dalam operasi asinkron, Node.js akan menulis berkas secara non-blokir, sementara dalam operasi sinkron, Node.js akan menulis berkas secara blokir.

Penggunaan:

-   File writing digunakan ketika aplikasi perlu menyimpan data hasil proses atau hasil operasi ke dalam berkas, seperti log aplikasi, file konfigurasi yang diperbarui, atau menyimpan data yang diperlukan untuk aplikasi berikutnya.

### Pentingnya Asinkronisitas:

-   Dalam penggunaan file reading dan file writing, operasi asinkron lebih umum digunakan karena memungkinkan aplikasi untuk tetap responsif dan efisien. Dengan demikian, aplikasi dapat melanjutkan eksekusi operasi lain tanpa menunggu pembacaan atau penulisan berkas selesai. File reading dan file writing merupakan bagian integral dari pengelolaan berkas di Node.js dan memungkinkan pengembang untuk mengakses, membaca, dan menulis data dari dan ke dalam berkas dengan mudah dan efisien dalam aplikasi mereka.

## Langkah-Langkah

Buat folder bernama "contoh_nodejs_membaca_dan_menulis_file", kemudian masuk ke dalamnya.

Selanjutnya buat file "readfile.js" dan isi dengan kode ini:

```
// file: readfile.js

// begin: import modules
const fs = require('fs');
const util = require('util');
// end: import modules

// baca file "hello.txt" secara asynchronous
function readHello() {
    fs.readFile('./hello.txt', 'utf8', function (err, data) {
        // tampilkan isinya
        console.log(data);
    });
}

// baca file "hello.txt" secara asynchronous dengan async await
async function readHelloAsyncAwait() {
    // ubah dulu jadi promise
    const readFileAsyncAwait = util.promisify(fs.readFile);

    // sekarang baru bisa menggunakan async await
    const hello = await readFileAsyncAwait('./hello.txt', 'utf8');

    // tampilkan isinya
    console.log(hello);
}

// jalankan
readHello();
readHelloAsyncAwait();
```

Selanjutnya buat file "readfilesync.js" dan isi dengan kode ini:

```
// file: readfilesync.js

// import module fs
const fs = require('fs');

// baca file "hello.txt"
function readHello() {
    // baca secara synchronous. sudah tersedia fungsinya secara default
    const hello = fs.readFileSync('./hello.txt', 'utf8');

    // tampilkan isinya
    console.log(hello);
}

readHello();
```

Selanjutnya buat file "writefile.js" dan isi dengan kode ini:

```
// file: writefile.js

// begin: import modules
const fs = require('fs');
const util = require('util');
// end: import modules

// tulis file secara asyncrhonous
function writeHello() {
    fs.writeFile('./hello-write-file.txt', "hello world writeFile", function () {
        console.log('file sudah ditulis.');
    })
}

// tulis file secara asyncrhonous dengan async await
async function writeHelloAsyncAwait() {
    // ubah dulu jadi promise
    const writeFileAsyncAwait = util.promisify(fs.writeFile);

    // sekarang bisa menggunakan async await
    await writeFileAsyncAwait('./hello-write-file-async-await.txt', "hello world writeFileAsyncAwait");
    console.log('file sudah ditulis.');
}

// jalankan
// writeHello();

writeHelloAsyncAwait();
```

Selanjutnya buat file "writefilesync.js" dan isi dengan kode ini:

```
// file: writefilesync.js

// import module fs
const fs = require('fs');

// tulis file secara synchronous. fungsinya sudah tersedia secara default
function writeHello() {
    fs.writeFileSync('./hello-write-file-sync.txt', "hello world writeFileSync");
}

// jalankan
writeHello();
```

Selanjutnya, buat file bernama "hello.txt" dan isi dengan:

```
hello world
```

Untuk menjalankan kode-kode tadi, buka folder projectnya via terminal, kemudian jalankan perintah:

```
node <nama_script>
```

## Pembahasan

### Pembahasan "readfile.js"

Kode ini adalah sebuah program JavaScript yang bertujuan untuk membaca isi dari file "hello.txt" secara asynchronous menggunakan Node.js.

Berikut adalah penjelasan baris per baris:

```
const fs = require('fs');
const util = require('util');
COPY
Baris ini mengimpor dua modul dari Node.js, yaitu fs (File System) untuk melakukan operasi file dan util untuk menggunakan utilitas bawaan Node.js.

 function readHello() {
       fs.readFile('./hello.txt', 'utf8', function (err, data) {
           // tampilkan isinya
           console.log(data);
       });
   }
```

Fungsi readHello() digunakan untuk membaca file "hello.txt" secara asynchronous menggunakan fs.readFile().

Callback function yang diberikan akan dipanggil setelah file selesai dibaca.

Jika terjadi kesalahan, err akan berisi informasi tentang kesalahan, jika tidak, data akan berisi isi dari file yang dibaca.

```
async function readHelloAsyncAwait() {
       // ubah dulu jadi promise
       const readFileAsyncAwait = util.promisify(fs.readFile);

       // sekarang baru bisa menggunakan async await
       const hello = await readFileAsyncAwait('./hello.txt', 'utf8');

       // tampilkan isinya
       console.log(hello);
   }
```

Fungsi readHelloAsyncAwait() juga membaca file "hello.txt" secara asynchronous, tetapi menggunakan util.promisify() untuk mengubah fungsi fs.readFile() menjadi promise-based sehingga dapat digunakan dengan async/await.

Ini membuat kodenya terlihat lebih bersih dan mudah dipahami.

```
readHello();
readHelloAsyncAwait();
```

Terakhir, kedua fungsi tersebut dipanggil untuk dieksekusi. readHello() akan menampilkan isi file "hello.txt" menggunakan callback, sementara readHelloAsyncAwait() akan melakukannya menggunakan async/await.

Karena operasi baca file dilakukan secara asynchronous, pemanggilan kedua fungsi tidak akan saling menunggu satu sama lain, sehingga keduanya akan dieksekusi secara bersamaan.

### Pembahasan "readfilesync.js"

Kode ini merupakan program JavaScript yang bertujuan untuk membaca isi dari file "hello.txt", namun kali ini menggunakan metode synchronous (blocking) daripada asynchronous.

Berikut penjelasan baris per baris:

```
const fs = require('fs');
```

Baris ini mengimpor modul fs (File System) dari Node.js, yang digunakan untuk melakukan operasi file.

```
function readHello() {
    const hello = fs.readFileSync('./hello.txt', 'utf8');
    console.log(hello);
}
```

Fungsi readHello() membaca file "hello.txt" secara synchronous menggunakan fs.readFileSync().

Ini berarti eksekusi program akan terhenti sementara file dibaca, dan program tidak akan melanjutkan eksekusi selama proses baca file belum selesai.

Setelah file dibaca, isi file akan disimpan dalam variabel hello, dan kemudian ditampilkan di konsol menggunakan console.log().

```
readHello();
```

Terakhir, fungsi readHello() dipanggil untuk dieksekusi.

Karena metode fs.readFileSync() bersifat synchronous, pemanggilan fungsi ini akan menghentikan eksekusi program sampai proses pembacaan file selesai.

Ketika menggunakan readFileSync, proses eksekusi program akan dihentikan sementara sampai operasi file selesai.

Ini berarti bahwa jika ada operasi lain yang perlu dilakukan, seperti menanggapi permintaan HTTP atau input pengguna, maka proses tersebut akan ditunda sampai pembacaan file selesai.

Hal ini dapat menghambat kinerja dalam aplikasi yang membutuhkan respon cepat terhadap berbagai input.

Sebaliknya, metode asynchronous, seperti yang digunakan dalam kode sebelumnya, memungkinkan program untuk melanjutkan eksekusi tanpa harus menunggu selesainya operasi file.

### Pembahasan "writefile.js"

Kode ini bertujuan untuk menulis ke file menggunakan Node.js, baik secara synchronous maupun asynchronous dengan menggunakan async/await.

Berikut penjelasan baris per baris:

```
const fs = require('fs');
const util = require('util');
```

Baris ini mengimpor modul fs (File System) dan util dari Node.js.

fs digunakan untuk operasi file, sedangkan util akan digunakan untuk mengubah fungsi fs.writeFile() menjadi promise-based agar bisa digunakan dengan async/await.

```
function writeHello() {
    fs.writeFile('./hello-write-file.txt', "hello world writeFile", function () {
        console.log('file sudah ditulis.');
    })
}
```

Fungsi writeHello() menulis ke file "hello-write-file.txt" secara asynchronous menggunakan fs.writeFile().

Setelah file selesai ditulis, callback function akan dipanggil dan pesan "file sudah ditulis." akan ditampilkan di konsol.

```
async function writeHelloAsyncAwait() {
    const writeFileAsyncAwait = util.promisify(fs.writeFile);

    await writeFileAsyncAwait('./hello-write-file-async-await.txt', "hello world writeFileAsyncAwait");
    console.log('file sudah ditulis.');
}
```

Fungsi writeHelloAsyncAwait() melakukan hal yang sama seperti writeHello(), tetapi menggunakan async/await.

Pertama, fungsi util.promisify() digunakan untuk mengubah fungsi fs.writeFile() menjadi promise-based.

Kemudian, await digunakan untuk menulis ke file "hello-write-file-async-await.txt". Setelah selesai, pesan "file sudah ditulis." akan ditampilkan di konsol.

```
writeHelloAsyncAwait();
```

Terakhir, fungsi writeHelloAsyncAwait() dipanggil untuk menulis ke file secara asynchronous.

Kode ini menunjukkan cara menulis ke file baik secara synchronous maupun asynchronous dengan menggunakan Node.js.

Metode asynchronous lebih disukai karena tidak menghentikan eksekusi program saat menulis file, sehingga tidak menghalangi proses lain yang sedang berjalan.

### Pembahasan "writefilesync.js"

Kode ini adalah sebuah program sederhana yang bertujuan untuk menulis ke file secara synchronous (blok) menggunakan Node.js.

Berikut adalah penjelasan baris per baris:

```
const fs = require('fs');
```

Baris ini mengimpor modul fs (File System) dari Node.js, yang digunakan untuk melakukan operasi file.

```
function writeHello() {
    fs.writeFileSync('./hello-write-file-sync.txt', "hello world writeFileSync");
}
```

Fungsi writeHello() menulis teks "hello world writeFileSync" ke dalam file bernama "hello-write-file-sync.txt" secara synchronous menggunakan fs.writeFileSync().

Ini berarti eksekusi program akan terhenti sementara sampai proses penulisan file selesai.

```
writeHello();
```

Pemanggilan fungsi writeHello() dijalankan secara langsung.

Ini akan menyebabkan proses penulisan ke file berlangsung pada saat program dijalankan.

Kode ini berguna untuk membuat atau memperbarui file dengan konten yang diberikan secara langsung dan dalam mode blocking.

Namun, karena metode fs.writeFileSync() bersifat synchronous, hal ini dapat menyebabkan program berhenti menanggapi input atau permintaan lainnya sampai proses penulisan selesai.

Oleh karena itu, penggunaan metode asynchronous lebih disarankan dalam kebanyakan kasus agar program dapat terus berjalan dan merespons input atau permintaan yang datang.

## Penutup

Sekian dan terima kasih.
