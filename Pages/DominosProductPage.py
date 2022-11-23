import configparser
import os

from selenium.webdriver.common.by import By

from Pages.DominosHomePage import DominosHomePage


class DominosProductPage(DominosHomePage):

    def __init__(self, browser):
        super().__init__(browser)

        self.config = configparser.RawConfigParser()

        try:
            with open(f"../Repository/ObjectRepository/products.ini", 'r') as f:
                self.config.read(f"../Repository/ObjectRepository/products.ini")
        except FileNotFoundError:
            with open(f"{os.getcwd()}/Repository/ObjectRepository/products.ini", 'r') as f:
                self.config.read(f"{os.getcwd()}/Repository/ObjectRepository/products.ini")

    def is_product_page_loaded(self):
        self.wait_page_load()
        self.wait_visibility_all("DominosProductPage", "ProductPageList_xpath")
        print("Product Page Loaded")

    def add_cart_product(self, product_name):
        self.wait_clickable("DominosProductPage", "ProductPageList_xpath")
        product_by = (By.XPATH, f"(//div[@data-label='{product_name}']//child::button[@data-label='addTocart'])[1]")
        self.action_move(product_by)
        self.js_click(product_by)
        try:
            self.wait_quick("DominosProductPage", "AddExtraNO_xpath").click()
        except Exception:
            pass
        product_cart = (By.XPATH, f"//div[@class='crt-cnt-descrptn']/span[text()='{product_name}']")
        self.wait_visibility(product_cart)
        self.wait_visibility_all("DominosProductPage", "EachProductPrice_xpath")
        product_qty = (By.XPATH, f"//div[@class='crt-cnt-descrptn']/span[text()='"
                                 f"{product_name}']/../../..//child::span[@class='cntr-val']")
        product_price = (By.XPATH, f"//div[@class='crt-cnt-descrptn']/span[text()='"
                                   f"{product_name}']/../../..//child::span[@class='rupee']")
        self.wait_presence(product_qty)
        self.wait_presence(product_price)
        print(f"Added to Cart - {product_name} "
              f"| Qty - {self.get_text(product_qty)} | Price - {self.get_text(product_price)}")

    def cart_value_verify(self):
        each_product_value_ele = self.wait_visibility_all("DominosProductPage", "EachProductPrice_xpath")
        each_product_value_list = []
        for ele in each_product_value_ele:
            each_product_value_list.append(float(ele.text))
        print(each_product_value_list)
        if sum(each_product_value_list) == float(self.get_text("DominosProductPage", "SubTotalPrice_xpath")):
            print("Each Product Total Value ( "+str(sum(each_product_value_list))+" ) == Sub Total Value ( "+
                  self.get_text("DominosProductPage", "SubTotalPrice_xpath") + " )")
        else:
            assert sum(each_product_value_list) == float(self.get_text("DominosProductPage", "SubTotalPrice_xpath"))

    def add_cart_list(self, product_list_name):
        self.wait_page_load()
        items_list = self.config.items(product_list_name)
        for product, qty in items_list:
            self.add_cart_product(product.title())
