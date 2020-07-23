function convertToRoman(num) {
  var rom ={0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC",100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM",1000:"M",2000:"MM",3000:"MMM"};
  var res=""
  if (num<10000){
    if (num>999){
      var t = parseInt(num/1000);
      res+=(rom[t*1000]);
      num=num%1000;
    }
    if(num>99){
      var h = parseInt(num/100);
      res+=(rom[h*100]);
      num= num%100}
    if (num>9){
      var t=parseInt(num/10);
      res+=(rom[t*10]);
      num=num%10;}
    if ((num%10)!=0){
    var o=num%10;
    res+=(rom[o])
    }
    }

 return res;
}

console.log(convertToRoman(400));
