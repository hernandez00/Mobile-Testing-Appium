import unittest
from _pageObjects.Calc      import Calculator
from _webdriver.Webdriver   import Driver
from time                   import sleep

class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_sum(self):
        calculator = Calculator(self.driver)
        calculator.summing(1, 2)

    def test_multiplicacao(self):
        calculator = Calculator(self.driver)
        calculator.multiplying(2, 3)

    def tearDown(self):
        self.driver.instance.quit()