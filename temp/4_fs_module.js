// ! while using sync function it is same as the async functions it holds the execution of program unitl that function completes its task

// * in our case we will need sync function because of our code stpes as u can see

// import http from 'node:http';

// const server = http.createServer((req, res) => {
//     res.writeHead(200, {'content-type' : 'text/plain'});
//     res.end("Hello World\n");
// });

// server.listen(3000, '127.0.0.1', () => {
//     console.log("Listening on 127.0.0.1:3000");
// });

import fs from "fs";
fs.rmSync("4_Demo", { recursive: true, force: true }, () => {
    console.error("Directory removed");
});

fs.mkdirSync("4_Demo", () => {
    console.log("Directory created");
});
fs.writeFileSync("4_Demo/hello.txt", "Hello from Node.js!", () => {
    console.log("File created");
});

const data = fs.readFileSync("4_Demo/hello.txt", "utf-8", () => {
    console.log("File read");
});

console.log(data);

// try{
//     fs.rmSync("4_Demo", {recursive: true, force: true});

//     fs.mkdirSync("4_Demo");

//     fs.writeFileSync("4_Demo/hello.txt", "Hello World!!");
//     const data = fs.readFileSync("4_Demo/hello.txt", 'utf-8');
//     console.log(data);
// } catch(err){
//     console.error(err);
// }
