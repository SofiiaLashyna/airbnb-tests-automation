import pytest
from selenium import webdriver
from property_page import AirbnbPropertyPage
import time


def test_tc_002_dynamic_price_calculation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    property_page = AirbnbPropertyPage(driver)

    property_url = "https://uk.airbnb.com/rooms/1474650919129609972?check_in=2026-09-18&check_out=2026-09-20&photo_id=2277640875&source_impression_id=p3_1774392303_P3Gb0I591e5HICF2&previous_page_section_name=1000"

    try:
        property_page.load(property_url)
        property_page.close_translation_popup()

        assert property_page.is_booking_widget_visible() == True, "Booking widget is not visible!"
        print("\nBooking widget is visible!.")

        property_page.open_calendar()

        property_page.select_date("09/26/2026")
        time.sleep(1)
        property_page.select_date("09/28/2026")

    finally:
        driver.quit()