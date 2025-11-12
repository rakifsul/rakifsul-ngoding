# Belajar Node JS Cara Membuat Project

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_create

## Pendahuluan

Node.js adalah sebuah platform runtime environment yang bisa digunakan untuk banyak hal...

Salah satu manfaat dari Node.js adalah membuat backend dari aplikasi web.

Tapi, sebenarnya tidak hanya itu.

Secara keseluruhan, Node.js juga bisa digunakan untuk membuat aplikasi command line, bahkan menjadi bagian dari Electron js yang digunakan untuk aplikasi desktop GUI.

Saat Node.js diinstall, biasanya NPM juga ikut terinstall.

NPM itu sendiri adalah package manager yang fungsinya untuk memanajemen package-package yang digunakan dalam sebuah project Node.js, bahkan selain Node.js sekalipun.

Jadi tidak aneh jika React juga bisa menggunakan NPM untuk memanajemen package-package yang digunakan di dalamnya.

Dalam tutorial ini, kita akan membuat project Node.js dari nol dengan menggunakan npm.

## Lebih Lanjut tentang Node.js

Node.js adalah lingkungan runtime JavaScript yang dibangun di atas mesin JavaScript V8 dari Google Chrome.

Berikut adalah beberapa poin penting tentang Node.js:

-   JavaScript di Sisi Server: Node.js memungkinkan untuk menjalankan kode JavaScript di sisi server, yang sebelumnya terbatas pada browser. Ini memungkinkan pengembang untuk menggunakan JavaScript di kedua sisi, baik di sisi klien (browser) maupun di sisi server.
-   Non-blocking dan Event-driven: Node.js menggunakan model pemrograman non-blocking dan event-driven yang memungkinkan untuk menangani banyak koneksi secara bersamaan dengan cepat dan efisien. Ini berguna dalam membangun aplikasi yang skala besar atau real-time seperti aplikasi web, streaming, dan permainan.
-   Asynchronous I/O: Node.js memungkinkan untuk melakukan operasi I/O secara asinkron, yang berarti operasi-operasi seperti membaca atau menulis ke berkas, mengambil data dari database, atau memanggil API eksternal dapat dilakukan tanpa menghentikan eksekusi program. Hal ini mengoptimalkan penggunaan CPU dan mempercepat respons aplikasi.
-   NPM (Node Package Manager): Node.js dilengkapi dengan NPM, manajer paket yang kuat untuk mengelola dependensi dan paket-paket JavaScript. NPM memungkinkan untuk dengan mudah menginstal, mengelola, dan membagikan kode JavaScript dalam proyek-proyek Node.js.
-   Komunitas yang Besar: Node.js memiliki komunitas pengembang yang besar dan aktif yang terus berkontribusi dalam pengembangan, dokumentasi, dan sumber daya belajar. Ini membuat Node.js menjadi salah satu ekosistem pengembangan yang paling populer dan berkembang pesat di dunia.
-   Fleksibilitas dan Skalabilitas: Node.js cocok digunakan untuk berbagai jenis aplikasi, mulai dari aplikasi web, aplikasi backend, server API, hingga aplikasi real-time seperti chat atau game. Dengan model non-blocking dan event-driven, Node.js juga dapat dengan mudah di-skala secara horizontal untuk menangani beban yang lebih besar.
-   Cross-platform: Node.js dapat dijalankan di berbagai platform, termasuk Windows, macOS, dan Linux. Ini membuatnya menjadi pilihan yang fleksibel untuk pengembangan aplikasi yang berjalan di berbagai lingkungan.

Secara keseluruhan, Node.js adalah lingkungan runtime yang kuat dan fleksibel untuk menjalankan kode JavaScript di sisi server.

Dengan model pemrograman non-blocking dan event-driven, serta dukungan dari NPM dan komunitas yang besar, Node.js menjadi pilihan yang populer untuk pengembangan aplikasi modern.

## Lebih Lanjut tentang NPM

NPM (Node Package Manager) adalah manajer paket untuk ekosistem Node.js yang memungkinkan untuk mencari, menginstal, dan mengelola paket-paket JavaScript dalam proyek-proyek Node.js.

Berikut adalah beberapa poin penting tentang NPM:

-   Manajer Paket: NPM adalah manajer paket yang kuat yang digunakan untuk mengelola dependensi dan paket-paket JavaScript dalam proyek-proyek Node.js. Ini memungkinkan pengembang untuk mengatur dan menyimpan kode JavaScript dari berbagai sumber dengan mudah.
-   Repository Publik: NPM memiliki repositori publik yang luas yang berisi ribuan paket-paket JavaScript yang tersedia untuk digunakan. Pengembang dapat mencari dan menemukan paket yang sesuai dengan kebutuhan proyek mereka di repositori publik NPM.
-   Instalasi Paket: NPM memungkinkan untuk menginstal paket-paket JavaScript dalam proyek dengan mudah menggunakan perintah npm install. NPM akan mengunduh dan menginstal paket beserta dependensinya ke dalam direktori proyek secara otomatis.
-   Manajemen Versi: NPM memungkinkan untuk mengelola versi paket dengan mudah. Pengembang dapat menginstal versi spesifik dari paket, memperbarui paket ke versi terbaru, atau mengunci versi paket untuk memastikan konsistensi dalam proyek.
-   Scripting: NPM memungkinkan untuk menambahkan skrip-sript kustom ke dalam berkas package.json yang mempermudah dalam menjalankan tugas-tugas tertentu, seperti kompilasi kode, menjalankan uji coba, atau memulai server pengembangan.
-   Paket Lokal dan Global: NPM memungkinkan untuk menginstal paket-paket secara lokal dalam proyek atau secara global di seluruh sistem. Pengembang dapat memilih untuk menggunakan paket dalam ruang lingkup proyek atau membuatnya tersedia secara global di seluruh sistem.
-   Kemudahan Kolaborasi: NPM memfasilitasi kolaborasi dan berbagi kode antar pengembang. Pengembang dapat dengan mudah berbagi proyek dan dependensinya dengan orang lain menggunakan file package.json dan repositori publik NPM.

Secara keseluruhan, NPM adalah alat yang sangat penting dalam ekosistem Node.js yang memungkinkan untuk mencari, menginstal, dan mengelola paket-paket JavaScript dengan mudah dalam proyek-proyek Node.js.

Ini membantu meningkatkan produktivitas dan memperluas fungsionalitas proyek dengan menggunakan kode dari komunitas yang luas dan beragam.

## Tujuan

Berikut ini adalah tujuan dari tutorial ini:

-   Pembaca mampu membuat project Node.js dari nol.
-   Pembaca mengenal Node.js dan NPM.

## Prasyarat

Berikut ini adalah prasyarat dari tutorial ini:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Men-download dan meng-install Node.js dan NPM.
-   Bisa meng-akses Node.js dan NPM dari PowerShell di folder manapun.

## Langkah-Langkah

Pertama, pastikan Anda telah meng-install Node.js dan NPM.

Selanjutnya, buatlah folder bernama "contoh_nodejs_create".

Sebenarnya, nama foldernya bisa apapun, tapi dalam tutorial ini, gunakan saja nama tersebut agar tutorial ini lebih mudah dipahami.

Sekarang, buka folder "contoh_nodejs_create" dengan command line.

Kemudian, jalankan:

```
npm init -y
```

Nanti, akan muncul file bernama "package.json" yang isinya seperti ini:

```
{
  "name": "contoh_nodejs_create",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Selanjutnya, Anda bisa membuat file baru bernama "index.js" di dalam folder tersebut.

Alternatifnya, Anda bisa ganti "index.js" dengan "yanglain.js" di file "package.json" dan membuat file "yanglain.js" bukannya "index.js" di dalam folder "tutorial-0".

Dengan kata lain, bebas-bebas saja...

Sekarang, buka file "index.js" dengan teks editor, kemudian isi dengan kode ini:

```
// mem-print teks "hello world".
console.log("hello world");
```

Selanjutnya, jalankan:

```
node index.js
```

Nanti akan muncul output:

```
hello world
```

Sampai di sini langkah-langkahnya selesai.

## Pembahasan

Pertama-tama, kita telah selesai membuat project dengan perintah:

```
npm init -y
```

Perintah tersebut akan membuatkan "package.json" dengan isi default.

Jika tanpa "-y":

```
npm init
```

Nanti Anda akan melihat prompt untuk melakukan perubahan isi dari "package.json".

Namun, jika Anda ingin mengubah isi dari "package.json", sebenarnya Anda juga bisa menggunakan teks editor setelah "package.json" dibuat.

Jadi, bebas-bebas sajalah...

Sekarang, kita bahas isi dari file "index.js".

Script "index.js" yang berisi:

```
// mem-print teks "hello world".
console.log("hello world");
```

Tidak mem-print:

```
// mem-print teks "hello world".
```

Tapi hanya:

```
hello world
```

Saja. Itu karena karakter "//" gunanya adalah untuk menandai komentar dan setiap komentar tidak dieksekusi.

Jadi, tanda "//" berfungsi ganda: sebagai komentar dan untuk menonaktifkan kode.

Setelah project dibuat, Anda bisa dengan aman meng-install package-package dari NPM.

Karena, daftarnya akan dimasukkan ke file "package.json".

Tepatnya di property "dependencies" jika menggunakan perintah:

```
npm install <nama-package>
```

Dan di property "devDependencies" jika menggunakan perintah:

```
npm install <nama-package> --save-dev
```

Tapi ingat, perintah tadi harus dijalankan dalam folder project, yakni yang ada file "package.json"-nya.

## Penutup

Sekarang, seharusnya Anda telah mengenal Node.js, NPM, dan cara menggunakannya.

Membuat project Node.js seharusnya tidak masalah sekarang.
