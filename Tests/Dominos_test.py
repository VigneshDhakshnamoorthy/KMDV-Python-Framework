from time import sleep

import pytest

from Pages.DominosProductPage import DominosProductPage
from Tests.TestBase import TestBase


class TestDominos(TestBase):
    pincode = "600100"
    product_list_VEG = "ADD CART LIST - VEG PIZZA"
    product_list_NVEG = "ADD CART LIST - NON-VEG PIZZA"
    product_list_SID = "ADD CART LIST - SIDES"

    @pytest.mark.parametrize("get_browser", TestBase.get_data_json("Dominos Add Cart"), indirect=["get_browser"])
    def test_dominos(self, get_browser):
        product_page = DominosProductPage(get_browser)
        product_page.is_home_page_loaded()
        product_page.click_order_online()
        product_page.close_popup()
        product_page.update_location(self.pincode)
        product_page.is_product_page_loaded()
        product_page.add_cart_list(self.product_list_VEG)
        product_page.cart_value_verify()
        product_page.add_cart_list(self.product_list_NVEG)
        product_page.cart_value_verify()
        product_page.add_cart_list(self.product_list_SID)
        product_page.cart_value_verify()
        sleep(2)
