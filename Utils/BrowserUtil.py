
from selenium import webdriver
from selenium.webdriver import FirefoxProfile


class BrowserUtil:

    @staticmethod
    def get(request):
        name = request.param[5].lower()
        if name == 'chrome':
            browser = webdriver.Chrome()
        elif name == 'firefox':
            firefox_profile = FirefoxProfile()
            firefox_profile.set_preference("geo.enabled", True)
            firefox_profile.set_preference("geo.provider.use_corelocation", True)
            firefox_profile.set_preference("geo.prompt.testing", True)
            firefox_profile.set_preference("geo.prompt.testing.allow", True)
            browser = webdriver.Firefox(firefox_profile=firefox_profile)
        elif name == 'edge':
            browser = webdriver.Edge()
        else:
            browser = webdriver.Chrome()
        browser.maximize_window()
        browser.implicitly_wait(15)
        browser.get("https://www.dominos.co.in/")
        return browser
