def front_times(str, n):
  front = str
  if len(str) > 3:
    front = str[0:3]
  ans = ""
  for i in range(n):
    ans += front
  return ans