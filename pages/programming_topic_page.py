import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class ProgrammingTopicPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    text_format_checkbox = "//input[@id='art_types-text_book']"
    chips_text = "//*[@id='main']/div[2]/div[2]/div[2]/div[2]/span/div/div"
    eng_language_checkbox = "//input[@id='languages-en']"
    chips_english = "//*[@id='main']/div[2]/div[2]/div[2]/div[2]/span[2]/div"
    high_rate_switcher = "//*[@id='main']/div[2]/div[2]/div[1]/div[6]/div[1]/div[2]/div"
    chips_high_rate = "//*[@id='main']/div[2]/div[2]/div[2]/div[2]/span[3]/div/div"
    book_1 = "//*[@id='main']/div[2]/div[2]/div[2]/div[4]/div[1]/div[1]/div[10]/div/a"
    catalog_btn = "//button[@data-testid='header-catalog-button']"
    cars_and_sda_topic_link = "//*[@id='genres_popup']/div[1]/div/div/div/div[8]/ul/li[5]/a"
    cars_and_sda_title = "//span[@class='PageHeader_title__text__rrWrd']"

    # Safe click helper
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

    def get_chips_text(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.chips_text))
        )

    def get_eng_language_checkbox(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.eng_language_checkbox))
        )
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.eng_language_checkbox))
        )

    def get_chips_english(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.chips_english))
        )

    def get_high_rate_switcher(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.high_rate_switcher))
        )
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.high_rate_switcher))
        )

    def get_chips_high_rate(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.chips_high_rate))
        )

    def get_book_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.book_1))  # Возвращает первый найденный элемент
        )

    def get_catalog_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_btn)))

    def get_cars_and_sda_topic_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.cars_and_sda_topic_link))  # Возвращает первый найденный элемент
        )

    def get_cars_and_sda_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.cars_and_sda_title))  # Возвращает первый найденный элемент
        )

    # Actions
    def click_text_format_checkbox(self):
        element = self.get_text_format_checkbox()
        self.safe_click(element)
        print("Text format checkbox was checked")
        time.sleep(2)

    def click_eng_language_checkbox(self):
        element = self.get_eng_language_checkbox()
        self.safe_click(element)
        print("English language checkbox was checked")
        time.sleep(2)

    def click_high_rate_switcher(self):
        element = self.get_high_rate_switcher()
        self.safe_click(element)
        print("High rate switcher was switched")
        time.sleep(2)

    def click_book_1(self):
        element = self.get_book_1()
        self.safe_click(element)
        print("Book 1 was clicked")
        time.sleep(2)

    def click_catalog_btn(self):
        self.get_catalog_btn().click()
        print("Catalog button was clicked")
        time.sleep(2)

    def click_cars_and_sda_topic_link(self):
        element = self.get_cars_and_sda_topic_link()
        self.safe_click(element)
        print("Cars and SDA link was clicked")
        time.sleep(2)

    # Methods
    def select_programming_book(self):
        Logger.add_start_step(method="select_programming_book")
        self.get_current_url()

        # Шаг 1: Клик на чекбокс "Text Format"
        self.click_text_format_checkbox()
        self.check_word(self.get_chips_text(), 'Текст')

        # Шаг 2: Клик на чекбокс "English Language"
        self.click_eng_language_checkbox()
        self.check_word(self.get_chips_english(), 'Английский')

        # Шаг 3: Клик на переключатель "High Rate"
        self.click_high_rate_switcher()
        self.check_word(self.get_chips_high_rate(), 'Высокая оценка')

        self.click_book_1()
        self.assert_url('https://www.litres.ru/book/mili-ali/software-testing-concepts-and-operations-33825118/')
        Logger.add_end_step(url=self.driver.current_url, method="select_programming_book")

    def select_sda_book(self):
        Logger.add_start_step(method="select_sda_book")
        self.click_catalog_btn()
        self.click_cars_and_sda_topic_link()
        self.get_current_url()
        self.check_word(self.get_cars_and_sda_title(), 'автомобили и ПДД')
        Logger.add_end_step(url=self.driver.current_url, method="select_sda_book")
