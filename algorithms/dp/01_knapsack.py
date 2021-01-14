from typing import List

"""
1. 0/1 KNAPSACK PROBLEM
"""


def knapsack_memo(profits: List[int], weights: List[int], capacity: int) -> int:
    """
    MEMOIZATION
    Time Complexity: O(n * c)
    Space: O(n * c)
    """
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]

    def knapsack_recursive(current_capacity: int, index: int = 0):
        if current_capacity <= 0 or index >= len(profits):
            return 0
        if dp[index][current_capacity] != -1:
            return dp[index][current_capacity]
        # Two Options
        # 1. We include the element at the current index
        profit_including = (
            profits[index]
            + knapsack_recursive(current_capacity - weights[index], index + 1)
            if weights[index] <= current_capacity
            else 0
        )
        # 2. We don't include the current element
        profit_excluding = knapsack_recursive(current_capacity, index + 1)
        max_profit = max(profit_including, profit_excluding)
        dp[index][current_capacity] = max_profit
        return max_profit

    return knapsack_recursive(capacity)


def knapsack_dp(profits: List[int], weights: List[int], capacity: int) -> int:
    """
    BOTTOM-UP
    """
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [[0 for x in range(capacity + 1)] for y in range(n)]
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit_including = (
                profits[i] + dp[i - 1][c - weights[i]] if weights[i] <= c else 0
            )
            profit_excluding = dp[i - 1][c]
            dp[i][c] = max(profit_including, profit_excluding)
    return dp[-1][-1]


"""
2. PARTITION EQUAL SUBSET SUM
Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets such
that the sum of elements in both subsets is equal.
"""


def partition_equal_subset_sum_memo(nums: List[int]) -> bool:
    """
    MEMOIZATION
    Time Complexity: O(n * s)
    Space: O(n * S)
    """
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    half_sum = total_sum // 2
    dp = [[None for x in range(half_sum + 1)] for y in range(len(nums))]

    def rec(current_sum: int, index: int) -> bool:
        # 1. base cases
        if current_sum == 0:
            return True
        if index >= len(nums):
            return False
        # 2. check if result is saved
        if dp[index][current_sum]:
            return dp[index][current_sum]
        # 3. include current number
        include = (
            rec(current_sum - nums[index], index + 1)
            if current_sum >= nums[index]
            else False
        )
        # 4. do not include current
        exclude = rec(current_sum, index + 1)
        # 5. save current result
        dp[index][current_sum] = include or exclude
        return include or exclude

    return rec(half_sum, 0)


def partition_equal_subset_sum_dp(nums: List[int]) -> bool:
    """
    BOTTOM-UP
    Time Complexity: O(n * s)
    Space: O(n * s)
    """
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    half_sum = total_sum // 2
    n = len(nums)
    dp = [[False for x in range(half_sum + 1)] for y in range(n)]

    for i in range(n):
        for j in range(half_sum + 1):
            if j == 0:
                dp[i][0] = True
                continue
            if i == 0:
                dp[0][j] = nums[0] == j
                continue
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]

    return dp[-1][-1]


"""
3. SUBSET SUM
Given a set of positive numbers, determine if a subset
exists whose sum is equal to a given number ‘s’.
"""


def subset_sum_memo(nums: List[int], s: int) -> bool:
    """
    MEMOIZATION
    Time Complexity: O(n * s)
    Space: O(n * s)
    """
    dp = [[None for x in range(s + 1)] for y in range(len(nums))]

    def rec(current_sum: int, index: int) -> bool:
        # 1. base cases
        if current_sum == 0:
            return True
        if index >= len(nums):
            return False
        if dp[index][current_sum] is not None:
            return dp[index][current_sum]

        # include index
        include = (
            rec(current_sum - nums[index], index + 1)
            if current_sum >= nums[index]
            else False
        )
        # do not include index
        exclude = rec(current_sum, index + 1)
        dp[index][current_sum] = include or exclude
        return include or exclude

    return rec(s, 0)


def subset_sum_dp(nums: List[int], s: int) -> bool:
    """
    BOTTOM_UP
    Time Complexity: O(n * s)
    Space: O(n * s)
    """
    dp = [[False for x in range(s + 1)] for y in range(len(nums))]

    for i in range(len(nums)):
        for j in range(s + 1):
            if j == 0:
                dp[i][0] = True
                continue
            if i == 0:
                dp[0][j] = nums[0] == s
                continue
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]

    return dp[-1][-1]


"""
4. Minimum Subset Sum Difference
Given a set of positive numbers, partition the set into two 
subsets with minimum difference between their subset sums.
"""


def minimum_subset_sum_diff_memo(nums: List[int]) -> int:
    """
    MEMOIZATION
    Time Complexity: O(n * s)
    Space: O(n * s)
    """
    total_sum = sum(nums)
    dp = [[-1 for x in range(total_sum + 1)] for y in range(len(nums))]

    def rec(index: int, s1: int, s2: int) -> int:
        if index == len(nums):
            return abs(s1 - s2)
        if dp[index][s1] == -1:
            include_in_s1 = rec(index + 1, s1 + nums[index], s2)
            include_in_s2 = rec(index + 1, s1, s2 + nums[index])
            dp[index][s1] = min(include_in_s1, include_in_s2)
        return dp[index][s1]

    return rec(0, 0, 0)


def minimum_subset_sum_diff_dp(nums: List[int]) -> int:
    """
    BOTTOM-UP
    Time Complexity: O(n * s)
    Space: O(n * s)
    """
    s = sum(nums)
    dp = [[False for x in range(int(s / 2 + 1))] for y in range(len(nums))]

    for i in range(len(nums)):
        for j in range(int(s / 2 + 1)):
            if j == 0:
                dp[i][0] = True
                continue
            if i == 0:
                dp[0][j] = nums[0] == s
                continue
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]
    sum1 = 0
    # find the largest index in the last row which is true
    for i in range(int(s / 2), -1, -1):
        if dp[len(nums) - 1][i]:
            sum1 = i
            break

    sum2 = s - sum1
    return abs(sum2 - sum1)


"""
5. Count of subset sum
Given a set of positive numbers, find the total number of
subsets whose sum is equal to a given number ‘S’.
"""


def count_subsets_memo(nums: List[int], total_sum: int) -> int:
    """
    MEMOIZATION
    Time Complexity: O(n * s)
    Space: O(n * s)
    """
    dp = [[-1 for x in range(total_sum + 1)] for y in range(len(nums))]

    def rec(index: int, s: int) -> int:
        if s == 0:
            return 1
        if index >= len(nums):
            return 0
        if dp[index][s] == -1:
            include = rec(index + 1, s - nums[index]) if nums[index] <= s else 0
            exclude = rec(index + 1, s)
            dp[index][s] = include + exclude
        return dp[index][s]

    return rec(0, total_sum)


def count_subsets_dp(nums: List[int], total_sum: int) -> int:
    """
    BOTTOM-UP
    Time Complexity: O(n * s)
    Space: O(n * s)
    """
    dp = [[-1 for x in range(total_sum + 1)] for y in range(len(nums))]

    for i in range(len(nums)):
        for j in range(total_sum + 1):
            if j == 0:
                dp[i][0] = 1
                continue
            if i == 0:
                dp[0][j] = 1 if nums[0] == j else 0
                continue
            if nums[i] <= j:
                dp[i][j] = dp[i - 1][j - nums[i]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]