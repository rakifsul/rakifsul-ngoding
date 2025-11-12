// import modul dotenv
const dotEnv = require("dotenv");

// inisialisasi dotenv, di sini file .env dibaca
dotEnv.config();

// tampilkan isi .env
console.log(process.env.APP_NAME, typeof process.env.APP_NAME);
console.log(process.env.BASE_URL, typeof process.env.BASE_URL);
console.log(process.env.NUM_OF_CORES, typeof process.env.BASE_URL);
