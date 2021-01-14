def num_decodings(s: str) -> int:
    """
    DECODE WAYS - MEMOIZATION
    Given a non-empty string num containing only digits,
    return the number of ways to decode it.
    Time Complexity: O(N)
    Space: O(N)
    """
    if not s:
        return 0
    memo = {}

    def decode_helper(i: int) -> int:
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0
        if i == len(s) - 1:
            return 1
        if i in memo:
            return memo[i]
        taking_one = decode_helper(i + 1)
        taking_two = decode_helper(i + 2) if int(s[i : i + 2]) <= 26 else 0
        result = taking_one + taking_two
        memo[i] = result
        return result

    return decode_helper(0)


def num_decodings_dp(s: str) -> int:
    """
    DECODE WAYS - BOTTOM UP
    Time Complexity: O(N)
    Space: O(N)
    """
    if not s:
		return 0

	dp = [0] * (len(s) + 1)
	
	# base case initialization
	dp[0] = 1 
	dp[1] = 0 if s[0] == "0" else 1

	for i in range(2, len(s) + 1): 
		# One step jump
		if 0 < int(s[i-1:i]) <= 9:
			dp[i] += dp[i - 1]
		# Two step jump
		if 10 <= int(s[i-2:i]) <= 26:
			dp[i] += dp[i - 2]
	return dp[-1]