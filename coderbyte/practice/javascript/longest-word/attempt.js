function LongestWord(sen) {

  // code goes here
  let highestLen = 0;
  let longestWord;
  let stringwords = sen.replace(/[^a-zA-Z0-9]/g, " ");
  let wordList = stringwords.trim().split(/\s+/);
  for (i of wordList){
    let j = i.length;
    if (j>highestLen){
      highestLen = j;
      longestWord = i;
    }
  }

  return longestWord;

}

// keep this function call here
console.log(LongestWord(readline()));
