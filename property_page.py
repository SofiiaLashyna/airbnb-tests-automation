from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AirbnbPropertyPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.booking_widget = (By.CSS_SELECTOR, "[data-section-id='BOOK_IT_SIDEBAR']")
        self.check_in_btn = (By.CSS_SELECTOR, "div[data-testid='book-it-default-checkin']")
        self.reserve_btn = (By.CSS_SELECTOR, "button[data-testid='homes-pdp-cta-btn']")

        self.disclaimer_text = (By.XPATH,
                                "//*[contains(text(), 'Плата поки що не стягуватиметься') or contains(text(), 'You won’t be charged yet')]")

    def close_translation_popup(self):
        try:
            close_btn_xpath = "//button[@aria-label='Закрити' or @aria-label='Close']"

            short_wait = WebDriverWait(self.driver, 5)
            close_btn = short_wait.until(EC.element_to_be_clickable((By.XPATH, close_btn_xpath)))
            close_btn.click()
            print("\n[Info] Translation popup closed.")
        except TimeoutException:
            print("\n[Info] Translation popup haven't showed up.")

    def load(self, url: str):
        self.driver.get(url)
        print(f"\n[Info] Load house page: {url}")

    def is_booking_widget_visible(self):
        try:
            widget = self.wait.until(EC.visibility_of_element_located(self.booking_widget))
            return widget.is_displayed()
        except TimeoutException:
            print("\n[Error] Booking widget is not visible!.")
            return False

    def open_calendar(self):
        try:
            check_in = self.wait.until(EC.element_to_be_clickable(self.check_in_btn))
            check_in.click()
            print("[Info] Calendar opened.")
        except TimeoutException:
            print("[Info] Calendar has already been opened or is not visible.")

    def select_date(self, date_str: str):
        month, day, year = date_str.split('/')

        target_date = f"{day}.{month}.{year}"

        css_selector = f"div[data-testid='calendar-day-{target_date}']"
        date_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_element)
        self.driver.execute_script("arguments[0].click();", date_element)
        print(f"Date chosen: {target_date}")

    def is_disclaimer_visible(self):
        try:
            disclaimer = self.wait.until(EC.visibility_of_element_located(self.disclaimer_text))
            return disclaimer.is_displayed()
        except TimeoutException:
            print("\n[Error] Disclaimer hasn't showed up.")
            return False