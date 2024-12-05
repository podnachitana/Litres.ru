import pytest
import allure

from pages.audiobook_page import AudiobookPage
from pages.audiobooks_page import AudiobooksPage
from pages.qa_book_page import QaBookPage
from pages.cars_and_sda_page import CarsAndSdaPage
from pages.cart_page import CartPage
from pages.knowledge_and_skills_page import KnowledgeAndSkillsPage
from pages.main_page import MainPage
from pages.programming_topic_page import ProgrammingTopicPage
from pages.sda_book_page import SdaBookPage


@pytest.fixture(scope='session')
@allure.description("Authorization")
def authorized_driver(set_up):
    driver = set_up
    main_page = MainPage(driver)
    main_page.authorization()
    yield driver
    driver.quit()


@pytest.mark.run(order=1)
@allure.description("Select QA book")
def test_select_qa_book(authorized_driver):
    driver = authorized_driver
    kasp = KnowledgeAndSkillsPage(driver)
    kasp.select_comp_book()

    prog_book_p = ProgrammingTopicPage(driver)
    prog_book_p.select_programming_book()

    book_1 = QaBookPage(driver)
    book_1.add_to_cart()


@pytest.mark.run(order=2)
@allure.description("Select SDA book")
def test_select_sda_book(authorized_driver):
    driver = authorized_driver
    prog_book_p = ProgrammingTopicPage(driver)
    prog_book_p.select_sda_book()

    cars_sda_page = CarsAndSdaPage(driver)
    cars_sda_page.select_sda_book()

    sda_book_page = SdaBookPage(driver)
    sda_book_page.add_to_cart()


@pytest.mark.run(order=3)
@allure.description("Select audiobook")
def test_select_audiobook(authorized_driver):
    driver = authorized_driver
    cars_sda_page = CarsAndSdaPage(driver)
    cars_sda_page.select_audiobook()

    audiobooks = AudiobooksPage(driver)
    audiobooks.select_audiobook()

    audiobook = AudiobookPage(driver)
    audiobook.add_to_cart()


@pytest.mark.run(order=4)
@allure.description("Check and verify cart contents")
def test_verify_cart_contents(authorized_driver):
    driver = authorized_driver
    cart = CartPage(driver)
    cart.checking_books()
    cart.checking_prices()
    cart.delete_books_from_cart()
