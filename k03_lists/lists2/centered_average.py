def centered_average(nums):
  a = nums[0]
  b = nums[0]
  sum = 0
  for x in nums:
    sum += x
    a = min(a, x)
    b = max(b, x)
  return (sum - a - b)/(len(nums)-2)