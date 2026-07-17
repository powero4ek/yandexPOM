from YandexPages import SearchHelper

def test_yandex_search(browser):

    yandex_main_page.enter_word("Hello")

    yandex_main_page.click_search_button()

    yandex_main_page.wait_url_contains("search")

    url = yandex_main_page.get_current_url()

    assert "search" in url
