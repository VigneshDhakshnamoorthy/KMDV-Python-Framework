from selenium.webdriver.common.alert import Alert

from Pages.PageBase import PageBase


class DominosHomePage(PageBase):

    def __init__(self, browser):
        super().__init__(browser)

    def is_home_page_loaded(self):
        self.wait_visibility("DominosHomePage", "OrderOnlineBtn_xpath")
        print("Home Page Loaded")

    def click_order_online(self):
        self.click("DominosHomePage", "OrderOnlineBtn_xpath")
        print("Order Online Button Clicked")

    def close_popup(self):
        try:
            self.switch_frame("moe-onsite-campaign-630dd4f74685e185561359ff")
            self.click("DominosHomePage", "PopupAdCloseBtn_xpath")
            self.switch_default()
            print("Popup Closed")

        except Exception:
            pass

    def update_location(self, pincode):
        self.pin = pincode
        self.wait_page_load()
        self.click("DominosHomePage", "LocationInput_xpath")
        print("Location Button Clicked")
        self.type(self.locator.get_by("DominosHomePage", "LocationInputBox_xpath"), self.pin)
        print("Updated The Location To : "+self.pin)
        self.wait_page_load()
        self.click("DominosHomePage", "LocationSearchBtn_xpath")
        print("Locate me Button Clicked")
        self.wait_page_load()
