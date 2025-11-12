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
