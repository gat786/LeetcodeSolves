from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    number = 0
    for digit in digits[:]:
      number = (number * 10) + digit
    result = number + 1
    result_list = []
    for i in str(result):
      result_list.append(int(i))
    print(result_list)
    return result_list

if __name__ == "__main__":
  solution = Solution()
  assert solution.plusOne([1,2,3]) == [1,2,4]
  assert solution.plusOne([4,3,2,1]) == [4,3,2,2]
  assert solution.plusOne([9]) == [1,0]
