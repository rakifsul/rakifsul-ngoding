// import module http
const http = require("http");

// buat server. dan apapun request nya...
const server = http.createServer((req, res) => {
    // response dengan teks hello world. kemudian akhiri
    res.write("Hello World!");
    res.end();
});

// jalankan server di port 3000
server.listen(3000, () => {
    console.log("Server berjalan di port 3000.");
});
