from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class AirbnbHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://uk.airbnb.com/"
        self.wait = WebDriverWait(driver, 10)

        self.popup_ok_button = (By.XPATH, "//button[contains(text(), 'OK')]")
        self.search_button_to_activate = (By.CSS_SELECTOR, "div[data-testid='little-search']")
        self.where_input = (By.ID, "bigsearch-query-location-input")
        self.suggestion_item = (By.CSS_SELECTOR, "[role='option']")
        self.date_menu_btn = (By.CSS_SELECTOR, "div[data-testid='structured-search-input-field-split-dates-0']")

        self.guests_menu = (By.CSS_SELECTOR, "div[data-testid='structured-search-input-field-guests-button']")
        self.add_adult_btn = (By.CSS_SELECTOR, "button[data-testid='stepper-adults-increase-button']")
        self.search_submit_btn = (By.CSS_SELECTOR, "button[data-testid='structured-search-input-search-button']")

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
        print(f"\n[Info] Location is selected: {location}")

    def open_calendar(self):
        try:
            date_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Додайте дати')]")))
            date_btn.click()
            print("[Info] Calendar is opened.")
        except TimeoutException:
            print("[Info] Calendar is already opened or button is not found.")

    def select_date(self, date_str: str):
        month, day, year = date_str.split('/')
        iso_date = f"{year}-{month}-{day}"

        css_selector = f"button[data-state--date-string='{iso_date}']"
        date_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

        self.driver.execute_script("arguments[0].click();", date_element)
        print(f"[Info] Date button is clicked: {iso_date}")

    def is_autocomplete_visible(self):
        try:
            suggestions = self.wait.until(EC.presence_of_all_elements_located(self.suggestion_item))
            print(f"\n[Info] Found {len(suggestions)} suggestions in the list.")
            return len(suggestions) > 0
        except TimeoutException:
            print("\n[Error] Couldn't find any suggestions in the list.")
            return False

    def add_one_adult_guest(self):
        guests_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Хто')]")))
        guests_field.click()
        print("\n[Info] Opened menu guest choice.")

        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='stepper-adults-increase-button']")))
        add_btn.click()
        print("[Info] Added 1 adult.")

    def click_search_button(self):
        search_xpath = "//button[.//div[text()='Пошук']]"
        search_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, search_xpath)))

        self.driver.execute_script("arguments[0].click();", search_btn)
        print("[Info] Clicked button 'Search'.")
