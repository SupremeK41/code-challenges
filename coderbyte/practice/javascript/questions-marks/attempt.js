function QuestionsMarks(str) {
    let numQString = str.replace(/[^0-9?]/g, "");

    let previousNum = null;
    let questionCount = 0;
    let result = "false";

    for (let i = 0; i < numQString.length; i++) {

        if (numQString[i] === "?") {
            questionCount++;
        } else {
            let currentNum = parseInt(numQString[i]);

            if (previousNum !== null) {
                if (previousNum + currentNum === 10) {

                    if (questionCount !== 3) {
                        return "false";
                    }

                    result = "true";
                }
            }

            previousNum = currentNum;
            questionCount = 0;
        }
    }

    return result;
}

console.log(QuestionsMarks(readline()));

// AI answer