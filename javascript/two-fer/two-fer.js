
var TwoFer = function () {};
TwoFer.prototype.twoFer = function (who) {
  if (who == null){
    return "One for you, one for me."
  }
  else{
      return "One for " + who + ", one for me."
  }
  return who;
};

module.exports = TwoFer;

