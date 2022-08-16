from selenium.webdriver.support         import expected_conditions as EC
from selenium.webdriver.support.wait    import WebDriverWait
from appium.webdriver.common.mobileby   import MobileBy

class Calculator:
    def __init__(self, driver):
        self.driver = driver

        self.result = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'com.miui.calculator:id/result'
        )))
        self.addition = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, 'plus'
        )))
        self.division = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, 'divide'
        )))
        self.multiplication = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, 'multiply'
        )))
        self.subtraction = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, 'minus'
        )))

    def clickNumber(self, num):
        _num = str(num)
        self.driver.instance.find_element(MobileBy.ID, "com.miui.calculator:id/btn_" + _num + "_s").click()
        #assert _num in self.result.text, 'Resultado não é esperado com o valor esperado.'

    def summing(self, num1, num2):
        self.clickNumber(num1)
        self.addition.click()
        self.clickNumber(num2)

        result = sum(num1, num2)
        calcResult = int(self.result.text)
        assert result == calcResult, 'Resultados diferentes para soma'

    def multiplying(self, num1, num2):
        self.clicknumber(num1)
        self.multiplication.click()
        self.clicknumber(num2)

        result = num1 * num2
        calcResult = int(self.result.text)
        assert result == calcResult, 'Resultados diferentes para multiplicação'