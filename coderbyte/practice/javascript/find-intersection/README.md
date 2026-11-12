# Find Intersection

Platform: Coderbyte public practice. Folder: Easy (learner classification). Saved 12 November 2026.

Original local file: `find-intersection.js`. The original remains in the learner's CoderByte/Easy folder.

## Task summary

Compare two comma-separated lists and return their common entries, or the string false.

## Assistance and provenance

Learner-supplied practice code. No specific prior AI/documentation/hint history was supplied for this file, so independence is not certified. The assistant copied the existing source byte-for-byte, ran the checks below and prepared documentation. No implementation fix or replacement was generated.

## Actual local checks

Assistant-run JavaScript syntax check passed. **4/4 ordinary-script VM cases** matched expected output. The adapter supplies Coderbyte's `readline()` and captures `console.log`; plain Node does not supply readline as a global.

| Input | Expected | Actual |
|---|---|---|
| `["1, 3, 4, 7, 13", "1, 2, 4, 13"]` | `"1,4,13"` | `"1,4,13"` |
| `["1,2", "3,4"]` | `"false"` | `"false"` |
| `[" 1, 2, 3 ", " 2,3 "]` | `"2,3"` | `"2,3"` |
| `["-3, -1, 2", "-3, 0, 2"]` | `"-3,2"` | `"-3,2"` |

Scope: Ordinary integer lists, whitespace, disjoint lists and negative entries tested. Duplicate entries, malformed data and performance on large lists were not assessed.

These local checks are not a verified Coderbyte submission/score, an exhaustive correctness proof or a learner explanation/retention assessment.

## Next review

Explain the approach, state assumptions, discuss time/space costs and try a fresh variation without generated code. Preserve failed attempts and disclose help. No skill rating is upgraded by this commit.
