
def area(a):

```
принимает один натуральный аргумент - а
возвращает квадрат а
```
    return a * a


def perimeter(a):
```
принимает один натуральный аргумент - а
возвращает а умноженное на 4
```
    return 4 * a


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul_area(self):
        self.assertEqual(area(10, 0), 0)

    def test_negative_number(self):
        self.assertEqual(area(-1, 0), "Incorrect input")

        self.assertEqual(perimeter(-5, -5), "Incorrect input")

    def test_zero_sum(self):
        self.assertEqual(perimeter(12, 0), 24)
