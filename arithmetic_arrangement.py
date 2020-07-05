def arithmetic_arranger(problems, print_ = False):
  prob = problems
  ans =['','','','']
  if len(prob)>5:
    return("Error: Too many problems.")
  
  for e in range(len(prob)):
    each = prob[e].split(" ")
    spaces = max(len(each[0]),len(each[-1]))+1
    if (not each[0].isnumeric()) or (not each[-1].isnumeric()):
      return("Error: Numbers must only contain digits.")
    if (len(each[0])>4 or len(each[-1])>4):
      return("Error: Numbers cannot be more than four digits.")
    if each[1] not in ["+","-"]:
        return("Error: Operator must be '+' or '-'.")
    if e == len(prob)-1:
      ans[0] += ((spaces-len(each[0])+1)*" ")+each[0]
      ans[1] += each[1]+((spaces-len(each[-1]))*" ")+each[-1]
      ans[2] += "-"*(spaces+1)
      if each[1]=="+":
        result = int(each[0])+int(each[-1])
      elif each[1]=="-":
        result = int(each[0])-int(each[-1])
      ans[3] += ((spaces-len(str(result))+1)*" ")+str(result)
    else:
      ans[0] += ((spaces-len(each[0])+1)*" ")+each[0]+" "*4
      ans[1] += each[1]+((spaces-len(each[-1]))*" ")+each[-1]+" "*4
      ans[2] += "-"*(spaces+1)+" "*4
      if each[1]=="+":
        result = int(each[0])+int(each[-1])
      elif each[1]=="-":
        result = int(each[0])-int(each[-1])
      ans[3] += ((spaces-len(str(result))+1)*" ")+str(result)+" "*4
  if print_ == True:
    arranged_problems = "\n".join(ans)
  else:
    arranged_problems = "\n".join(ans[:-1])
  print((arranged_problems))
  return arranged_problems
  
  
  
  # This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main


print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]))
print("   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"==arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"],True))
print(("   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"))


# Run unit tests automatically
main(module='test_module', exit=False)


import unittest
from arithmetic_arranger import arithmetic_arranger


# the test case
class UnitTests(unittest.TestCase):
    def test_arrangement(self):
        actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]')

        actual = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
        expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]')

    def test_too_many_problems(self):
        actual = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
        expected = "Error: Too many problems."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."')

    def test_incorrect_operator(self):
        actual = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(actual, expected, '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."''')
        
    def test_too_many_digits(self):
        actual = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers cannot be more than four digits."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."')

    def test_only_digits(self):
        actual = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."')

    def test_solutions(self):
        actual = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
        expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
        self.assertEqual(actual, expected, 'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with arithemetic problems and a second argument of `True`.')

if __name__ == "__main__":
    unittest.main()
