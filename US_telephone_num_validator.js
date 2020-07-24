function telephoneCheck(str) {
  var test =/(^[1]?\s?)(\d{3}[-\s]?\d{3}[-\s]?\d{4})$|(^[1]?\s?[(]\d{3}?[)]\s?\d{3}?[-]\d{4}?)$/;
  
  return (test).test(str);
}

console.log(telephoneCheck("2767890382"));
console.log(telephoneCheck("1 (555) 555-5555"));
