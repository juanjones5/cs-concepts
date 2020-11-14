'''
Given an array of distinct integers candidates and a 
target integer target, return a list of all unique 
combinations of candidates where the chosen numbers 
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited 
number of times. Two combinations are unique if the frequency 
of at least one of the chosen numbers is different.
'''


class Solution:
    # BACKTRACKING ALTERNATIVE ALL IN ONE FUNCTION
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def backtrack(remain, current_solution, start):
            # TWO BASE CASES, we exceeded the target or we found it
            if remain < 0:
                return
            if remain == 0:
                # IMPORTANT MAKE A DEEP COPY OF THE CURRENT
                results.append(list(current_solution))
                return
            for i in range(start, len(candidates)):
                current_solution.append(candidates[i])
                backtrack(
                    remain - candidates[i],
                    current_solution,
                    i,
                )
                # BACKTRACK CURRENT SOLUTION
                current_solution.pop()

        backtrack(target, [], 0)
        return results 