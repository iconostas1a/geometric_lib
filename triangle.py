def area(a, h):

 ```
    принимает два аргумента a, h - сторона и высота треугольника
    возвращает произведение a и h/2
   ```
    return a * h / 2

def perimeter(a, b, c):
  ```
    принимает три натурадьных аргумента - a, b, c
    возвращает сумму трёх сторон треугольника

    ```

    return a * h / 2



class TriangleTestCase(unittest.TestCase):
    def test_zero_mul_area(self):
        self.assertEqual(area(10, 0), 0)

    def test_negative_number(self):
        self.assertEqual(area(-1, 8), "Incorrect input")

        self.assertEqual(perimeter(10, -1, 8), "Incorrect input")

    def test_zero_sum(self):
        self.assertEqual(perimeter(8, 0, 9), 17)
