from selenium.webdriver.support         import expected_conditions as EC
from selenium.webdriver.support.wait    import WebDriverWait
from appium.webdriver.common.mobileby   import MobileBy

class CalcHomeScreen:
    def __init__(self, driver):
        self.driver = driver       

    def plusBtnTouch(self):
        WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ACCESSIBILITY_ID, "plus"
        ))).click()
        
    def resultField(self):
        return WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, "com.miui.calculator:id/result"
        )))

    def numTouch(self, num):
        num = str(num)
        self.driver.instance.find_element(MobileBy.ID, f"com.miui.calculator:id/btn_{num}_s").click()

    def sumCalc(self, num1, num2):
        self.numTouch(num1)
        self.plusBtnTouch()
        self.numTouch(num2)
        self.result = self.resultField()

        if self.result.text == f"= {num1+num2}":
            print("Deu certo!")
        else:
            print("Não deu certo AINDA!")
