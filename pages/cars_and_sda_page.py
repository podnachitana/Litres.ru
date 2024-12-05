import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class CarsAndSdaPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    text_format_checkbox = "//input[@id='art_types-text_book']"
    text_chips = "//*[@id='main']/div[2]/div[2]/div[2]/div[2]/span/div/div"
    russian_lang_checkbox = "//*[@id='main']/div[2]/div[2]/div[1]/div[5]/div[2]/div/div/div[1]/div/label/div"
    russian_lang_chips = "//*[@id='main']/div[2]/div[2]/div[2]/div[2]/span[2]/div"
    sda_book = "//p[contains(text(), 'Поехали! Все, что нужно знать')]"
    audiobooks_link = "//*[@id='lowerMenuWrap']/nav/div/a[6]"
    audiobooks_title = "//h1[@class='DashboardHeader_title__Gqfs1']"

    def safe_click(self, element):
        """Выполняет клик через Selenium или JavaScript в случае перехвата клика."""
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    # Getters
    def get_text_format_checkbox(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.text_format_checkbox))
        )
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.text_format_checkbox))
        )

    def get_text_chips(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.text_chips))
        )

    def get_russian_lang_checkbox(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.russian_lang_checkbox))
        )
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.russian_lang_checkbox))
        )

    def get_russian_lang_chips(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.russian_lang_chips))
        )

    def get_sda_book(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.sda_book))
        )

    def get_audiobooks_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.audiobooks_link)))

    def get_audiobooks_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.audiobooks_title))
        )

    # Actions
    def click_text_format_checkbox(self):
        element = self.get_text_format_checkbox()
        self.safe_click(element)
        print("Text format checkbox was checked")
        time.sleep(2)

    def click_russian_lang_checkbox(self):
        element = self.get_russian_lang_checkbox()
        self.safe_click(element)
        print("Russian language checkbox was checked")
        time.sleep(2)

    def click_sda_book(self):
        element = self.get_sda_book()
        self.safe_click(element)
        print("SDA Book was clicked")
        time.sleep(2)

    def click_audiobooks_link(self):
        self.get_audiobooks_link().click()
        print("Audiobooks link was clicked")
        time.sleep(2)

    # Methods
    def select_sda_book(self):
        with allure.step("Select SDA book"):
            Logger.add_start_step(method="select_sda_book")
            self.get_current_url()

            self.click_text_format_checkbox()
            self.check_word(self.get_text_chips(), 'Текст')

            self.click_russian_lang_checkbox()
            self.check_word(self.get_russian_lang_chips(), 'Русский')

            self.click_sda_book()
            self.assert_url('https://www.litres.ru/book/sergey-moryahin/poehali-vse-chto-nuzhno-znat-nachinauschim-voditelyam-68624554/')
            Logger.add_end_step(url=self.driver.current_url, method="select_sda_book")

    def select_audiobook(self):
        with allure.step("Select Audiobook"):
            Logger.add_start_step(method="select_audiobook")
            self.click_audiobooks_link()
            self.get_current_url()
            self.check_word(self.get_audiobooks_title(), 'Аудиокниги')
            Logger.add_end_step(url=self.driver.current_url, method="select_audiobook")
