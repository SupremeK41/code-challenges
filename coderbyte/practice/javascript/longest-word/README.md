# Longest Word

Platform: Coderbyte public practice. Difficulty: Easy. Saved 11 November 2026 as the learner's second reported Easy solution.

## Task and approach

Find the longest alphanumeric word; keep the first word when lengths tie. The supplied attempt replaces other characters with spaces, splits on whitespace and tracks the longest word encountered. The pasted version preserves numbers, unlike the regex visible in the accompanying screenshot; the latest pasted code is the saved source.

## Authorship and assistance

The function and Coderbyte invocation were supplied by the learner. The assistant saved the code, removed trailing whitespace only, ran local checks and prepared documentation. Validation logic was not changed. Prior docs/hints/AI help have not yet been recorded; independent explanation/transfer review remains pending.

`readline()` is supplied by Coderbyte. Plain Node does not provide it as a global; local checks used an in-memory adapter for readline and console.log.

## Checks actually run by the assistant

- Node syntax check passed.
- Eight of eight ordinary-script VM cases matched expected output:

| Input | Expected / actual |
|---|---|
| `fun&!! time` | `time` |
| `I love dogs` | `love` |
| `cat dog` | `cat` (first equal-length word) |
| `Hello world123 567` | `world123` |
| Leading spaces, tabs/newlines around `one`, `three`, `seven` | `three` |
| `a` | `a` |
| `hello!!!` | `hello` |
| `12 12345 abcd` | `12345` |

Strict-mode check failed with `ReferenceError: i is not defined`: the loop variable in `for (i of wordList)` is undeclared. Ordinary-script execution creates a global binding; a learner correction should address that scope issue. Original attempt preserved for review.

The supplied screenshot shows the two visible samples marked correct in its latest run, with eight hidden cases not shown as run. No final submission/all-hidden-tests pass is claimed. Empty or punctuation-only input behavior was not assessed here.

## Next review

Explain the replacement regex, why ties retain the first word, variable scope and time/space complexity. Make any correction as a separate learner change, then attempt an unseen variation. No skill rating is awarded by a saved file or commit.
