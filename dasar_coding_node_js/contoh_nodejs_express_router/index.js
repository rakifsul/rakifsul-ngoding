// import module express
const express = require("express");

// inisialisasi express
const app = express();

// begin: import routers
const indexRouter = require("./routes/index.js");
const aboutRouter = require("./routes/about.js");
// end: import routers

// begin: gunakan sebagai routers. parameter pertama adalah path prefix nya
app.use("/", indexRouter);
app.use("/about", aboutRouter);
// end: gunakan sebagai routers. parameter pertama adalah path prefix nya

// jalankan server di port 3000
app.listen(3000, () => {
    console.log("Server berjalan di port 3000");
});
