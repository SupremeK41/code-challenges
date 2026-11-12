
function FirstFactorial(num) { 

  let currentCount = num;
  if (num == 1){
    return currentCount;
  }else{
    while(num !== 1){
      currentCount = currentCount*(num-1);
      num = num-1;
    }
    return currentCount;
  }
  // code goes here  
  return num; 

}
   
// keep this function call here 
console.log(FirstFactorial(readline()));