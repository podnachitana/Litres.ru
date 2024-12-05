import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login_icon = "//div[@data-testid='tab-login']"
    email = "//input[@id='auth__input--enterEmailOrLogin']"
    continue_btn = "//button[@data-testid='auth__button--continue']"
    password = "//input[@data-testid='auth__input--enterPassword']"
    login_btn = "//button[@data-testid='auth__button--enter']"
    later_btn = "//*[@id='modal']/div[2]/div/div/div/div/div/form/div[3]/button"
    text_logo_profile = "//div[@class='ProfileButton_profileButton__title__GV_yX']"
    catalog_btn = "//button[@data-testid='header-catalog-button']"
    knowledge_and_skills_link = "//*[@id='genres_popup']/div[1]/div/div/div/div[5]/a"

    # Getters
    def get_login_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_icon)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_continue_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))

    def get_later_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.later_btn)))

    def get_text_logo_profile(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.text_logo_profile)))

    def get_catalog_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_btn)))

    def get_knowledge_and_skills_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.knowledge_and_skills_link)))

    # Actions
    def click_login_icon(self):
        self.get_login_icon().click()
        print("Login icon button was clicked")
        time.sleep(2)

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Email was added")
        time.sleep(2)

    def click_continue_btn(self):
        self.get_continue_btn().click()
        print("Continue button was clicked")
        time.sleep(2)

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Password was added")
        time.sleep(2)

    def click_login_btn(self):
        self.get_login_btn().click()
        print("Login button was clicked")
        time.sleep(2)

    def click_later_btn(self):
        self.get_later_btn().click()
        print("Later button was clicked")
        time.sleep(2)

    def click_catalog_btn(self):
        self.get_catalog_btn().click()
        print("Catalog button was clicked")
        time.sleep(2)

    def click_knowledge_and_skills_link(self):
        self.get_knowledge_and_skills_link().click()
        print("Knowledge and skills link was clicked")
        time.sleep(2)

    # Methods
    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.get_current_url()
            self.click_login_icon()
            self.input_email("tatianaterrible@yandex.ru")
            self.click_continue_btn()
            self.input_password("f5wwxgt7")
            self.click_login_btn()
            self.click_later_btn()
            self.check_word(self.get_text_logo_profile(), 'Профиль')
            self.click_catalog_btn()
            self.click_knowledge_and_skills_link()
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
