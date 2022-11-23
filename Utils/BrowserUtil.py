from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class BrowserUtil:

    @staticmethod
    def get(request):
        name = request.param[5].lower()
        if name == 'chrome':
            browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif name == 'firefox':
            firefox_profile = FirefoxProfile()
            firefox_profile.set_preference("geo.enabled", True)
            firefox_profile.set_preference("geo.provider.use_corelocation", True)
            firefox_profile.set_preference("geo.prompt.testing", True)
            firefox_profile.set_preference("geo.prompt.testing.allow", True)
            browser = webdriver.Firefox(firefox_profile=firefox_profile,
                                        service=FirefoxService(GeckoDriverManager().install()))
        elif name == 'edge':
            browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.maximize_window()
        browser.implicitly_wait(15)
        browser.get("https://www.dominos.co.in/")
        return browser
