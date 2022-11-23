from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

from Utils.LocatorUtil import LocatorUtil


class PageBase:

    def __init__(self, browser):
        self.browser = browser
        self.locator = LocatorUtil("mercy")
        self.waitTime = 15
        self.pin = None

    def close_instance(self):
        self.browser.quit()

    def is_page_load(self):
        if str(self.browser.execute_script("return document.readyState")).__contains__("complete") or \
                str(self.browser.execute_script("return document.readyState")).__contains__("active"):
            return True
        else:
            return False

    def wait_page_load(self):
        i = 0
        while i < self.waitTime:
            if self.is_page_load():
                break
            else:
                sleep(1)
                i += 1

    def wait_visibility(self, *args):
        return WebDriverWait(self.browser, self.waitTime, poll_frequency=1). \
            until(ec.visibility_of_element_located(self.arg_div(*args)))

    def wait_visibility_all(self, *args):
        return WebDriverWait(self.browser, self.waitTime, poll_frequency=1). \
            until(ec.visibility_of_all_elements_located(self.arg_div(*args)))

    def wait_clickable(self, *args):
        return WebDriverWait(self.browser, self.waitTime, poll_frequency=1). \
            until(ec.element_to_be_clickable(self.arg_div(*args)))

    def wait_presence(self, *args):
        return WebDriverWait(self.browser, self.waitTime, poll_frequency=1). \
            until(ec.presence_of_element_located(self.arg_div(*args)))

    def wait_quick(self, *args):
        return WebDriverWait(self.browser, 3, poll_frequency=1). \
            until(ec.visibility_of_element_located(self.arg_div(*args)))

    def wait_all_presence(self, *args):
        return WebDriverWait(self.browser, self.waitTime, poll_frequency=1). \
            until(ec.presence_of_all_elements_located(self.arg_div(*args)))

    def arg_div(self, *args):
        self.wait_page_load()
        if len(args) == 1:
            return args[0]
        elif len(args) == 2:
            return self.locator.get_by(*args)

    def wait_alart(self):
        self.wait_page_load()
        return WebDriverWait(self.browser, self.waitTime, poll_frequency=1).until(ec.alert_is_present())

    def click(self, *args):
        self.wait_clickable(self.arg_div(*args)).click()

    def action_click(self, *args):
        self.wait_page_load()
        action = ActionChains(self.browser)
        element = self.wait_clickable(*args)
        action.move_to_element(element).click(element).perform()

    def js_click(self, *args):
        self.wait_page_load()
        self.browser.execute_script("arguments[0].click();", self.wait_clickable(*args))

    def js_type(self, by, text):
        self.wait_page_load()
        self.browser.execute_script(f"arguments[0].value='{text}';", self.wait_clickable(by))

    def js_scroll(self, *args):
        self.wait_page_load()
        self.browser.execute_script("arguments[0].scrollIntoView();", self.wait_presence(*args))

    def type(self, by, text):
        self.wait_page_load()
        self.wait_visibility(by).send_keys(text)

    def action_type(self, by, text):
        self.wait_page_load()
        action = ActionChains(self.browser)
        element = self.wait_visibility(by)
        action.move_to_element(element).send_keys_to_element(element, text).perform()

    def action_move(self, *args):
        self.wait_page_load()
        action = ActionChains(self.browser)
        element = self.wait_visibility(*args)
        action.move_to_element(element).perform()

    def type_enter(self, by, text):
        self.wait_page_load()
        self.wait_visibility(by).send_keys(text + Keys.ENTER)

    def get_text(self, *args):
        self.wait_page_load()
        return self.wait_visibility(*args).text

    def verify_text(self, by, text):
        self.wait_page_load()
        return self.get_text(by) == text

    def get_title(self):
        self.wait_page_load()
        return self.browser.title

    def switch_frame(self, text):
        self.browser.switch_to.frame(text)

    def switch_default(self):
        self.browser.switch_to.default_content()
