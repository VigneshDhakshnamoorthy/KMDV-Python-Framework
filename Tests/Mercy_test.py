import pytest

from Pages.FindDoctorPage import FindDoctorPage
from Tests.TestBase import TestBase


class TestMercy(TestBase):

    location_name = "Cincinnati, OH 45201, USA"

    @pytest.mark.parametrize("get_browser", TestBase.get_data_excel("Dominos Add Cart"), indirect=["get_browser"])
    def test_mercy(self, get_browser):
        find_doctor = FindDoctorPage(get_browser)
        find_doctor.is_homepage_loaded()
        find_doctor.click_location_box()
        find_doctor.enter_location_search_box(self.location_name)
        find_doctor.save_location()
        find_doctor.click_find_doctor_link()
        find_doctor.is_find_doctor_page_loaded()
        find_doctor.click_primary_care()
        find_doctor.back_to_care_option()
        find_doctor.click_gynecology_care()
        find_doctor.back_to_care_option()
        find_doctor.click_cardiology_care()
        find_doctor.back_to_care_option()
        find_doctor.click_orthopedics_care()
