# Instalar o pacote para executar Appium
# pip install Appium-Python-Client
# run test: python -m unittest tests/test_something.py

import unittest
from time                               import sleep
from appium                             import webdriver
from appium.webdriver.common.appiumby   import AppiumBy

from _webDriver.Webdriver               import Driver
from _pageObjects.HomeScreen            import CalcHomeScreen       as CHS
from _pageObjects.TermsAndConditions    import TermsAndConditions   as TAC

from selenium.webdriver.common.action_chains            import ActionChains
from selenium.webdriver.common.actions                  import interaction
from selenium.webdriver.common.actions.action_builder   import ActionBuilder
from selenium.webdriver.common.actions.pointer_input    import PointerInput

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_openApp(self):
        actions = ActionChains(self.driver.instance)
        actions.w3c_actions = ActionBuilder(self.driver.instance, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(545, 1612)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(557, 819)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
    
        el2 = self.driver.instance.find_element(by=AppiumBy.XPATH, value="(//android.widget.TextView[@content-desc=\"Calculator\"])[2]")
        el2.click()

        # Permitir o click no botão de aceitar termos e condições
        # Liberar para dispositivo emulado
        """
        actions = ActionChains(self.driver.instance)
        actions.w3c_actions = ActionBuilder(self.driver.instance, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(771, 2018)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        # Liberar para dispositivo fisico
        el2 = self.driver.instance.find_element(by=AppiumBy.ID, value="android:id/button1")
        el2.click()
        """

    def test_sum(self):
        calcHS = CHS(self.driver)
        calcHS.sumCalc(3, 9)

    def tearDown(self):
        self.driver.instance.quit()    
