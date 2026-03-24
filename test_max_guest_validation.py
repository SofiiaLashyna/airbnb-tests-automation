import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_tc_018_url_guest_manipulation():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        malicious_url = "https://uk.airbnb.com/s/Lviv/homes?adults=150"
        print(f"\n[Info] Go by the URL: {malicious_url}")
        driver.get(malicious_url)

        time.sleep(5)

        page_text = driver.find_element(By.TAG_NAME, "body").text

        print("[Info] Check whether we can see '150' adults...")

        assert "150" not in page_text, "Bug is found!."

        print("\nTC_018 Passed: system blocked invalid number of guests.")

    finally:
        driver.quit()