function rot13(str) {
  var res='';
  str=str.split("");
  for (let i=0;i<str.length;i++){
    if (/[a-z]/i.test(str[i])){
      str[i]=str[i].toUpperCase()
      let t = str[i].charCodeAt(0);
      t=t+13;
      if((t)>90){
        t= (t-90)+65-1
        }
        res+=(String.fromCharCode(t));
        console.log(res);
    }
    else{
      res+=str[i];
    }
  }
  return res;
}

rot13("SERR PBQR PNZC");
