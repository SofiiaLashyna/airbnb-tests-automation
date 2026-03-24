import pytest
from selenium import webdriver
from home_page import AirbnbHomePage
import time


def test_tc_011_switch_to_experiences():
    driver = webdriver.Chrome()
    driver.maximize_window()
    home_page = AirbnbHomePage(driver)

    try:
        home_page.load()
        home_page.close_welcome_popup()

        time.sleep(2)

        home_page.switch_to_experiences()

        time.sleep(2)

        current_url = driver.current_url
        assert "experiences" in current_url.lower() or "search_type" in current_url.lower(), "URL haven't changed to 'experiences'!"

        print("\nTC_011 Passed: Success!")

    finally:
        driver.quit()