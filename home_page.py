from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AirbnbHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://uk.airbnb.com/"
        self.wait = WebDriverWait(driver, 10)

        self.popup_ok_button = (By.XPATH, "//button[contains(text(), 'OK')]")

        self.search_button_to_activate = (By.CSS_SELECTOR, "div[data-testid='little-search']")
        self.where_input = (By.ID, "bigsearch-query-location-input")
        self.suggestion_item = (By.CSS_SELECTOR, "[role='option']")

    def load(self):
        self.driver.get(self.url)

    def close_welcome_popup(self):
        try:
            short_wait = WebDriverWait(self.driver, 4)
            ok_btn = short_wait.until(EC.element_to_be_clickable(self.popup_ok_button))
            ok_btn.click()
            print("\n[Info] Welcome popup closed.")
        except TimeoutException:
            print("\n[Info] No welcome popup appeared, moving on.")

    def activate_search(self):
        try:
            big_search_btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='structured-search-input-field-query']")))
            big_search_btn.click()
            print("\n[Info] Clicked big search bar.")
        except TimeoutException:
            small_search_btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='little-search']")))
            small_search_btn.click()
            print("\n[Info] Clicked little search button.")

    def enter_location(self, location: str):
        input_field = self.wait.until(EC.visibility_of_element_located(self.where_input))
        input_field.clear()
        input_field.send_keys(location)

    def is_autocomplete_visible(self):
        try:
            suggestions = self.wait.until(EC.presence_of_all_elements_located(self.suggestion_item))
            print(f"\n[Info] Знайдено {len(suggestions)} підказок у списку.")
            return len(suggestions) > 0
        except TimeoutException:
            print("\n[Error] Підказки так і не з'явилися.")
            return False
