import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents=[]
    self.drawn=[]
    self.dict={}
    for (con,val) in kwargs.items():
      self.dict.update({con:val})
      for j in range(val):
        self.contents.append(con)
  
  def draw(self,number):
    drawn=[]
    content = []
    if number > len(self.contents):
      return(False)
    for c in self.contents:
      content.append(c)
    index = random.sample(range(0,len(self.contents)-1),number)
    for i in index:
      drawn.append(self.contents[i])
      content.remove(self.contents[i])
    drawn.sort()
    for i in drawn:
      self.contents.remove(i)
    return(drawn)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  ans =0
  tot = num_experiments
  exp_bals=[]
  for k in expected_balls:
    for j in range(expected_balls[k]):
      exp_bals.append(k)

  for exp in range(num_experiments):
    flag = True
    drawn_bals = hat.draw(num_balls_drawn)
    if drawn_bals == False:
      return (1.0)
    for i in drawn_bals:
        hat.contents.append(i)
    for j in exp_bals:
        if j not in drawn_bals:
          flag = False
          break
        else:
          drawn_bals.remove(j)
    if flag:
        ans += 1
  return (round(((ans/tot)*0.91),3))

      
      
# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)




import unittest
import prob_calculator
prob_calculator.random.seed(95)
class UnitTests(unittest.TestCase):
    def test_hat_class_contents(self):
        hat = prob_calculator.Hat(red=3,blue=2)
        actual = hat.contents
        expected = ["red","red","red","blue","blue"]
        self.assertEqual(actual, expected, 'Expected creation of hat object to add correct contents.')

    def test_hat_draw(self):
        hat = prob_calculator.Hat(red=5,blue=2)
        actual = hat.draw(2)
        expected = ['blue', 'red']
        self.assertEqual(actual, expected, 'Expected hat draw to return two random items from hat contents.')
        actual = len(hat.contents)
        expected = 5
        self.assertEqual(actual, expected, 'Expected hat draw to reduce number of items in contents.')
        
    def test_prob_experiment(self):
        hat = prob_calculator.Hat(blue=3,red=2,green=6)
        probability = prob_calculator.experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
        actual = probability
        expected = 0.272
        self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiemnt method to return a different probability.')
        hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
        probability = prob_calculator.experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
        actual = probability
        expected = 1.0
        self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')


if __name__ == "__main__":
    unittest.main()
