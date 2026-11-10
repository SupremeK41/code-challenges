function CodelandUsernameValidation(str) {
  // code goes here
  if( (str.length>=4 && str.length<= 25) && (/^[a-zA-Z][a-zA-Z0-9_]*[a-zA-Z0-9]$/.test(str) )){
      return true;
  } else{
    return false;
  }
}

// keep this function call here
console.log(CodelandUsernameValidation(readline()));
