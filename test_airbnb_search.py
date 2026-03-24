import pytest
from selenium import webdriver
from home_page import AirbnbHomePage


def test_tc_013_location_autocomplete():
    driver = webdriver.Chrome()
    driver.maximize_window()
    home_page = AirbnbHomePage(driver)

    try:
        home_page.load()
        home_page.close_welcome_popup()
        home_page.activate_search()
        home_page.enter_location("Kyi")

        assert home_page.is_autocomplete_visible() == True, "Dropdown with suggestions did not appear!"
        print("\nTC_013 Passed: Autocomplete is working correctly.")

    finally:
        driver.quit()
