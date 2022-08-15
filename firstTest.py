# Instalar o pacote para executar Appium
# pip install Appium-Python-Client

from appium                             import webdriver
from appium.webdriver.common.appiumby   import AppiumBy
from time                               import sleep

# For W3C actions
from selenium.webdriver.common.action_chains            import ActionChains
from selenium.webdriver.common.actions                  import interaction
from selenium.webdriver.common.actions.action_builder   import ActionBuilder
from selenium.webdriver.common.actions.pointer_input    import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "08f3dc7b0404"
"""
caps["appPackage"] = "com.miui.calculator"
caps["appActivity"] = "com.miui.calculator.cal.CalculatorActivity"
"""
#caps["avd"] = "AppiumP"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

sleep(2)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(542, 1851)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(555, 661)
actions.w3c_actions.pointer_action.release()
actions.perform()

sleep(2)

el1 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@content-desc=\"Calculator\"])[2]")
el1.click()

sleep(2)

el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="clear")
el12.click()
el13 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_9_s")
el13.click()
el14 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_8_s")
el14.click()
el15 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="multiply")
el15.click()
el16 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_6_s")
el16.click()
el17 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="point")
el17.click()
el18 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_9_s")
el18.click()
el19 = driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_3_s")
el19.click()
el20 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")
el20.click()

sleep(1)

if driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/result").text == "= 679.14":
    print("Deu certo!")

driver.quit()