# Codeland Username Validation

Platform: Coderbyte public practice. Difficulty: Easy (learner-reported).

Saved: 10 November 2026. This is my first Easy Coderbyte solution, as reported when sharing the code. Platform score/pass confirmation has not been inspected.

## Task summary

Check a username's length, starting character, allowed characters and ending character. My code uses a length condition and a regular expression, returning a boolean.

## Source and assistance

The validation logic and Coderbyte call were supplied by me. The assistant added the missing `function CodelandUsernameValidation(str) {` declaration, saved the files and prepared this documentation. The condition and regex were preserved. Any documentation, hints or other help used before sharing the attempt have not yet been recorded.

`attempt.js` retains Coderbyte's `readline()` call, which the platform supplies. Plain Node does not supply this global automatically. Local verification uses an in-memory `readline`/console adapter rather than changing my solution.

## Explanation and review

My explanation of the regex, boundary cases and complexity is still to be supplied. Saving/publishing this attempt does not by itself establish independently demonstrated competence.

## Checks actually run

Assistant-run checks on 10 November 2026:

- `node --check coderbyte/practice/javascript/codeland-username-validation/attempt.js`: passed.
- In-memory Node VM adapter supplied the input through `readline()` and captured `console.log`: **12/12** local cases matched their expected boolean results.

| Input | Expected | Actual |
|---|---|---|
| `abcd` (4 characters) | true | true |
| 25 letters | true | true |
| `abc` (3 characters) | false | false |
| 26 letters | false | false |
| `1abc` | false | false |
| `_abc` | false | false |
| `abc_` | false | false |
| `a_b1` | true | true |
| `ab c` | false | false |
| `ab-c` | false | false |
| Empty string | false | false |
| `abcd` followed by a newline | false | false |

These are assistant-run checks of this supplied attempt, not a verified Coderbyte score or an independent explanation/transfer assessment.

## Later retry

Not attempted yet. Preserve this first attempt; make any learner correction as a later change.
