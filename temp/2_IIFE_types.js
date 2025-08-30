(function () {
    console.log("Standard IIFE");
})();

// Arrow function IIFE
(() => {
    console.log("Arrow function IIFE");
})();

// Using unary operators
!(function () {
    console.log("IIFE with !");
})();

// Using void operator
void (function () {
    console.log("IIFE with void");
})();

// IIFE with parameters
((name) => {
    console.log(`Hello, ${name}!`);
})("Node.js");
