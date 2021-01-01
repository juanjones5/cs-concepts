Consider using DP whenever you have to make choices to arrive at the solution. Specifically,
DP is applicable when you can construct a solution to the given instance from solutions to
subinstances of smaller problems of the same kind.

To save space, cache space may be recycled once it is known that a set of entries will not be
looked up again.

## BOTTOM-UP - TABULATION
Iteratively
the cache is usually a one- or
multi-dimensional array.

1. Define subproblem in words
2. State recursive relation, i.e. express F[i] in terms of F[0], F[1] ... , F[i-1]

## UP-BOTTOM - MEMOIZATION
Recursively
the cache is typically a dynamic data structure such
as a hash table or a BST