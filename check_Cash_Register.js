function checkCashRegister(price, cash, cid) {
  var change = cash-price;
  var arr =[];
  var res=[];
  var res2=[];
  var ch_amnt={"PENNY":0.01,"NICKEL":0.05,"DIME":0.1,"QUARTER":0.25,"ONE":1,"FIVE":5,"TEN":10,"TWENTY":20,"ONE HUNDRED":100};
  var avl={};
  var final={status:'',change:[]};
  for (let v of cid){
    avl[v[0]]=(parseInt(v[1]/ch_amnt[v[0]]));
  }
  cid.forEach((a)=>arr.push(ch_amnt[a[0]]));
  arr= arr.sort((a,b)=>(a-b));
  arr.forEach((a)=>{ const key = Object.keys(ch_amnt).find(key => ch_amnt[key] === a);
  res.push([key,a]);
  res2.push([key,0]);
  });
  var flag=true;
  var c=arr.length-1;
  while (flag&&c>=0){
    var e =res[c][1];
    if (change - e >=0){
      for (let r=0;r<cid.length;r++){
        if (cid[r][0]===res[c][0]){
          var index = r;
          break;
        }
      }
      while ((change - e >=0)&&(cid[index][1]>0)){
        change =change -e;
        cid[index][1] -=e;
        res2[c][1] += e;
        change = Math.round(change*100)/100;
        res2[c][1] = Math.round(res2[c][1]*100)/100;
        cid[index][1] = Math.round(cid[index][1]*100)/100;
        //console.log(res2[c][1],change)
  
        //console.log(e, change, cid[index][1],res2[c][1])
    }
    }
    if (change ===0){
      flag = false;
    }
    c-=1;
  }

  if (flag){
    final.status="INSUFFICIENT_FUNDS";
    return(final);
  }else{
    var func = function(a){
      return(a[1]==0);}
    var bool = cid.every(func);
    if (!bool){
    final.status="OPEN";
    res2.forEach((a)=>{
      if (a[1]!==0){
        final.change.unshift(a);  }
    });
    return(final);}
    else{
      final.status ="CLOSED";
      final.change=res2;
      return(final);
    }
  }


  // return change;
}
console.log(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
console.log(checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));
console.log(checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));
