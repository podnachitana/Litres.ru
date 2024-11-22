import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(get_url)

    """Method check word"""
    def check_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Word was found")

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('/Users/tatianazudina/PycharmProjects/Mie.ru/screen/' + name_screenshot)

    """Method assert URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL is good")
