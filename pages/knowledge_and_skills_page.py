import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class KnowledgeAndSkillsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    сomputer_literature_topic_link = "//*[@id='main']/div[2]/div[2]/div[1]/div[1]/div[4]/div/div[8]/a"
    page_header = "//span[@class='PageHeader_title__text__rrWrd']"
    programming_topic_link = "//*[@id='main']/div[2]/div[2]/div[1]/div[1]/div[4]/div/div[3]/a"
    programming_link_title = "//span[@class='PageHeader_title__text__rrWrd']"

    # Getters
    def get_сomputer_literature_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.сomputer_literature_topic_link)))

    def get_page_header(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.page_header)))

    def get_programming_topic_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.programming_topic_link)))

    def get_programming_link_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.programming_link_title)))

    # Actions
    def click_сomputer_literature_link(self):
        self.get_сomputer_literature_link().click()
        print("Computer literature link was clicked")
        time.sleep(2)

    def click_programming_topic_link(self):
        self.get_programming_topic_link().click()
        print("Programming topic link was clicked")
        time.sleep(2)

    # Methods
    def select_comp_book(self):
        self.get_current_url()
        self.click_сomputer_literature_link()
        self.check_word(self.get_page_header(), 'компьютерная литература')
        self.click_programming_topic_link()
        self.check_word(self.get_programming_link_title(), 'программирование')
