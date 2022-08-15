from appium     import webdriver

class Driver:
    def __init__(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '08f3dc7b0404'
        }
        
        self.instante = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)