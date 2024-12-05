from playwright.sync_api import expect
from pages.locators import LoginLocators


class Base:
    '''Базовый класс, содержит универсальные методы'''

    def __init__(self, page):
         self._page = page


    def go_to_login_page(self):
        self._page.locator(LoginLocators.LOGIN_BUTTON).click()
        self._page.wait_for_load_state("load")  # Ожидаем завершения загрузки страницы
        expect(self._page).to_have_url('https://fkniga.ru/auth/')
        print('Открыта страница login_page')


    def get_current_url(self):
        '''Метод для возврата url'''

        current_url = self._page.url
        print(f'Текущий url: {current_url}')