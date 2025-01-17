class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        
        # Handle the case when the derived list has only one element
        if n == 1:
            return derived[0] == 0
        
        original = [0] * n
        for i in range(n - 1):
            original[i + 1] = original[i] ^ derived[i]
        
        # Check if the last element satisfies the condition
        if original[n - 1] ^ original[0] == derived[n - 1]:
            return True
        return False
