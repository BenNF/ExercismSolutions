var Cipher = function(key){
    if (key == null){
        this.key = "";
        for(var i =0; i < 100; i++){
            this.key += String.fromCharCode(Math.floor(Math.random()*26)+97)
        }
    }
    else{
        var keyList = key.split("");
        for(var i =0; i < keyList.length; i++){
            if (keyList[i] != keyList[i].toLowerCase()){
                throw new Error("Invalid Key")
            }
        }
        this.key = key;
    }

};
Cipher.prototype.decode = function(msg){

};

Cipher.prototype.encode = function (msg) {

};

module.exports=Cipher;

c = new Cipher("aaaaaaaaaaaaaaa");
console.log(c.key);