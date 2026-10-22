from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AirbnbHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://uk.airbnb.com/"
        self.wait = WebDriverWait(driver, 10)
        self.short_wait = WebDriverWait(driver, 4)
        self.popup_ok_button = (By.XPATH, "//button[contains(text(), 'OK')]")
        self.search_button_to_activate = (By.CSS_SELECTOR, "div[data-testid='little-search']")
        self.big_search_btn = (By.CSS_SELECTOR, "[data-testid='structured-search-input-field-query']")

        self.where_input = (By.ID, "bigsearch-query-location-input")
        self.suggestion_item = (By.CSS_SELECTOR, "[role='option']")

        self.add_date_btn = (By.XPATH, "//*[contains(text(), 'Add date')]")
        self.date_menu_btn = (By.CSS_SELECTOR, "div[data-testid='structured-search-input-field-split-dates-0']")

        self.date_btn_template = "button[data-state--date-string='{}']"

        self.guests_menu = (By.CSS_SELECTOR, "div[data-testid='structured-search-input-field-guests-button']")
        self.who_guests_field = (By.XPATH, "//*[contains(text(), 'Хто')]")
        self.add_adult_btn = (By.CSS_SELECTOR, "button[data-testid='stepper-adults-increase-button']")

        self.submit_search_btn = (By.XPATH, "//button[.//div[text()='Пошук']]")
        self.experiences_tab = (By.ID, "search-block-tab-EXPERIENCES")

    def load(self):
        self.driver.get(self.url)

    def close_welcome_popup(self):
        try:
            ok_btn = self.short_wait.until(EC.element_to_be_clickable(self.popup_ok_button))
            ok_btn.click()
            print("\n[Info] Welcome popup closed.")
        except TimeoutException:
            print("\n[Info] No welcome popup appeared, moving on.")

    def activate_search(self):
        try:
            big_search_btn = self.wait.until(EC.element_to_be_clickable(self.big_search_btn))
            big_search_btn.click()
            print("\n[Info] Clicked big search bar.")
        except TimeoutException:
            small_search_btn = self.wait.until(EC.element_to_be_clickable(self.search_button_to_activate))
            small_search_btn.click()
            print("\n[Info] Clicked little search button.")

    def enter_location(self, location: str):
        input_field = self.wait.until(EC.visibility_of_element_located(self.where_input))
        input_field.clear()
        input_field.send_keys(location)
        print(f"\n[Info] Location is typed: {location}")

        try:
            first_suggestion = self.wait.until(EC.element_to_be_clickable(self.suggestion_item))
            first_suggestion.click()
            print("[Info] Clicked on the first location suggestion.")
        except TimeoutException:
            print("[Warning] Dropdown suggestions didn't appear.")

    def open_calendar(self):
        try:
            date_btn = self.wait.until(EC.element_to_be_clickable(self.add_date_btn))
            date_btn.click()
            print("[Info] Calendar is opened.")
        except TimeoutException:
            print("[Info] Calendar is already opened or button is not found.")

    def select_date(self, date_str: str):
        month, day, year = date_str.split('/')
        iso_date = f"{year}-{month}-{day}"

        css_selector = self.date_btn_template.format(iso_date)
        date_locator = (By.CSS_SELECTOR, css_selector)

        date_element = self.wait.until(EC.presence_of_element_located(date_locator))

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
        guests_field = self.wait.until(EC.element_to_be_clickable(self.who_guests_field))
        guests_field.click()
        print("\n[Info] Opened menu guest choice.")

        add_btn = self.wait.until(EC.element_to_be_clickable(self.add_adult_btn))
        add_btn.click()
        print("[Info] Added 1 adult.")

    def click_search_button(self):
        search_btn = self.wait.until(EC.element_to_be_clickable(self.submit_search_btn))
        self.driver.execute_script("arguments[0].click();", search_btn)
        print("[Info] Clicked button 'Search'.")

    def switch_to_experiences(self):
        try:
            exp_tab = self.wait.until(EC.presence_of_element_located(self.experiences_tab))
            self.driver.execute_script("arguments[0].click();", exp_tab)
            print("\n[Info] Switched to experiences.")
        except TimeoutException:
            print("\n[Error] Page 'experiences' not found.")