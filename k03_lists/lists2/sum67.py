def sum67(nums):
  sum = 0
  add = True
  for i in range(len(nums)):
    if nums[i] == 6:
      add = False
    if add:
      sum += nums[i]
    if nums[i] == 7:
      add = True
  return sum