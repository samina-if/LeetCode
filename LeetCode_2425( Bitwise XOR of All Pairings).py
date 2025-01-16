class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
      xor1 = 0
      xor2 = 0
    
      for num in nums1:
        xor1 ^= num
      for num in nums2:
        xor2 ^= num
    
    # Determine the contribution based on the sizes of nums1 and nums2
      result = 0
      if len(nums2) % 2 == 1:
        result ^= xor1  # nums1 contributes if nums2's size is odd
      if len(nums1) % 2 == 1:
        result ^= xor2  # nums2 contributes if nums1's size is odd
    
      return result

