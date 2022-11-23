import configparser
import os

from selenium.webdriver.common.by import By


class LocatorUtil:

    def __init__(self, file_name):
        self.config = configparser.RawConfigParser()

        try:
            with open(f"../Repository/ObjectRepository/{file_name}.ini", 'r') as f:
                self.config.read(f"../Repository/ObjectRepository/{file_name}.ini")
        except FileNotFoundError:
            with open(f"{os.getcwd()}/Repository/ObjectRepository/{file_name}.ini", 'r') as f:
                self.config.read(f"{os.getcwd()}/Repository/ObjectRepository/{file_name}.ini")

    def get_value(self, section, locator_name):
        return self.config.get(section, locator_name)

    def get_by(self, section, locator_name):
        get_prop = self.get_value(section, locator_name)
        by_type = locator_name.lower().split("_")[-1]
        by_value = None
        if by_type == 'xpath':
            by_value = (By.XPATH, get_prop)
        elif by_type == 'id':
            by_value = (By.ID, get_prop)
        elif by_type == 'name':
            by_value = (By.NAME, get_prop)
        elif by_type == 'class':
            by_value = (By.CLASS_NAME, get_prop)
        elif by_type == 'css':
            by_value = (By.CSS_SELECTOR, get_prop)
        elif by_type == 'link':
            by_value = (By.LINK_TEXT, get_prop)
        elif by_type == 'partial':
            by_value = (By.PARTIAL_LINK_TEXT, get_prop)
        elif by_type == 'tag':
            by_value = (By.TAG_NAME, get_prop)
        return by_value
