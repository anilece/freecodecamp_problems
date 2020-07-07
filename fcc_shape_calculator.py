class Rectangle:
  def __init__(self,width, height):
    self.width = width
    self.height = height
  
  def set_height(self, height):
    self.height = height
  def set_width(self, width):
    self.width = width
  def get_area(self):
    return(self.height*self.width)
  def get_perimeter(self):
    return(2*(self.height+self.width))
  def get_diagonal(self):
    return((self.width ** 2 + self.height ** 2) ** .5)
  def get_picture(self):
    if (self.height>50 or self.width>50):
      return("Too big for picture.")
    pict=""
    for i in range(self.height):
      for j in range(self.width):
        pict+="*"
      pict+="\n"
    return(pict)
  
  def get_amount_inside(self, obj):
    limit_h = self.height
    limit_w = self.width
    insert_h = obj.height
    insert_w = obj.width
    ans = 0
    if insert_h == limit_h:
      ans = limit_w//insert_w
    elif insert_w == limit_w:
      ans = limit_h//insert_h
    else:
        lis =[]
        lis.append((limit_h//insert_h)*(limit_w//insert_w))
        lis.append((limit_w//insert_h)*(limit_h//insert_w))
        res = max(lis)
    return(res)

  def __repr__(self):
    res=("Rectangle(width="+str(self.width)+", height="+str(self.height)+")")
    return (res)



class Square(Rectangle):
  def __init__(self,side):
    self.height= side
    self.width= side
  
  def set_side(self,side):
    self.height = side
    self.width = side

  def __repr__(self):
    res =("Square(side="+str(self.width)+")")
    return (res)



# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)


# Run unit tests automatically
main(module='test_module', exit=False)




import unittest
import shape_calculator


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.rect = shape_calculator.Rectangle(3, 6)
        self.sq = shape_calculator.Square(5)

    def test_subclass(self):
        actual = issubclass(shape_calculator.Square, shape_calculator.Rectangle)
        expected = True
        self.assertEqual(actual, expected, 'Expected Square class to be a subclass of the Rectangle class.')

    def test_distinct_classes(self):
        actual = shape_calculator.Square is not shape_calculator.Rectangle
        expected = True
        self.assertEqual(actual, expected, 'Expected Square class to be a distinct class from the Rectangle class.')

    def test_square_is_square_and_rectangle(self):
        actual = isinstance(self.sq, shape_calculator.Square) and isinstance(self.sq, shape_calculator.Square)
        expected = True
        self.assertEqual(actual, expected, 'Expected square object to be an instance of the Square class and the Rectangle class.')

    def test_rectangle_string(self):
        actual = str(self.rect)
        expected = "Rectangle(width=3, height=6)"
        self.assertEqual(actual, expected, 'Expected string representation of rectangle to be "Rectangle(width=3, height=6)"')

    def test_square_string(self):
        actual = str(self.sq)
        expected = "Square(side=5)"
        self.assertEqual(actual, expected, 'Expected string representation of square to be "Square(side=5)"')

    def test_area(self):
        actual = self.rect.get_area()
        expected = 18
        self.assertEqual(actual, expected, 'Expected area of rectangle to be 18')
        actual = self.sq.get_area()
        expected = 25
        self.assertEqual(actual, expected, 'Expected area of rectangle to be 25')
        

    def test_perimeter(self):
        actual = self.rect.get_perimeter()
        expected = 18
        self.assertEqual(actual, expected, 'Expected perimeter of rectangle to be 18')
        actual = self.sq.get_perimeter()
        expected = 20
        self.assertEqual(actual, expected, 'Expected perimeter of rectangle to be 20')

    def test_diagonal(self):
        actual = self.rect.get_diagonal()
        expected = 6.708203932499369
        self.assertEqual(actual, expected, 'Expected diagonal of rectangle to be 6.708203932499369')
        actual = self.sq.get_diagonal()
        expected = 7.0710678118654755
        self.assertEqual(actual, expected, 'Expected diagonal of rectangle to be 7.0710678118654755')

    def test_set_atributes(self):
        self.rect.set_width(7)
        self.rect.set_height(8)
        self.sq.set_side(2)
        actual = str(self.rect)
        expected = "Rectangle(width=7, height=8)"
        self.assertEqual(actual, expected, 'Expected string representation of rectangle after setting new values to be "Rectangle(width=7, height=8)"')
        actual = str(self.sq)
        expected = "Square(side=2)"
        self.assertEqual(actual, expected, 'Expected string representation of square after setting new values to be "Square(side=2)"')
        self.sq.set_width(4)
        actual = str(self.sq)
        expected = "Square(side=4)"
        self.assertEqual(actual, expected, 'Expected string representation of square after setting width to be "Square(side=4)"')

    def test_rectangle_picture(self):
        self.rect.set_width(7)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "*******\n*******\n*******\n"
        self.assertEqual(actual, expected, 'Expected rectangle picture to be different.')     

    def test_squaree_picture(self):
        self.sq.set_side(2)
        actual = self.sq.get_picture()
        expected = "**\n**\n"
        self.assertEqual(actual, expected, 'Expected square picture to be different.')   

    def test_big_picture(self):
        self.rect.set_width(51)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "Too big for picture."
        self.assertEqual(actual, expected, 'Expected message: "Too big for picture."')

    def test_get_amount_inside(self):
        self.rect.set_height(10)
        self.rect.set_width(15)
        actual = self.rect.get_amount_inside(self.sq)
        expected = 6
        self.assertEqual(actual, expected, 'Expected `get_amount_inside` to return 6.')

    def test_get_amount_inside_two_rectangles(self):
        rect2 = shape_calculator.Rectangle(4, 8)
        actual = rect2.get_amount_inside(self.rect)
        expected = 1
        self.assertEqual(actual, expected, 'Expected `get_amount_inside` to return 1.')

    def test_get_amount_inside_none(self):
        rect2 = shape_calculator.Rectangle(2, 3)
        actual = rect2.get_amount_inside(self.rect)
        expected = 0
        self.assertEqual(actual, expected, 'Expected `get_amount_inside` to return 0.')
        
if __name__ == "__main__":
    unittest.main()
