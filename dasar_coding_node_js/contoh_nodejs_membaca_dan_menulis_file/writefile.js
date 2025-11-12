// import modul fs untuk membaca/menulis file
const fs = require('fs');

// import modul util untuk mem-promise-kan yang belum promise.
const util = require('util');

// tulis file dengan metode callback
function writeHello() {
    fs.writeFile('./hello-write-file.txt', "hello world writeFile", function () {
        console.log('file sudah ditulis.');
    })
}

// tulis file dengan metode promise via async await.
async function writeHelloAsyncAwait() {
    const writeFileAsyncAwait = util.promisify(fs.writeFile); // di-promise-kan
    await writeFileAsyncAwait('./hello-write-file-async-await.txt', "hello world writeFileAsyncAwait");
    console.log('file sudah ditulis.');
}

// panggil keduanya
writeHello();
writeHelloAsyncAwait();