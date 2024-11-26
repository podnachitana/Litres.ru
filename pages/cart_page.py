import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    title_qa_book_cart = "//*[@id='main']/div/div/div[2]/div/div[2]/div[3]/h3/a"
    title_sda_book_cart = "//*[@id='main']/div/div/div[2]/div/div[2]/div[2]/h3/a"
    title_audiobook_cart = "//*[@id='main']/div/div/div[2]/div/div[2]/div[1]/h3/a"

    price_qa_book_cart = "//*[@id='main']/div/div/div[2]/div/div[2]/div[3]/div[4]/strong"
    price_sda_book_cart = "//*[@id='main']/div/div/div[2]/div/div[2]/div[2]/div[4]/strong"
    price_audiobook_cart = "//*[@id='main']/div/div/div[2]/div/div[2]/div[1]/div[4]/strong"

    title_qa_book_page = "Software Testing. Concepts and Operations"
    title_sda_book_page = "За рулем без страха и сомнений"
    title_audiobook_page = "Трансерфинг реальности. Ступени I, II, III, IV, V"

    price_qa_book_page = 13540.05
    price_sda_book_page = 399
    price_audiobook_page = 1399

    # Getters
    def get_title_qa_book_cart(self):
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, self.title_qa_book_cart)))

    def get_title_sda_book_cart(self):
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, self.title_sda_book_cart)))

    def get_title_audiobook_cart(self):
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, self.title_audiobook_cart)))

    def get_price_qa_book_cart(self):
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, self.price_qa_book_cart)))

    def get_price_sda_book_cart(self):
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, self.price_sda_book_cart)))

    def get_price_audiobook_cart(self):
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, self.price_audiobook_cart)))

    # Actions

    # Methods
    def checking_books(self):
        self.get_current_url()

        # Check QA book
        qa_element = self.get_title_qa_book_cart()
        expected_qa_book_text = self.title_qa_book_page

        try:
            self.verify_text(qa_element, expected_qa_book_text)
        except Exception as e:
            print(f"QA book verification error: {e}")

        # Check SDA book
        sda_element = self.get_title_sda_book_cart()
        expected_sda_book_text = self.title_sda_book_page

        try:
            self.verify_text(sda_element, expected_sda_book_text)
        except Exception as e:
            print(f"SDA book verification error: {e}")

        # Check Audiobook
        audio_element = self.get_title_audiobook_cart()
        expected_audiobook_text = self.title_audiobook_page

        try:
            self.verify_text(audio_element, expected_audiobook_text)
        except Exception as e:
            print(f"Audiobook verification error: {e}")

    def checking_prices(self):
        qa_price = self.get_price_qa_book_cart()
        expected_qa_price = self.price_qa_book_page
        self.check_price(qa_price, expected_qa_price)

        sda_price = self.get_price_sda_book_cart()
        expected_sda_price = self.price_sda_book_page
        self.check_price(sda_price, expected_sda_price)

        audio_price = self.get_price_audiobook_cart()
        expected_audio_price = self.price_audiobook_page
        self.check_price(audio_price, expected_audio_price)

        qa_price_text = qa_price.text.replace('₽', '').replace(' ', '').replace(',', '.').strip()
        sda_price_text = sda_price.text.replace('₽', '').replace(' ', '').replace(',', '.').strip()
        audio_price_text = audio_price.text.replace('₽', '').replace(' ', '').replace(',', '.').strip()

        try:
            qa_price = float(qa_price_text)
            sda_price = float(sda_price_text)
            audio_price = float(audio_price_text)
        except ValueError as e:
            raise ValueError(f"Could not convert one of the lines to a number: {e}")

        # Рассчитываем общую сумму
        total_sum = qa_price + sda_price + audio_price
        expected_total_sum = 15338.05

        # Проверяем равенство сумм
        assert total_sum == expected_total_sum, f"The sum in the cart doesn't match the expected: expected {expected_total_sum}, got {total_sum}"
        print("Total sum in the cart matches the expected")
