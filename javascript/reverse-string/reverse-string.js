var reverseString = function (str) {
    return str.split("").reverse().join("")
};
module.exports = reverseString;
console.log(reverseString("Hello World"));