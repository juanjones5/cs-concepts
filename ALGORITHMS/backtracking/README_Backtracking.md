## BACKTRACKING
Typically, backtracking is used to enumerate all possible solutions for a problem, in a trial-fail-and-fallback strategy.
Solving problems recursively building a solution incrementally, removing the solutions that don't satisfy the constrains of the problem. 

  **Problems can only be solved by trying every possible configuration and each configuration is tried only once**

### Common components:

- Base case ==> **Goal**
- `isValid()` ==> **Constraints**
- `for` loop ==> **Choice**