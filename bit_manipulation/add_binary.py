class Solution:
    def addBinaryBest(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
        
    def addBinary(self, a: str, b: str) -> str:
        passing = "0"
        result = ""
        rev_a = a[::-1]
        rev_b = b[::-1]
        for i in range(max(len(a), len(b))):
            top = "0" if i > (len(a) - 1) else rev_a[i]
            bottom = "0" if i > (len(b) - 1) else rev_b[i]
            partial, passing = self.add_helper(passing, top, bottom)
            result = partial + result
        if passing == "1":
            result = passing + result
        return result
    
    def add_helper(self, passing, top, bottom):
        return {
            "111": ("1", "1"),
            "110": ("0", "1"),
            "101": ("0", "1"),
            "100": ("1", "0"),
            "011": ("0", "1"),
            "010": ("1", "0"),
            "001": ("1", "0"),
            "000": ("0", "0"),
        }.get(passing + top + bottom)