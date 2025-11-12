# Belajar Node JS Mengenal Puppeteer

## Source Code Project Ini

https://github.com/rakifsul/belajar_coding_node_js/tree/main/contoh_nodejs_puppeteer

## Pendahuluan

Setelah Anda belajar tentang Axios pada "[Belajar Node JS Mengenal Axios](https://github.com/rakifsul/belajar_coding_node_js/blob/main/Belajar-Node-JS-Mengenal-Axios.md)", mungkin Anda akan menyadari sesuatu.

Yakni, isi HTML yang diperoleh melalui Axios tadi masih bisa diolah.

Dengan library tertentu, mengekstrak data berharga dari HTML yang dikembalikan bisa dilakukan dengan mudah.

TAPI... itu dengan asumsi bahwa data berharga tersebut ada di HTML nya, bukan tersembunyi dalam JavaScript.

Lalu, bagaimana dengan halaman web yang kontennya dinamis, dalam artian hanya tampil setelah diolah dengan JavaScript?

Jawabannya ada pada Puppeteer.

Puppeteer itu sendiri mengandalkan web browser untuk melakukan perolehan data.

Analoginya:

-   Data yang dikembalikan dari Axios menyerupai browser view source.
-   Data yang dikembalikan dari Puppeteer menyerupai browser inspect element.

Di artikel ini, saya akan memberikan contoh sederhana untuk menggunakan Puppeteer.

## Lebih Lanjut tentang Puppeteer

Puppeteer adalah sebuah library Node.js yang dikembangkan oleh tim Google Chrome.

Ini memungkinkan otomatisasi browser headless (tanpa UI) melalui antarmuka yang ramah pengembang.

Berikut adalah beberapa poin penting tentang Puppeteer:

-   Automasi Browser: Puppeteer memungkinkan Anda mengendalikan browser Chrome atau Chromium secara programatik melalui JavaScript. Anda dapat mengotomatiskan interaksi seperti klik, isi formulir, navigasi, dan lainnya.
-   Headless Mode: Salah satu fitur utama dari Puppeteer adalah kemampuannya untuk menjalankan browser dalam mode tanpa kepala (headless). Ini berarti browser tidak akan memiliki antarmuka pengguna grafis (GUI), yang membuatnya lebih efisien untuk menjalankan skrip otomatisasi di latar belakang.
-   Testing Otomatis: Puppeteer sangat berguna untuk pengujian otomatis di situs web. Anda dapat mengotomatiskan serangkaian aksi pengguna untuk menguji fungsi dan kinerja situs web Anda.
-   Web Scraping: Dengan menggunakan Puppeteer, Anda dapat melakukan web scraping, yaitu mengekstrak data dari halaman web secara otomatis. Ini dapat berguna untuk mengumpulkan informasi dari situs web yang tidak menyediakan API.
-   Rendering dan Screenshot: Puppeteer dapat digunakan untuk merender halaman web dan mengambil tangkapan layar (screenshot). Ini berguna jika Anda perlu membuat laporan visual atau melakukan pemantauan visual terhadap perubahan pada situs web.
-   Deteksi dan Bypass CAPTCHA: Dengan menggunakan Puppeteer, Anda dapat memprogram agar melakukan navigasi ke halaman web yang membutuhkan CAPTCHA, dan dalam beberapa kasus, Anda bahkan dapat membuat skrip yang secara otomatis memecahkan CAPTCHA.
-   Dukungan untuk Chrome DevTools Protocol: Puppeteer dibangun di atas protokol DevTools Chrome, yang memberikan kontrol penuh terhadap perilaku browser. Ini memungkinkan Anda untuk melakukan debugging, analisis, dan optimisasi performa.

Keseluruhan, Puppeteer adalah alat yang sangat kuat dan fleksibel untuk mengotomatisasi interaksi dengan browser, baik untuk pengujian otomatis, web scraping, atau tujuan lainnya.

## Tujuan

Tujuan dari artikel ini adalah:

-   Pembaca mengenal Puppeteer.
-   Pembaca mampu mencoba menggunakan Puppeteer.

## Prasyarat

Berikut ini adalah prasyarat dari tutorial ini:

-   Menggunakan sistem operasi Windows 10 ke atas.
-   Men-download dan meng-install Node.js dan NPM.
-   Bisa mengakses Node.js dan NPM dari PowerShell di folder manapun.

## Langkah-Langkah

Pertama, buatlah project Node.js bernama "contoh_nodejs_puppeteer" dengan cara yang telah dijelaskan di "[Belajar Node JS Cara Membuat Project](https://github.com/rakifsul/belajar_coding_node_js/blob/main/Belajar-Node-JS-Cara-Membuat-Project.md)".

Selanjutnya, ubah file "package.json" menjadi seperti ini:

```
{
  "name": "contoh_nodejs_puppeteer",
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
    "puppeteer": "^22.8.0"
  }
}
```

Selanjutnya, ubah file "index.js" menjadi seperti ini:

```
// import module
const puppeteer = require("puppeteer");

(async () => {
    // jalankan browser dan buka halaman kosong
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // navigasi ke URL ini
    // sebagai referensi, kunjungi https://quotes.toscrape.com dan lihat menunya.
    // di sana ada menu bertuliskan "reading".
    // disclaimer: mungkin halaman tersebut telah berubah saat Anda mengunjunginya.
    await page.goto("https://quotes.toscrape.com");

    // terapkan ukuran layar
    await page.setViewport({ width: 1024, height: 768 });

    // tunggu hingga elemen dengan selector ini muncul
    await page.waitForSelector("body > div > div:nth-child(2) > div.col-md-4.tags-box > span:nth-child(7) > a");

    // baca teks-nya
    let result = await page.evaluate(() => {
        let elements = Array.from(document.querySelectorAll("body > div > div:nth-child(2) > div.col-md-4.tags-box > span:nth-child(7) > a"));
        let textContent = elements.map((element) => {
            return element.textContent;
        });
        return textContent;
    });

    // tampilkan hasilnya
    console.log(result);

    // tutup puppeteer browser
    await browser.close();
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
[ 'reading' ]
```

## Pembahasan

Kode ini menggunakan Puppeteer untuk mengotomatisasi browser Chrome atau Chromium dalam menjalankan serangkaian tindakan pada halaman web tertentu.

Mari kita jelaskan baris per baris:

-   `const puppeteer = require("puppeteer");`: Ini mengimpor modul Puppeteer ke dalam skrip Node.js Anda. Ini memungkinkan Anda menggunakan semua fungsi dan fitur yang disediakan oleh Puppeteer.
-   `(async () => { ... })();`: Ini adalah fungsi anonim yang didefinisikan dan segera dieksekusi (self-invoking). Ini menggunakan async/await untuk mengelola asinkronitas dalam JavaScript.
-   `const browser = await puppeteer.launch();`: Baris ini memulai browser menggunakan metode `puppeteer.launch()`. Ini akan membuat instance baru dari browser Chrome atau Chromium yang akan digunakan untuk menjalankan tindakan-tindakan berikutnya.
-   `const page = await browser.newPage();`: Ini membuat halaman baru di dalam browser yang telah dibuka sebelumnya. Instance halaman baru ini akan digunakan untuk melakukan interaksi selanjutnya, seperti navigasi ke URL tertentu dan mengevaluasi elemen-elemen di dalamnya.
-   `await page.goto("https://quotes.toscrape.com");`: Ini adalah langkah penting, di mana skrip melakukan navigasi ke URL "https://quotes.toscrape.com". Ini membuka halaman web yang ingin kita ambil informasinya.
-   `await page.setViewport({ width: 1024, height: 768 });`: Baris ini menetapkan ukuran viewport (area yang terlihat oleh pengguna) pada halaman web. Dalam contoh ini, viewport ditetapkan dengan lebar 1024 piksel dan tinggi 768 piksel.
-   `await page.waitForSelector("body > div > div:nth-child(2) > div.col-md-4.tags-box > span:nth-child(7) > a");`: Ini adalah langkah yang memastikan bahwa elemen dengan selector yang ditentukan telah muncul di halaman. Skrip akan menunggu hingga elemen tersebut tersedia sebelum melanjutkan.
-   `let result = await page.evaluate(() => { ... });`: Ini menggunakan metode `page.evaluate()` untuk mengeksekusi fungsi evaluasi di dalam lingkungan halaman web. Dalam kasus ini, itu akan mengeksekusi fungsi yang mencari elemen dengan selector tertentu dan mengambil teksnya.
-   `console.log(result);`: Hasil yang diperoleh dari evaluasi sebelumnya kemudian dicetak ke konsol. Ini akan menampilkan teks yang diambil dari elemen yang diidentifikasi sebelumnya.
-   `await browser.close();`: Langkah terakhir adalah menutup browser menggunakan browser.close() setelah selesai melakukan tindakan-tindakan yang diinginkan.

Ingat bahwa pada `let result = await page.evaluate(() => { ... });`, kode dalam blok fungsi yang menjadi parameter page.evaluate, scope-nya bukan di Node.js, melainkan di browser, jadi, itu JavaScript-nya browser.

Keseluruhan, skrip ini mengotomatisasi browser untuk membuka halaman "https://quotes.toscrape.com", menunggu hingga elemen tertentu muncul, dan kemudian mengambil teks dari elemen tersebut untuk kemudian dicetak ke console.

## Penutup

Begitulah contoh sederhana penggunaan puppeteer.

Jika ingin belajar lebih lanjut, kunjungi dokumentasinya.
