import booking.constants as const
import os
from selenium import webdriver
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\selenium_drivers",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()# chon duong dan tu PATH

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()# tu thoat

    def land_first_page(self):
        self.get(const.BASE_URL)#tu dong mo page moi tu URL

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()# tự động chọn nơi để đi

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()# tự động chọn ngày trả phòng

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()# tự động chọn ngày trả phòng

    def select_adults(self, count=1):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()# chọn số người


    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()# tự động click vào nút tìm