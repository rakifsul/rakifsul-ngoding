// import express
const express = require("express");

// buat routernya
const router = express.Router();

// handle request "/"
router.get("/", (req, res) => {
    // kirim teks bertuliskan "INDEX"
    res.send("INDEX");
});

// export modul ini
module.exports = router;
