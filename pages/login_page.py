from base.base_class import Base
from pages.locators import LoginLocators
from playwright.sync_api import expect

class LoginPage(Base):
    def __init__(self, page):
        super().__init__(page)

    # ----------------------------Actions----------------------------
    def input_mail(self, mail):
        self._page.locator(LoginLocators.MAIL_INPUT).fill(mail)
        print('Ввод mail')

    def input_password(self, password):
        self._page.locator(LoginLocators.PASSWORD_INPUT).fill(password)
        print('Ввод пароля')

    def click_enter_button(self):
        self._page.locator(LoginLocators.ENTER_BUTTON).click()
        print('Вход в личный кабинет')


# ----------------------------Methods----------------------------
    # авторизация в системе
    def log_in(self, mail, password):
        print('Авторизация в системе')
        print(f'Текущий url: {self._page.url}')

        # ввод данных и вход
        self.input_mail(mail)
        self.input_password(password)
        self.click_enter_button()

    # проверка на успешную авторизацию
    def is_logged_in(self):
        print('Проверка успешной авторизации')
        self.assert_url('https://fkniga.ru/cabinet/')
        self._page.locator(LoginLocators.CHECK_AUTH_WORD)
        print('Авторизация успешно пройдена')


        # проверка на неверный ввод данных пользователя
    def not_logged_in(self):
        print('Проверка авторизации c вводом неверных данных пользователя')
        expect(LoginLocators.CHECK_WRONG_DATA, normalize_whitespace=True).to_contain_text('Неверный телефон/почта или пароль.')
        print('Неверный телефон/почта или пароль')


