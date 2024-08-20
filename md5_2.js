const CryptoJS = require('crypto-js');

// MD5 hash to compare
const targetHash = 'aaedfac4a732ad7608d720886b69f289';

// List of words to test
const words = [
    "Rickrolling has taught us to be wary of random links more than any cyber security courses ever has.",
    "Meme",
    "jpeg",
    "InfoSec Image",
    "meme.jpg",
    "meme.jpeg",
    "aGlkZGVuX2luX3RoZV9kZXRhaWxz; ",
    "aGlkZGVuX2luX3RoZV9kZXRhaWxz",
    "aGlkZGVuX2luX3RoZV9kZXRhaWxz;",
    "0123456789abcdef",
    "hidden_in_the_details"
];

// Function to calculate MD5 hash of a given string
function md5Hash(text) {
    return CryptoJS.MD5(text).toString();
}

// Check each word
for (const word of words) {
    if (md5Hash(word) === targetHash) {
        console.log(`Match found: ${word}`);
        break;
    }
    else{
        console.log("No match found.");
    }
}
