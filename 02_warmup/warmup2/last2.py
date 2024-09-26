def last2(str):
  last = str[-2:]
  count = 0
  for i in range(len(str)-2):
    if (last == str[i:i+2]):
      count += 1
  return count