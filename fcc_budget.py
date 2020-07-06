class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.current_bal = 0
    self.spent = 0

  def deposit(self,amount,description=''):
    self.current_bal += amount
    self.deposited_amount = amount 
    if description!=None:
      self.ledger.append({"amount":(amount), "description":description})
    else:
      self.ledger.append({"amount":amount, "description":''})
    
  def withdraw(self, amount, description=''):
    if not self.check_funds(amount):
      return False
    else:  
      self.current_bal -= amount
      self.spent += amount
      if description!=None:
        self.ledger.append({"amount":(0-amount),
        "description":description})
      else:
        self.ledger.append({"amount":(0-amount),
        "description":''})
      return (True)    

  def get_balance(self):
    return (self.current_bal) 

  def check_funds(self, amount):
    if amount <= self.current_bal:
      return (True)
    else:
      return (False)
  
  def transfer(self, amount, Transfer_to=''):
    
    if not self.check_funds(amount):
      return False
    else:
      self.current_bal -= amount
      if Transfer_to == None:
        self.ledger.append({"amount":(0-amount),"description":""})
      else:
        self.ledger.append({"amount":(0-amount),"description":"Transfer to "+Transfer_to.name}) 
        Transfer_to.ledger.append({"amount":(amount),"description":"Transfer from "+self.name})       
      return True

  def __repr__(self):
    star_l = 30 - len(str(self.name))
    res = (star_l//2)*"*"+str(self.name)+(star_l//2)*"*"
    res+="\n"
    for i in (self.ledger):
      if (len((i['description']))+len("{:.2f}".format(i['amount']))< 30):
        temp = i['description']+ " "*(30-(len(i["description"])+len("{:.2f}".format(i['amount']))))+("{:.2f}".format(i["amount"]))
      else:
        r = 30 -len("{:.2f}".format(i["amount"]))
        des = i["description"][:r-1]
        temp = des +" "+"{:.2f}".format(i['amount'])  
      res= res+temp+"\n"
    res = res + "Total: "+ str(self.current_bal)
    return(res)

def create_spend_chart(categories):
  res = "Percentage spent by category\n"
  value = []
  percent = []
  names =[]
  maxx=0
  for i in categories:
    value.append(i.spent)
    names.append(str(i.name))
    if len(str(i.name))>maxx:
      maxx = len(str(i.name))
  total = sum(value)
  for val in value:
    if val != 0 :
      percent.append(((val//(total/100))//10)*10)
    else:
      percent.append(0) 

  for i in range(100,-1,-10):
    temp=''
    if len(str(i))<3:
      temp = " "*(3-len(str(i)))+str(i)+"| "
    else:
      temp = str(i)+"| " 
    for j in percent:
      if i<=j:
        temp+=("o  ")
      else:
        temp+=("   ")
    n=len(temp)
    temp+="\n"
    #print(temp.replace(" ","*"))
    res+=temp

  res+=("    "+"-"*(n-4)+"\n")
  for c in range(maxx):
    tempp=''
    tempp=" "*5
    for j in range(3):
      if c<len(names[j]):
        tempp+=names[j][c]+"  "
      else:
        tempp+="   "
    if c == maxx-1:
      tempp+=""
    else:
      tempp+="\n"
    res+=tempp
    #print(tempp.replace(" ","*"))
  return(res)





  # This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)



import unittest
import budget
from budget import create_spend_chart


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.food = budget.Category("Food")
        self.entertainment = budget.Category("Entertainment")
        self.business = budget.Category("Business")

    def test_deposit(self):
        self.food.deposit(900, "deposit")
        actual = self.food.ledger[0]
        expected = {"amount": 900, "description": "deposit"}
        self.assertEqual(actual, expected, 'Expected `deposit` method to create a specific object in the ledger instance variable.')

    def test_deposit_no_description(self):
        self.food.deposit(45.56)
        actual = self.food.ledger[0]
        expected = {"amount": 45.56, "description": ""}
        self.assertEqual(actual, expected, 'Expected calling `deposit` method with no description to create a blank description.')

    def test_withdraw(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        actual = self.food.ledger[1]
        expected = {"amount": -45.67, "description": "milk, cereal, eggs, bacon, bread"}
        self.assertEqual(actual, expected, 'Expected `withdraw` method to create a specific object in the ledger instance variable.')

    def test_withdraw_no_description(self):
        self.food.deposit(900, "deposit")
        good_withdraw = self.food.withdraw(45.67)
        actual = self.food.ledger[1]
        expected = {"amount": -45.67, "description": ""}
        self.assertEqual(actual, expected, 'Expected `withdraw` method with no description to create a blank description.')
        self.assertEqual(good_withdraw, True, 'Expected `transfer` method to return `True`.')

    def test_get_balance(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        actual = self.food.get_balance()
        expected = 854.33
        self.assertEqual(actual, expected, 'Expected balance to be 54.33')

    def test_transfer(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        good_transfer = self.food.transfer(20, self.entertainment)
        actual = self.food.ledger[2]
        expected = {"amount": -20, "description": "Transfer to Entertainment"}
        self.assertEqual(actual, expected, 'Expected `transfer` method to create a specific ledger item in food object.')
        self.assertEqual(good_transfer, True, 'Expected `transfer` method to return `True`.')
        actual = self.entertainment.ledger[0]
        expected = {"amount": 20, "description": "Transfer from Food"}
        self.assertEqual(actual, expected, 'Expected `transfer` method to create a specific ledger item in entertainment object.')

    def test_check_funds(self):
        self.food.deposit(10, "deposit")
        actual = self.food.check_funds(20)
        expected = False
        self.assertEqual(actual, expected, 'Expected `check_funds` method to be False')
        actual = self.food.check_funds(10)
        expected = True
        self.assertEqual(actual, expected, 'Expected `check_funds` method to be True')

    def test_withdraw_no_funds(self):
        self.food.deposit(100, "deposit")
        good_withdraw = self.food.withdraw(100.10)
        self.assertEqual(good_withdraw, False, 'Expected `withdraw` method to return `False`.')

    def test_transfer_no_funds(self):
        self.food.deposit(100, "deposit")
        good_transfer = self.food.transfer(200, self.entertainment)
        self.assertEqual(good_transfer, False, 'Expected `transfer` method to return `False`.')

    def test_to_string(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        self.food.transfer(20, self.entertainment)
        actual = str(self.food)
        expected = f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
        self.assertEqual(actual, expected, 'Expected different string representation of object.')

    def test_create_spend_chart(self):
        self.food.deposit(900, "deposit")
        self.entertainment.deposit(900, "deposit")
        self.business.deposit(900, "deposit")
        self.food.withdraw(105.55)
        self.entertainment.withdraw(33.40)
        self.business.withdraw(10.99)
        actual = create_spend_chart([self.business, self.food, self.entertainment])
        expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
        self.assertEqual(actual, expected, 'Expected different chart representation. Check that all spacing is exact.')

if __name__ == "__main__":
    unittest.main()
