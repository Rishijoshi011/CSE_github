// // server.mjs
// import { createServer } from 'node:http';

// const server = createServer((req, res) => {
//     res.writeHead(200, { 'Content-Type': 'text/plain' });
//     res.end('Hello World\n');
// });

// // starts a simple http server locally on port 3000
// server.listen(3000, '127.0.0.1', () => {
//     console.log('Listening on 127.0.0.1:3000');
// });

// run with `node server.mjs`

// import { some } from './3_export.js';
// console.log(some); // ! {some} will not work because in node js using {} is named import and when we {} it will look for named export which is not present in 3_export.js so it will give error so if you want to use defult export then you have to import without {}  
    
import some from './3_export.js';
console.log(some); 