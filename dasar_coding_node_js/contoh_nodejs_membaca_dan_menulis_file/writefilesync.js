// import modul fs
const fs = require('fs');

// tulis file
function writeHello() {
    fs.writeFileSync('./hello-write-file-sync.txt', "hello world writeFileSync");
}

// panggil tulis file
writeHello();