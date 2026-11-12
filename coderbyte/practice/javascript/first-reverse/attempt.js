function FirstReverse(str) { 
  let newS = "";
  for (let x = str.length; x>-1; x--){
    newS += str.charAt(x);
  }
  // code goes here  
  return newS; 

}
   
// keep this function call here 
console.log(FirstReverse(readline()));