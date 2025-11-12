// import express
const express = require("express");

// buat routernya
const router = express.Router();

// handle request /about.
// di parameternya tertulis "/" karena saat
// di-use di root index.js sudah ada path "/about"
router.get("/", (req, res) => {
    // kirim teks bertuliskan "ABOUT"
    res.send("ABOUT");
});

// export module ini
module.exports = router;
