from YandexPages import SearchHelper

def test_yandex_search(browser):

    yandex_main_page = SearchHelper(browser)

    yandex_main_page.go_to_site()

    yandex_main_page.enter_word("Hello")
    print("URL:", browser.current_url)

    yandex_main_page.wait_url_contains("search")

    url = yandex_main_page.get_current_url()

    assert "search" in url
