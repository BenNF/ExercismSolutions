var DnaTranscriber = function () {};

DnaTranscriber.prototype.toRna = function (s) {
    return s.split("").map(replace).join("")
};
function replace(c) {
  switch (c){
      case 'G': return 'C';
      case 'C': return 'G';
      case 'T': return 'A';
      case 'A': return 'U';
      default: throw new Error("Invalid input")
  }
}

module.exports = DnaTranscriber;