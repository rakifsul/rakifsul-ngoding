// begin: import modules
const bcrypt = require("bcryptjs");
// end: import modules

// nilai password
const password = "password";

// nilai hash password
const theHash = bcrypt.hashSync("password");
console.log(theHash);

// apakah input password cocok dengan hash?
let isMatch = bcrypt.compareSync(password, theHash);
console.log(isMatch);

// coba dengan input yang salah
isMatch = bcrypt.compareSync(password + "123", theHash);
console.log(isMatch);
