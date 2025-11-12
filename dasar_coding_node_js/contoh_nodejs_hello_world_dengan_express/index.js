// import module express
const express = require("express");

// inisialisasi express
const server = express();

// handle request "/"
server.get("/", (req, res, next) => {
    // response dengan teks "Hello World!", kemudian akhiri
    res.write("Hello World!");
    res.end();
});

// jalankan server di port 3000
server.listen(3000, () => {
    console.log("Server berjalan di port 3000.");
});
