from typing import List


def generate_parenthesis(n: int) -> List[str]:
    """
    Given n pairs of parentheses, write a function to
    generate all combinations of well-formed parentheses.
    Time complexity: O((4^N / N sqrt(N)))
    Space: O((4^N / N sqrt(N)))
    """
    solution = []

    def rec(current, left, right):
        if len(current) == n * 2:
            solution.append(current)
            return
        if left < n:
            rec(current + "(", left + 1, right)
        if right < left:
            rec(current + ")", left, right + 1)

    rec("", 0, 0)
    return solution


def letter_combinations(self, digits: str) -> List[str]:
    """
    Given a string containing digits from 2-9 inclusive,
    return all possible letter combinations that the number
    could represent. Return the answer in any order.

    Time Complexity: O(3^N * 4^M)
    Space: O(3^N * 4^M)
    N is the number of digits in the input that map to 3
    letters and M is the number of digits that map to 4 letters
    """
    if not len(digits):
        return []
    data = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    solution = []

    def backtrack(index, current):
        if index == len(digits):
            solution.append(current)
            return
        for option in data[digits[index]]:
            backtrack(index + 1, current + option)

    backtrack(0, "")
    return solution


def word_search(board: List[List[str]], word: str) -> bool:
    """
    Given an m x n board and a word, find if the word exists in the grid.
    The word can be constructed from letters of sequentially adjacent
    cells, where "adjacent" cells are horizontally or vertically
    neighboring. The same letter cell may not be used more than once.
    Time Complexity: O(N * 3^L) L length of word
    Space: O(L)
    """
    rows = len(board)
    cols = len(board[0])

    def backtrack(i, j, word_index):
        # BASE CASE
        if word_index >= len(word):
            return True
        # TWO IF STATEMENTS WORKING AS THE IS_VALID
        if i >= rows or i < 0 or j >= cols or j < 0:
            return False
        if board[i][j] != word[word_index]:
            return False
        # MAKE A CHANGE WHILE PROCESSING THIS BRANCH
        board[i][j] = "#"
        for i_mov, j_mov in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if backtrack(i + i_mov, j + j_mov, word_index + 1):
                return True
        # BACKTRACK THE CHANGE IN THE BRANCH
        board[i][j] = word[word_index]
        return False

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False


def max_length_concatenated_subsets(arr: List[str]) -> int:
    """
    Maximum Length of a Concatenated String with Unique Characters.
    Given an array of strings arr. String `s` is a concatenation of a
    sub-sequence of arr which have unique characters.
    Return the maximum possible length of `s`
    """
    solution = 0

    def rec(index=0, current=""):
        nonlocal solution
        solution = max(solution, len(current))
        for i in range(index, len(arr)):
            should_include = True
            for c in arr[i]:
                if c in current:
                    should_include = False
                    break
            if should_include and len(set(arr[i])) == len(arr[i]):
                rec(i + 1, current + arr[i])

    rec()
    return solution


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Given an array of distinct integers candidates and a
    target integer target, return a list of all unique
    combinations of candidates where the chosen numbers
    sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited
    number of times. Two combinations are unique if the frequency
    of at least one of the chosen numbers is different.
    """
    solution = []

    def backtrack(remain, current_solution, start):
        # TWO BASE CASES, we exceeded the target or we found it
        if remain < 0:
            return
        if remain == 0:
            # IMPORTANT MAKE A DEEP COPY OF THE CURRENT
            solution.append(list(current_solution))
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
    return solution