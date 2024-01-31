import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FS


DRIVER_PATH_CHROME = '../chromedriver'
DRIVER_PATH_FIREFOX = '../geckodriver'


#@pytest.fixture(scope='function')
#def driver():

#    service = Service(executable_path=DRIVER_PATH)
 #   options = Options()
#    options.add_argument("--window-size=1920,1080")
 #   driver = webdriver.Chrome(service=service, options=options)
#    yield driver
#    driver.quit()

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        service = FS(executable_path=DRIVER_PATH_FIREFOX)
        driver = webdriver.Firefox(service=service)
    elif request.param == 'chrome':
        service = Service(executable_path=DRIVER_PATH_CHROME)
        options = Options()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

#class WebdriverFactory:
##    @staticmethod
 #   def getWebdriver(browserName):
 #       if browserName == 'firefox':
 #           return webdriver.Firefox()
 #       elif browserName == 'chrome':
 #           return webdriver.Chrome()