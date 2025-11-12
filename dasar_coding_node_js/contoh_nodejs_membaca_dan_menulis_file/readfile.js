// import modul fs
const fs = require('fs');

// import modul util untuk mem-promise-kan yang bukan promise.
const util = require('util');


// baca file dengan metode callback
function readHello() {
    fs.readFile('./hello.txt', 'utf8', function (err, data) {
        console.log(data);
    });
}

// baca file dengan metode promise via async await
async function readHelloAsyncAwait() {
    const readFileAsyncAwait = util.promisify(fs.readFile); //di-promise-kan
    const hello = await readFileAsyncAwait('./hello.txt', 'utf8');
    console.log(hello);
}

// panggil keduanya
readHello();
readHelloAsyncAwait();