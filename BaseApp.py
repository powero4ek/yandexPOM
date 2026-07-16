from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.base_url = "https://ya.ru/"


    def go_to_site(self):
        self.driver.get(self.base_url)


    def find_element(self, locator, time=10):

        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator))


    def get_current_url(self):

        return self.driver.current_url


    def wait_url_contains(self, text, time=10):

        WebDriverWait(self.driver,time).until(lambda driver: text in driver.current_url)