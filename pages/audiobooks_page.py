import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class AudiobooksPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    audiobook = "//*[@id='main']/div/div[2]/div[9]/div/div/div/div/div[1]/div/div[1]/a/div/picture/img"

    def safe_click(self, element):
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def slow_scroll_and_load(self, target_xpath, max_scrolls=30):
        """Медленный скроллинг с ожиданием загрузки новых элементов."""
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        scrolls = 0

        while scrolls < max_scrolls:
            # Прокручиваем вниз на 500 пикселей
            self.driver.execute_script("window.scrollBy(0, 600);")
            time.sleep(1)  # Пауза для подгрузки контента

            # Проверяем, появились ли новые элементы
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # Проверяем, если целевой элемент видим
                try:
                    WebDriverWait(self.driver, 2).until(
                        EC.presence_of_element_located((By.XPATH, target_xpath))
                    )
                    print("Element was found")
                    return True
                except Exception:
                    pass  # Элемента пока нет, продолжаем прокрутку

            last_height = new_height
            scrolls += 1

        print("Reached scroll limit. Item not found.")
        return False

    def get_audiobook(self):
        try:
            # Медленный скроллинг, пока не загрузится целевой элемент
            found = self.slow_scroll_and_load(self.audiobook)
            if not found:
                raise Exception("Could not find the item after scrolling.")

            # Убедиться, что элемент кликабелен
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.audiobook))
            )
            print("Item found and available.")
            return element
        except Exception as e:
            print(f"Error while searching for a book: {e}")
            raise

    def click_audiobook(self):
        try:
            element = self.get_audiobook()
            ActionChains(self.driver).move_to_element(element).perform()
            time.sleep(1)  # Пауза для завершения анимации
            self.safe_click(element)
            print("Click to audiobook was successful.")
        except Exception as e:
            print(f"Error while trying to click on audiobook: {e}")

    def select_audiobook(self):
        Logger.add_start_step(method="select_audiobook")
        self.get_current_url()
        self.click_audiobook()
        self.assert_url('https://www.litres.ru/audiobook/vadim-zeland/transerfing-realnosti-stupen-i-ii-iii-iv-v-69461995/')
        Logger.add_end_step(url=self.driver.current_url, method="select_audiobook")
