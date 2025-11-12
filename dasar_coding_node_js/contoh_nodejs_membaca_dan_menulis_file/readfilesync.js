// import modul fs
const fs = require('fs');

// baca file secara synchronous
function readHello() {
    const hello = fs.readFileSync('./hello.txt', 'utf8');
    console.log(hello);
}


// panggil
readHello();