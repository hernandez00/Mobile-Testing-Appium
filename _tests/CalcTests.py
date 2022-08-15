import unittest
from _pageObjects.Calc      import Calculator
from Webdriver              import Driver

class CalculadoraTestes(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_sum(self):
        calculator = Calculator(self.driver)
        calculator.somming(1, 2)

    def test_multiplicacao(self):
        calculator = Calculator(self.driver)
        calculator.multiplying(2, 3)

    def tearDown(self):
        self.driver.instance.quit()
    
if __name__ == '__main__':
    unittest.main()