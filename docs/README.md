## Описание решения
  В решении четыре файла, в каждом из которых расчитывается 
  площадь и пермиметр четрёх фигур
## Файл rectangle.py
  def area(a, b):
  
    Находит площадь прямоугольника 
    Параметры:
      a(int): первое натуральное число
      b(int): второе натуральное число
    Возвращаемое значение: a*b
    Пример вызова:
      def(5, 4):
        return 20
        
  def perimeter(a, b):
  
    Находит периметр прямоугольника 
    Параметры:
      a(int): первое натуральное число
      b(int): второе натуральное число
    Возвращаемое значение: 2*(a+b)
    Пример вызова:
      def(5, 4):
        return 18
      
## Файл triangle.py
  def area(a, h):
  
    Находит площадь треугольника
    Параметры:
      a(int): первое натуральное число
      h(int): второе натуральное число
    Возвращаемое значение: a*h/2
    Пример вызова:
      def(5, 4):
        return 10
  def perimeter(a, b, c):
  
    Находит периметр прямоугольника 
    Параметры:
      a(int): первое натуральное число
      b(int): второе натуральное число
      c(int): третье натуральное число
    Возвращаемое значение: 2+b+c
    Пример вызова:
      def(5, 4, 3):
        return 12
## Файл square.py  
  def area(a):

    Находит площадь квадрата
    Параметры:
      a(int): натуральное число
    Возвращаемое значение: а*а
    Пример вызова:
      def(5):
        return 25

  def perimeter(a):
  
    Находит периметр квадрата
    Параметры:
      a(int): натуральное число
    Возвращаемое значение: 4*а
    Пример вызова:
      def(5):
        return 20

## Файл circle.py
 def area(r):
    
    Находит площадь круга
    Параметры:
     r(int): натуральное число
    Возвращаемое значение: math.pi * r * r

  def perimeter(r):

    Находит периметр круга
    Параметры:
     r(int): натуральное число
    Возвращаемое значение: 2 * math.pi * r

# примеры юниттестов для файла triangle.py

    class TriangleTestCase(unittest.TestCase):
      def test_zero_mul_area(self):
          self.assertEqual(area(10, 0), 0)
  
      def test_negative_number(self):
          self.assertEqual(area(-1, 8), "Incorrect input")
          
      def test_letter_input(self):
          self.assertEqual(area(1, "a"), "Incorrect input")

# примеры юниттестов для файла rectangle.py

    class RectangleTestCase(unittest.TestCase):
      def test_zero_mul_area(self):
          self.assertEqual(area(10, 0), 0)
    
      def test_negative_number(self):
          self.assertEqual(area(-1, 0), "Incorrect input")

# примеры юниттестов для файла circle.py

    class CircleTestCase(unittest.TestCase):
      def test_zero_mul_area(self):
          self.assertEqual(area(0), 0)
  
      def test_negative_number(self):
          self.assertEqual(area(-1), "Incorrect input")
          self.assertEqual(area(4), 50.26548245743669)

# примеры юниттестов для файла square.py

    class SquareTestCase(unittest.TestCase):
        def test_zero_mul_area(self):
            self.assertEqual(area(0), 0)
    
        def test_zero_sum(self):
            self.assertEqual(perimeter(12), 24)


# тест-кейсы для файла circle.py

|     Название теста     |     Входные данные     |     Expected     |     Actual       |
|------------------------|------------------------|------------------|----------------- |
|      perimeter(0)      |        r = 0           |         0        |        0         |
|      perimeter(-1)     |        r = -1          | Incorrect input  | Incorrect input  |
|      area(0)           |        r = 0           |         0        |        0         |
|      area(-5)          |        r = -5          | Incorrect input  | Incorrect input  |
|      area(4)           |        r = 4           | 50.26548245743669| 50.26548245743669|
|      area("a")         |        r = "a"         | Incorrect input  |  Incorrect input |
|      area(true)        |        r = true        | Incorrect input  |  Incorrect input |



# тест-кейсы для файла rectangle.py

|     Название теста     |     Входные данные     |     Expected     |     Actual       |
|------------------------|------------------------|------------------|----------------- |
|      perimeter(12, 0)  |      a = 12  b = 0     |         12       |        12        |
|      perimeter(-5, -5) |      a = -5  b = -5    | Incorrect input  | Incorrect input  |
|      area(-1, 0)       |      a = -1  b = 0     | Incorrect input  | Incorrect input  |
|      area(10, 0)       |      a = 10  b = 0     |         0        |        0         |
|      area(4, 2)        |      a = 4   b = 2     |         8        |        8         |
|      area(6, "a")      |      a = 6   b = "a"   | Incorrect input  | Incorrect input  |


# тест-кейсы для файла triangle.py

|     Название теста     |     Входные данные     |     Expected     |     Actual       |
|------------------------|------------------------|------------------|----------------- |
|   perimeter(10, -1, 8) | a = 10  b = -1  c = 8  | Incorrect input  | Incorrect input  |
|   perimeter(8, 0, 9)   | a = 8  b = 0  c = 9    |        17        |        17        |
|      area(-1, 8)       |      a = -1  b = 8     | Incorrect input  | Incorrect input  |
|      area(10, 0)       |      a = 10  b = 0     |         0        |        0         |
|      area(4, 2)        |      a = 4   b = 2     |         4        |        4         |
|      area(4, "a")      |      a = 4   b = "a"   | Incorrect input  | Incorrect input  |
|      area(true)        |      a = true          | Incorrect input  | Incorrect input  |


# тест-кейсы для файла square.py

|     Название теста     |     Входные данные     |     Expected     |     Actual       |
|------------------------|------------------------|------------------|----------------- |
|      perimeter(0)      |        r = 0           |         0        |        0         |
|      perimeter(-1)     |        r = -1          | Incorrect input  | Incorrect input  |
|      area(0)           |        r = 0           |         0        |        0         |
|      area(-5)          |        r = -5          | Incorrect input  | Incorrect input  |
|      area(4)           |        r = 4           |         16       |        16        |
|      area("a")         |        r = "a"         | Incorrect input  | Incorrect input  |

## История комитов 
  File's added (2c29e18) - добавлен файл rectangle.py
  
  triangle file's added (41e7b31) - добавлен файл triangle.py
  
  formula's changed (06f00e1) - в файле rectangle.py формула a+b изменена на 2*(a+b)

  Update README.md (aee10ad) - добавлена документация 

  comments are added (759fc1d) - добавлены комментарии к файлам
