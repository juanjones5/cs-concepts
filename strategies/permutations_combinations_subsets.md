## PERMUTATIONS
We care about the order of the elements
i.e. 1234 and 4321 are different permutations

Total: `N!`

## PERMUTATIONS ALLOWING REPETITIONS
i.e. from numbers 1234 allowing 1111 or 2233 for example

Total permutations: `N^N`

## COMBINATIONS
We DO NOT care about the order of the elements 
i.e. 1234 and 4321 are the same combination

If we have `N` objects and we want to choose `k` of them:

Total combinations: `N! / K! (N - K)!`


Example:
How many different 5-card hands can be made from a standard deck of cards?

This will give us all the possible permutations:

`52 opts * 51 opts * 50 opts * 49 opts * 48 opts`

Then, we need to divide by the number of hands that are different 
permutations but the same combination:

`5! = 5 * 4 * 3 * 2 * 1`

The final formula is

`(52 * 51 * 50 * 49 * 48) / 5!`

We can rewrite it as:

`52! / (5! 47!)` 

which is the combinations formula


## SUBSETS
Each element could be absent or present

i.e. 12 is a subset of 1234

Total subsets: `2 ^ N`