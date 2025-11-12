# Belajar Node JS Menampilkan Machine ID

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_menampilkan_machine_id

## Pendahuluan

Kali ini, kita akan belajar cara menampilkan machine ID di Node.js

Ketika kita membuat sebuah aplikasi, terutama aplikasi desktop, mungkin saja kita ingin membatasi penginstallan aplikasi tersebut pada satu komputer saja.

Dengan kata lain kita mungkin menginginkan sebuah sistem lisensi dalam aplikasi kita.

Agar hal tersebut dapat terwujud diperlukan suatu cara untuk mendapatkan identitas unik dari OS di komputer tersebut.

Node Machine ID ( https://www.npmjs.com/package/node-machine-id ) bisa membantu kita untuk mendapatkan unique id dari OS yang menggunakannya.

Pada dasarnya Node Machine ID menggunakan registry untuk mendapatkan unique id di Windows.

Tepatnya di “HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography”.

## Lebih Lanjut tentang node-machine-id

node-machine-id adalah sebuah paket npm yang menyediakan cara untuk mendapatkan ID mesin (machine ID) dari sistem tempat aplikasi Node.js berjalan.

ID mesin ini biasanya berupa nilai unik yang berhubungan dengan perangkat keras atau konfigurasi sistem, dan sering digunakan untuk tujuan lisensi, identifikasi, atau keamanan dalam aplikasi.

Beberapa poin penting tentang node-machine-id:

-   Mendapatkan ID Mesin Secara Konsisten: Paket ini memungkinkan aplikasi Node.js untuk mendapatkan ID mesin yang konsisten dari sistem yang berjalan di berbagai platform, seperti Windows, macOS, dan Linux. Ini membantu dalam menjaga keunikan dan ketahanan aplikasi dalam situasi berbagai lingkungan sistem.
-   Menggunakan Metode Penyedia ID Yang Berbeda: Node-machine-id menyediakan metode untuk mendapatkan ID mesin menggunakan berbagai penyedia, seperti UUID, serial disk, atau metode kustom. Ini memberikan fleksibilitas dalam memilih metode yang paling sesuai dengan kebutuhan aplikasi.
-   Keselarasan dengan Standar Platform: Paket ini dirancang untuk mematuhi standar platform terkait pengambilan ID mesin. Misalnya, di Windows, itu akan mencoba mendapatkan nomor serial disk, sementara di macOS, itu akan menggunakan UUID.
-   Penggunaan yang Sederhana: Node-machine-id menyediakan antarmuka yang sederhana dan mudah digunakan untuk mendapatkan ID mesin dari sistem. Ini memungkinkan pengembang untuk dengan cepat mengintegrasikan fitur ini ke dalam aplikasi mereka tanpa banyak kode tambahan.
-   Kompabilitas dengan Lingkungan Node.js: Paket ini didesain untuk berjalan dengan baik di lingkungan Node.js, dan dapat diinstal dan digunakan melalui npm, manajer paket standar untuk proyek Node.js.

node-machine-id sangat berguna dalam aplikasi yang memerlukan identifikasi unik dari mesin atau sistem tempat aplikasi dijalankan.

Ini dapat digunakan untuk mengimplementasikan fitur lisensi, kontrol akses, atau identifikasi perangkat keras dalam aplikasi Node.js dengan cara yang mudah dan andal.

## Langkah-Langkah

Buat folder bernama "contoh_nodejs_menampilkan_machine_id", kemudian masuk ke dalamnya.

Selanjutnya buat file "tampilkan-machine-id-asynchronous.js" dan isi dengan kode ini:

```
// file: tampilkan-machine-id-asynchronous.js

// import modul node-machine-id
const machineId = require("node-machine-id").machineId;

// ambil machine id nya
async function dapatkanMachineID(original) {
    let mcid = await machineId({ original: original });
    return mcid;
}

// bungkus dalam sebuah function
async function run() {
    let mcid = await dapatkanMachineID(true);
    console.log(mcid);
}

// jalankan
run();
```

Selanjutnya buat file "tampilkan-machine-id-synchronous.js" dan isi dengan kode ini:

```
// file: tampilkan-machine-id-synchronous.js

// import modul node-machine-id
const machineIdSync = require("node-machine-id").machineIdSync;

// ambil machine id nya
let mcid = machineIdSync({ original: true });
console.log(mcid);
```

Untuk menjalankan kode-kode tadi, buka folder projectnya via terminal, kemudian jalankan perintah:

```
node <nama_script>
```

## Pembahasan

### Pembahasan "tampilkan-machine-id-asynchronous.js"

Kode ini adalah contoh penerapan pemrograman asinkron di JavaScript menggunakan fungsi async/await.

Mari kita bahas langkah-langkahnya:

-   Import Modul node-machine-id: Pada baris awal, modul node-machine-id diimpor menggunakan pernyataan require. Modul ini digunakan untuk mendapatkan ID mesin dari sistem yang sedang berjalan.
-   Fungsi dapatkanMachineID: Ini adalah fungsi asinkron yang bertugas untuk mendapatkan ID mesin. Fungsi ini menggunakan kata kunci async, yang menunjukkan bahwa fungsi tersebut akan mengembalikan janji (promise) secara implisit. Dalam tubuh fungsi, ID mesin diperoleh menggunakan fungsi machineId dari modul node-machine-id. Dengan menggunakan kata kunci await, proses ini ditunda hingga hasilnya tersedia.
-   Fungsi run: Fungsi ini juga dideklarasikan sebagai async. Ini digunakan untuk menjalankan logika aplikasi utama. Di dalamnya, dapatkanMachineID dipanggil dengan parameter true, yang kemudian menunggu hasilnya menggunakan await. Setelah hasil diterima, nilai ID mesin dicetak ke konsol.
-   Jalankan: Terakhir, fungsi run dipanggil untuk memulai eksekusi program.

Jadi, keseluruhan kode ini bertujuan untuk mendapatkan ID mesin secara asinkron dan mencetaknya ke konsol.

Dengan menggunakan async/await, kode ini lebih mudah dipahami dan dijalankan secara bersamaan dengan operasi lainnya tanpa menghalangi eksekusi program.

### Pembahasan "tampilkan-machine-id-synchronous.js"

Kode ini adalah contoh penerapan pemrograman secara sinkron di JavaScript untuk mendapatkan ID mesin menggunakan modul node-machine-id.

Berikut adalah penjelasan singkatnya:

-   Import Modul node-machine-id: Modul node-machine-id diimpor menggunakan pernyataan require.
-   Fungsi machineIdSync: Ini adalah fungsi sinkron yang digunakan untuk mendapatkan ID mesin secara langsung. Karena fungsi ini bersifat sinkron, tidak perlu menunggu hasilnya, sehingga ID mesin langsung diperoleh saat pemanggilan fungsi tersebut.
-   Mendapatkan ID Mesin: Fungsi machineIdSync dipanggil dengan parameter { original: true } untuk mendapatkan ID mesin. Hasilnya disimpan dalam variabel mcid.
-   Cetak ID Mesin: Nilai ID mesin yang diperoleh kemudian dicetak ke konsol menggunakan console.log.

Dalam kode ini, proses mendapatkan ID mesin dilakukan secara sinkron, yang berarti eksekusi program akan berhenti dan menunggu sampai hasilnya diperoleh sebelum melanjutkan eksekusi program selanjutnya.

Ini berbeda dengan pendekatan asinkron di mana program dapat melanjutkan eksekusi dan melakukan tugas-tugas lain sambil menunggu hasil operasi asinkron.

## Penutup

Sekian dan terima kasih.
