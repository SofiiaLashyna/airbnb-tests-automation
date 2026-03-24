import pytest
from selenium import webdriver
from home_page import AirbnbHomePage
import time


def test_tc_001_search_functionality():
    driver = webdriver.Chrome()
    driver.maximize_window()
    home_page = AirbnbHomePage(driver)

    try:
        home_page.load()
        home_page.close_welcome_popup()
        home_page.activate_search()
        home_page.enter_location("Lviv")

        home_page.open_calendar()

        home_page.select_date("04/15/2026")
        time.sleep(1)
        home_page.select_date("04/20/2026")

        home_page.add_one_adult_guest()
        home_page.click_search_button()
    finally:
        driver.quit()
