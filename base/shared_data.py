from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SharedData:
    title_audiobook_page = "//*[@id='book-card__wrapper']/div[2]/div[3]/div[1]/h1"
    title_sda_book_page = "//*[@id='book-card__wrapper']/div[2]/div[3]/div[1]/h1"
    title_qa_book_page = "//*[@id='book-card__wrapper']/div[2]/div[3]/div[1]/h1"

    def __init__(self, driver):
        self.driver = driver

    # Getters
    def get_title_audiobook_page(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.title_audiobook_page)))

    def get_title_sda_book_page(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.title_sda_book_page)))

    def get_title_qa_book_page(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.title_qa_book_page)))
