from playwright.sync_api import expect
from pages.locators import LoginLocators, BaseLocators


class Base:
    '''Базовый класс, содержит универсальные методы'''

    def __init__(self, page):
         self._page = page


    def go_to_login_page(self):
        self._page.locator(BaseLocators.LOGIN_BUTTON).click()
        self._page.wait_for_load_state("load")  # Ожидаем завершения загрузки страницы
        self.assert_url('https://fkniga.ru/auth/')
        print('Открыта страница login_page')

    def go_to_book_section(self):
        self._page.locator(BaseLocators.BOOKS_BUTTON).click()
        self._page.wait_for_load_state("load")  # Ожидаем завершения загрузки страницы
        expect(self._page).to_have_url('https://fkniga.ru/catalog/knigi/')
        print('Открыта страница book_page')

    # метод для возврата url
    def get_current_url(self):
        print(f'Текущий url: {self._page.url}')


    # Метод для проверки url
    def assert_url(self, expect_url):
        print('Проверка на коректный url')
        self.get_current_url()
        expect(self._page).to_have_url(expect_url)
        print('Url верный. Проверка пройдена успешно')