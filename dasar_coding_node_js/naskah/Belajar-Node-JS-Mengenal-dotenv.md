# Belajar Node JS Mengenal dotenv

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_dotenv

## Pendahuluan

Aplikasi yang dibuat dengan Node.js ada kalanya perlu konfigurasi.

Misalnya saja dalam aplikasi web diperlukan konfigurasi seperti:

-   Nama website
-   Base URL
-   Cookie secret
-   Dan lain-lain

Untuk mengubah konfigurasi tersebut, bisa saja dilakukan dengan mengubah kode, tapi itu kurang efisien.

Akan lebih baik jika konfigurasi tersebut disimpan dalam sebuah file terpisah agar saat kita ingin mengubahnya, kita tidak perlu mengubah script kode kita berulang kali.

Solusinya, kita bisa menggunakan package dotenv yang ada di NPM.

Mari kita coba...

## Lebih Lanjut tentang dotenv

dotenv adalah alat yang digunakan dalam pengembangan perangkat lunak untuk mengelola konfigurasi aplikasi dengan lebih efisien.

Dalam pengembangan perangkat lunak modern, penting untuk memisahkan konfigurasi dari kode sumber aplikasi untuk meningkatkan portabilitas, keamanan, dan fleksibilitas.

Dalam bagian ini, saya akan menjelaskan secara mendalam tentang dotenv, termasuk definisi, tujuan, manfaat, dan praktik terbaik.

### Definisi dotenv:

#### Konsep Dasar:

dotenv adalah alat yang memungkinkan pengembang menyimpan konfigurasi aplikasi seperti kunci API, URL database, atau pengaturan lingkungan lainnya dalam file teks terpisah. Nama "dotenv" berasal dari praktik menyimpan variabel lingkungan dalam file bernama ".env".

#### Implementasi:

Implementasi dotenv dapat berbeda-beda tergantung pada bahasa pemrograman atau lingkungan pengembangan yang digunakan. Biasanya, dotenv terdiri dari file teks sederhana yang berisi pasangan kunci-nilai yang dipisahkan oleh tanda sama dengan (=), dan aplikasi akan membaca file ini untuk mengambil konfigurasi saat memulai.

### Tujuan dotenv:

#### Memisahkan Konfigurasi dari Kode Sumber:

Salah satu tujuan utama dotenv adalah memisahkan konfigurasi dari kode sumber aplikasi. Dengan menggunakan file konfigurasi terpisah, pengembang dapat menghindari menyematkan konfigurasi langsung ke dalam kode, yang membuatnya lebih mudah dikelola dan diperbarui.

#### Keamanan:

Dengan menyimpan konfigurasi sensitif seperti kunci API atau sandi dalam file terpisah, dotenv membantu meningkatkan keamanan aplikasi. Ini mencegah informasi sensitif dari tersimpan di repositori kode sumber yang dapat diakses publik.

#### Portabilitas:

Menggunakan dotenv membuat aplikasi lebih mudah dipindahkan dari satu lingkungan ke lingkungan lainnya tanpa perlu mengubah kode sumber. Pengembang dapat dengan mudah mengonfigurasi aplikasi untuk lingkungan pengembangan, uji, dan produksi dengan file .env yang berbeda.

#### Fleksibilitas:

Dengan menyimpan konfigurasi dalam file .env terpisah, pengembang dapat dengan mudah mengubah konfigurasi tanpa perlu memodifikasi kode sumber. Ini memungkinkan penyesuaian cepat dan fleksibel terhadap perubahan lingkungan atau persyaratan aplikasi.

### Manfaat Penggunaan dotenv:

#### Kejelasan dan Organisasi Kode:

Dengan menggunakan dotenv, konfigurasi aplikasi dipisahkan dengan jelas dari kode sumber, meningkatkan kejelasan dan organisasi kode.

#### Keamanan Konfigurasi:

Dengan menyimpan konfigurasi sensitif di luar kode sumber, dotenv membantu meningkatkan keamanan aplikasi dengan mencegah paparan informasi sensitif.

#### Fleksibilitas dan Scalability:

dotenv memungkinkan aplikasi untuk dengan mudah beradaptasi dengan perubahan lingkungan atau persyaratan dengan memungkinkan pengaturan konfigurasi yang fleksibel dan skalabel.

#### Portabilitas dan Reproduktibilitas:

Dengan menyimpan konfigurasi dalam file .env terpisah, aplikasi dapat dipindahkan dari satu lingkungan ke lingkungan lainnya tanpa perlu memodifikasi kode sumber, meningkatkan portabilitas dan reproduktibilitas.

#### Pengujian yang Mudah:

Dengan menggunakan konfigurasi yang dipisahkan, dotenv membuat pengujian aplikasi menjadi lebih mudah karena pengembang dapat dengan mudah menyediakan konfigurasi yang berbeda untuk lingkungan pengembangan dan pengujian.

### Praktik Terbaik dalam Menggunakan dotenv:

#### Jangan Simpan Informasi Rahasia di Repositori Kode Sumber:

Pastikan untuk tidak menyimpan informasi rahasia seperti kunci API atau sandi di dalam repositori kode sumber. Gunakan file .env untuk menyimpan informasi sensitif tersebut.

#### Gunakan Nama Variabel yang Deskriptif:

Gunakan nama variabel yang deskriptif untuk memudahkan pengelolaan dan pemahaman konfigurasi aplikasi. Ini membantu meningkatkan kejelasan kode.

#### Gunakan .env.example sebagai Template:

Sertakan file .env.example di repositori kode sumber sebagai template untuk konfigurasi aplikasi. Ini membantu pengembang baru memahami variabel yang dibutuhkan.

#### Gunakan Penanganan Error dengan Bijak:

Pastikan untuk menangani error dengan bijaksana saat membaca atau menggunakan konfigurasi dari dotenv. Ini membantu mencegah aplikasi gagal karena konfigurasi yang tidak valid atau hilang.

#### Perbarui dan Monitor Konfigurasi secara Teratur:

Perbarui dan monitor file .env secara teratur untuk memastikan bahwa konfigurasi aplikasi tetap up-to-date dan sesuai dengan kebutuhan proyek.
dotenv adalah alat yang bermanfaat dalam pengembangan perangkat lunak modern untuk mengelola konfigurasi aplikasi dengan lebih efisien.

Dengan memisahkan konfigurasi dari kode sumber, dotenv membantu meningkatkan keamanan, fleksibilitas, dan portabilitas aplikasi.

Dengan mengikuti praktik terbaik, pengembang dapat memanfaatkan potensi penuh dotenv untuk mengelola konfigurasi aplikasi dengan lebih baik.

## Tujuan

Berikut ini adalah tujuan dari tutorial ini:

-   Pembaca mengenal dotenv dan mampu menggunakannya.

## Prasyarat

Berikut ini adalah prasyarat dari tutorial ini:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Men-download dan meng-install Node.js dan NPM.
-   Bisa meng-akses Node.js dan NPM dari PowerShell di folder manapun.

## Langkah-Langkah

Pertama, buatlah project Node.js bernama "contoh_nodejs_dotenv" dengan cara yang telah dijelaskan di "[Belajar Node JS Cara Membuat Project](https://github.com/rakifsul/belajar_coding_node_js/blob/main/Belajar-Node-JS-Cara-Membuat-Project.md)".

Selanjutnya, ubah file "package.json" menjadi seperti ini:

```
{
    "name": "contoh_nodejs_dotenv",
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
        "dotenv": "^16.3.2"
    }
}
```

Selanjutnya, isi file "index.js" dengan kode ini:

```
const dotEnv = require("dotenv");
dotEnv.config();

console.log(process.env.APP_NAME, typeof process.env.APP_NAME);
console.log(process.env.BASE_URL, typeof process.env.BASE_URL);
console.log(process.env.NUM_OF_CORES, typeof process.env.BASE_URL);
```

Selanjutnya, buat file bernama ".env" pada root folder project ini, kemudian isi dengan:

```
APP_NAME=TUTORIAL_DOTENV
BASE_URL=http://localhost:3000
NUM_OF_CORES=100
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
TUTORIAL_DOTENV string
http://localhost:3000 string
100 string
```

## Pembahasan

Pertama-tama, kita membuat project Node.js dan mengisinya dengan beberapa script.

Selanjutnya, kita menjalankan perintah npm install tanpa diikuti nama package.

Itu maksudnya adalah untuk meng-install seluruh dependencies yang tertulis di "package.json", dalam hal ini hanya dotenv.

Pada "index.js", kita mulai dari mengimpor modul dotenv:

```
const dotEnv = require("dotenv");
```

Kemudian kita menginisialisasinya;

```
dotEnv.config();
```

Mulai dari sini, seluruh isi file ".env" akan masuk ke memori.

Sehingga:

```
console.log(process.env.APP_NAME, typeof process.env.APP_NAME);
console.log(process.env.BASE_URL, typeof process.env.BASE_URL);
console.log(process.env.NUM_OF_CORES, typeof process.env.BASE_URL);
```

Kita bisa mengaksesnya dengan process.env diikuti dengan key yang ada di file ".env":

```
APP_NAME=TUTORIAL_DOTENV
BASE_URL=http://localhost:3000
NUM_OF_CORES=100
```

Dengan kata lain:

-   Untuk mengakses APP_NAME di ".env", process.env.APP_NAME
-   Untuk mengakses BASE_URL di ".env", process.env.BASE_URL
-   Untuk mengakses NUM_OF_CORES di ".env", process.env.NUM_OF_CORES

Semua tipe data yang tadi diimpor adalah string, sehingga jika perlu tipe lain mungkin perlu dikonversi dulu.

Kira-kira seperti itu...

## Penutup

Sekarang, seharusnya Anda telah mengenal dotenv dan mampu menggunakannya.
