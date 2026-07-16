from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class YandexSearchLocators:

    LOCATOR_YANDEX_SEARCH_FIELD = (By.NAME,"text")


class SearchHelper(BasePage):


    def enter_word(self, word):

        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)

        search_field.click()

        search_field.clear()

        search_field.send_keys(word)

        time.sleep(1)

        search_field.send_keys(Keys.ENTER)