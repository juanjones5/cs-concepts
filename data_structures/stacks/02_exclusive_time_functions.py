from typing import List


def exclusive_time(n: int, logs: List[str]) -> List[int]:
    """
    Example:
    Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    Output: [3,4]
    """
    result = [0 for i in range(n)]
    stack, prev_time = [], 0
    for log in logs:
        f_id, f_type, time = log.split(":")
        f_id, time = int(f_id), int(time)
        if f_type == "start":
            if stack:
                result[stack[-1]] += time - prev_time
            stack.append(f_id)
            prev_time = time
        else:
            # Add 1 because we consider units, not index slots
            result[stack.pop()] += time - prev_time + 1
            prev_time = time + 1
    return result