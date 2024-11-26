import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class QaBookPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_to_cart_btn = "//button[@data-testid='book__addToCartButton']"
    close_modal_window_btn = "//div[@data-testid='modal__close--button']"

    # Getters

    def get_add_to_cart_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_btn)))

    def get_close_modal_window_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.close_modal_window_btn)))

    # Actions
    def click_add_to_cart_btn(self):
        self.get_add_to_cart_btn().click()
        print("Add to cart button was clicked")
        time.sleep(2)

    def click_close_modal_window_btn(self):
        self.get_close_modal_window_btn().click()
        print("Close modal window button was clicked")
        time.sleep(2)

    # Methods

    def switch_to_first_tab(self):
        """Переключиться на первую вкладку."""
        self.driver.switch_to.window(self.driver.window_handles[0])
        print("Switched back to the first tab")
        time.sleep(2)

    def add_to_cart(self):
        self.get_current_url()
        self.click_add_to_cart_btn()
        self.click_close_modal_window_btn()
        self.switch_to_first_tab()