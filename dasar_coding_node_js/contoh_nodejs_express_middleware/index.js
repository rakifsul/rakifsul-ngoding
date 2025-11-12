// import modules
const express = require("express");

// inisialisasi express
const app = express();

// middleware ini berjalan secara global
app.use((req, res, next) => {
    console.log("MIDDLEWARE 1");
    next();
});

// request get untuk "/" atau dengan kata lain halaman index
// tanpa middleware lokal
app.get("/", (req, res) => {
    console.log("INDEX");
    res.send("INDEX");
});

// request get untuk "/about" atau dengan kata lain halaman about
// dengan middleware lokal
// perhatikan bahwa parameter ke-2 diisi function. itu middleware nya
app.get(
    "/about",
    (req, res, next) => {
        console.log("MIDDLEWARE 2");
        next();
    },
    (req, res) => {
        console.log("ABOUT");
        res.send("ABOUT");
    }
);

// jalankan server di port 3000
app.listen(3000, () => {
    console.log("Server berjalan di port 3000");
});
