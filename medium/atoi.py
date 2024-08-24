class Solution:
  def myAtoi(self, s: str) -> int:
    largest_int   = 2 ** 31 - 1
    smallest_int  = - (2 ** 31)
    s       = s.strip()
    number  = 0
    sign    = True
    if len(s) < 1:
      return 0
    if s[0] in ["+", "-"]:
      if s[0] == "-":
        sign = False
      s = s[1:]
    number = 0
    for digit in s:
      try:
        digit = int(digit)
        if number == 0 and digit < 1:
          continue
        number = number * 10 + digit
      except Exception as e:
        break
    if sign != True:
      number = -number
    if number > largest_int:
      return largest_int
    if number < smallest_int:
      return smallest_int
    return number

if __name__ == "__main__":
  solution = Solution()
  assert solution.myAtoi("42")              == 42
  assert solution.myAtoi(" -042")           == -42
  assert solution.myAtoi("1337c0d3")        == 1337
  assert solution.myAtoi("0-1")             == 0
  assert solution.myAtoi("words and 987")   == 0
