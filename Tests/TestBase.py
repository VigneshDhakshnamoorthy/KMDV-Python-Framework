
import pytest

from Utils.BrowserUtil import BrowserUtil
from Utils.ExcelUtil import ExcelUtil
from Utils.JsonUtil import JsonUtil


class TestBase:

    @staticmethod
    def get_data_excel(test_case_name):
        arr = ExcelUtil("mercy").get_test_data(test_case_name)
        for row in arr:
            yield row

    @staticmethod
    def get_data_json(test_case_name):
        arr = JsonUtil("mercy").get_test_data(test_case_name)
        for row in arr:
            yield row

    @pytest.fixture(scope="function")
    def get_browser(self, request):
        browser = BrowserUtil().get(request)
        yield browser
        browser.quit()


