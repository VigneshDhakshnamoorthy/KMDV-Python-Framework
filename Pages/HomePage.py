from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from Pages.PageBase import PageBase


class HomePage(PageBase):
    SectionName = "HomePage"
    HomePage_logo = (By.XPATH, "//img[@alt='Mercy Health']")
    Location_btn = (By.XPATH, "//button[@id='global-nav-location']/span")
    Location_heading = (By.XPATH, "//div[@class='subheading blue pb3 bb-light-grey']")
    Location_searchBox = (By.XPATH, "//div[@id='PlacesAutocomplete__root']/input")
    SaveLocation = (By.XPATH, "//button[@class='btn mr2 flex-1']")
    findDoctor_nav_link = (By.XPATH, "//div[@class='global-nav__main']/div/a[@href='/find-a-doctor']")
    conditionsTreatments_nav_link = (By.XPATH, "// div[ @class ='global-nav__main']/a["
                                               "@href='/conditions-and-treatments']")
    currentLocation = (By.XPATH, "//span[@class='inline-block mr3']")
    locationName = None

    def __init__(self, browser):
        super().__init__(browser)

    def is_homepage_loaded(self):
        self.wait_page_load()
        self.wait_visibility(self.SectionName, "LocationBtn_xpath")
        self.wait_all_presence(self.HomePage_logo)
        print("Home Page Loaded")

    def click_location_box(self):
        self.js_click(self.SectionName, "LocationBtn_xpath")
        print("Clicked on Location Box")

    def enter_location_search_box(self, location):
        self.locationName = location
        location_by = (By.XPATH, f"//div[contains(text(),'{location}')]")
        try:
            self.wait_visibility(self.Location_heading)
            self.wait_visibility(self.Location_searchBox)
            self.type(self.Location_searchBox, self.locationName)
            self.click(location_by)
        except TimeoutException:
            self.js_click(self.Location_btn)
            self.type(self.Location_searchBox, self.locationName)
            self.click(location_by)
        self.wait_visibility(self.SaveLocation)
        print("Updated the Location : " + self.locationName)

    def save_location(self):
        self.click(self.SaveLocation)
        self.browser.refresh()
        print("Location Saved")

    def click_find_doctor_link(self):
        self.click(self.findDoctor_nav_link)
        print("Clicked on Find Doctor Nav Link")

    def click_conditions_treatments_link(self):
        self.click(self.conditionsTreatments_nav_link)
        print("Clicked on Conditions & Treatments Nav Link")
