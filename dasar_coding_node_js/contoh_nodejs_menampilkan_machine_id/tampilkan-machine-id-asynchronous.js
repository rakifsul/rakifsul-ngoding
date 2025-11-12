// import modul
const machineId = require("node-machine-id").machineId;

// dapatkan machine id nya
async function dapatkanMachineID(original) {
    let mcid = await machineId({ original: original });
    return mcid;
}

// panggil secara async await
async function run() {
    let mcid = await dapatkanMachineID(true);
    console.log(mcid);
}

// panggil pembungkusnya (run) tadi
run();
