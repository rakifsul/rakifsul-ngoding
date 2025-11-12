// import modul express
const express = require("express");

// inisialisasi express
const app = express();


// handle get "/"
app.get("/", (req, res, next) => {
	// kembalikan file index.html
    res.sendFile(__dirname + "/views/" + "index.html");
});

// dengar di port 3000
app.listen(3000, () => {
    console.log("Server berjalan di port 3000");
});
