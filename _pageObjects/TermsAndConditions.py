from selenium.webdriver.support         import expected_conditions as EC
from selenium.webdriver.support.wait    import WebDriverWait
from appium.webdriver.common.mobileby   import MobileBy

class TermsAndConditions:
    def __init__(self, driver):
        self.driver = driver
        self.agree_btn = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, "android:id/button1"
        )))

        self.decline_btn = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, "android:id/button2"
        )))

    def accept(self):
        self.agree_btn.click()
    
    def decline(self):
        self.decline_btn.click()