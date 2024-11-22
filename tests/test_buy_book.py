from pages.main_page import MainPage


def test_buy_book(set_up):
    driver = set_up

    main_page = MainPage(driver)
    main_page.authorization()
