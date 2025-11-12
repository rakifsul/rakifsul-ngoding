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
