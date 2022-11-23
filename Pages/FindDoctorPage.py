from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage


class FindDoctorPage(HomePage):
    FindDoctor_logo = (By.XPATH, "//h1[@class='banner__heading relative z-1 regular mt2']")
    CareOption_heading = (By.XPATH, "// h2[text() = 'Convenient Care Options Near You']")
    CareOption_load = (By.XPATH, "//h2[@class='mt1 mb2 h4']")
    PrimaryCare_btn = (By.XPATH, "//a[@class='btn' and contains(text(),'Primary Care')]")
    Gynecology_btn = (By.XPATH, "//a[@class='btn' and contains(text(),'OBGYN')]")
    Cardiology_btn = (By.XPATH, "//a[@class='btn' and contains(text(),'Cardiology')]")
    Orthopedics_btn = (By.XPATH, "//a[@class='btn' and contains(text(),'Orthopedics')]")
    ProviderCount = (By.XPATH, "//div[@class='provider-search-results__sentence']")

    def __int__(self, browser):
        super.__init__(browser)

    def is_find_doctor_page_loaded(self):
        self.wait_page_load()
        self.wait_all_presence(self.FindDoctor_logo)
        self.wait_all_presence(self.CareOption_heading)
        print("Find Doctor Page Loaded")

    def back_to_care_option(self):
        self.browser.back()
        self.wait_all_presence(self.CareOption_heading)

    def click_primary_care(self):
        self.click(self.PrimaryCare_btn)
        self.wait_all_presence(self.CareOption_load)
        print("PrimaryCare Provider Count = "+self.get_provider_count())

    def click_gynecology_care(self):
        self.click(self.Gynecology_btn)
        self.wait_all_presence(self.CareOption_load)
        print("Gynecology Provider Count = "+self.get_provider_count())

    def click_cardiology_care(self):
        self.click(self.Cardiology_btn)
        self.wait_all_presence(self.CareOption_load)
        print("Cardiology Provider Count = "+self.get_provider_count())

    def click_orthopedics_care(self):
        self.click(self.Orthopedics_btn)
        self.wait_all_presence(self.CareOption_load)
        print("Orthopedics Provider Count = "+self.get_provider_count())

    def get_provider_count(self):
        return self.wait_visibility(self.ProviderCount).text.split(" ", 1)[0]





