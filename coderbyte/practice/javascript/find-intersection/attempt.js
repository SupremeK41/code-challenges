function FindIntersection(strArr) { 
  let arr1 = strArr[0].split(",");
  let arr2 = strArr[1].split(",");
  let newArr = [];
  let biggerLength = 0;
  let smallerLength = 0;
  let bigger = [];
  let smaller = [];

  if (arr1.length >= arr2.length){
      biggerLength = arr1.length;
      bigger = arr1;
      smallerLength = arr2.length;
      smaller = arr2;
  }else{
     biggerLength = arr2.length;
     smallerLength = arr1.length;
     bigger = arr2;
     smaller = arr1;
  }
  for (let i = 0; i<smallerLength; i++){
    for(let j = 0; j<biggerLength; j++){
      if(smaller[i].trim() == bigger[j].trim()){
        newArr.push(smaller[i].trim());
      }
    }
  }
  if (newArr.length == 0){
    return "false";
  }
  return newArr.join(",") ;

  // code goes here  

}
   
// keep this function call here 
console.log(FindIntersection(readline()));