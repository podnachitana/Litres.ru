import datetime
import time


class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(get_url)

    """Method check word"""
    def check_word(self, elements, word):
        """Проверяет, что хотя бы один элемент содержит заданное слово."""
        if not isinstance(elements, list):  # Если это одиночный элемент, преобразуем в список
            elements = [elements]
        texts = [element.text for element in elements]
        assert any(word in text for text in texts), f"None of the {texts} contain '{word}'"
        print(f"{word} word was found")

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('/Users/tatianazudina/PycharmProjects/Litres.ru/screen/' + name_screenshot)

    """Method assert URL"""
    def assert_url(self, result):
        # Переключаемся на последнюю вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])
        get_url = self.driver.current_url
        assert get_url == result, f"Expected URL '{result}', but got '{get_url}'"
        print("URL is good")

    """Compare text"""

    def verify_text(self, element, expected_text):
        actual_text = element.text.strip()
        assert actual_text == expected_text, f"Error: expected '{expected_text}' but received '{actual_text}'"
        print("Test passed successfully: text matches")

    """Method assert price"""

    """Method assert price"""

    """Method assert price"""

    def check_price(self, price_page_element, expected_price):
        # Получаем текст из WebElement и удаляем пробелы, символы валюты, запятые и другие нежелательные символы
        price_text = price_page_element.text.replace('₽', '').replace(' ', '').replace(',', '.').strip()

        # Преобразуем строку в float
        try:
            actual_price = float(price_text)
        except ValueError:
            raise ValueError(f"Не удалось преобразовать строку '{price_text}' в число.")

        # Проверяем равенство цен
        assert actual_price == expected_price, f"Prices are not equal: expected {expected_price}, got {actual_price}"
        print("Prices are equal")

    """Сonversion of numbers into float"""
    def check_total_sum(self):
        # Получаем текст цен из элементов и преобразуем их в float
        qa_price_text = self.get_price_qa_book_cart().text.replace('₽', '').replace(' ', '').replace(',', '.').strip()
        sda_price_text = self.get_price_sda_book_cart().text.replace('₽', '').replace(' ', '').replace(',', '.').strip()
        audio_price_text = self.get_price_audiobook_cart().text.replace('₽', '').replace(' ', '').replace(',',
                                                                                                          '.').strip()

        try:
            qa_price = float(qa_price_text)
            sda_price = float(sda_price_text)
            audio_price = float(audio_price_text)
        except ValueError as e:
            raise ValueError(f"Не удалось преобразовать одну из строк в число: {e}")

        # Рассчитываем общую сумму
        total_sum = qa_price + sda_price + audio_price
        expected_total_sum = 15338.05

        # Проверяем равенство сумм
        assert total_sum == expected_total_sum, f"Сумма в корзине не совпадает с ожидаемой: expected {expected_total_sum}, got {total_sum}"
        print("Сумма в корзине совпадает с ожидаемой")
