from appium import webdriver
#from appium.options.android             import UiAutomator2Options

class Driver:
    def __init__(self):
        self._caps = {
            "platformName": "Android",
            "appium:deviceName": "emulator-5554",
            "appium:avd": "AppiumTestA11"
        }

        self.instance = webdriver.Remote('http://192.168.100.221:4723/wd/hub', self._caps)

"""
        self._options = UiAutomator2Options

        self._options.platform_name = "Android"
        self._options.device_name   = "emulator-5554"
        self._options.avd           = "AppiumTestA11"
        self._options.app_package   = "com.miui.calculator"
        self._options.app_activity  = "com.miui.calculator.cal.CalculatorActivity"

        self.instance = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self._options)
"""