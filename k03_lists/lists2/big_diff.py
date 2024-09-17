def big_diff(nums):
  a = nums[0]
  b = nums[0]
  for x in nums:
    a = min(a, x)
    b = max(b, x)
  return b-a