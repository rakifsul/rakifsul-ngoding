// import modul
const machineIdSync = require("node-machine-id").machineIdSync;

// dapatkan machine id nya
let mcid = machineIdSync({ original: true });
console.log(mcid);