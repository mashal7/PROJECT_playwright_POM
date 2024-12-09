import logging

from base.base_class import Base, logger
from pages.locators import LoginLocators
from playwright.sync_api import expect

logger = logging.getLogger(__name__)

class LoginPage(Base):
    def __init__(self, page):
        super().__init__(page)

    # ----------------------------Actions----------------------------
    # ввод логина
    def input_mail(self, mail):
        self._page.locator(LoginLocators.MAIL_INPUT).fill(mail)
        print('Ввод mail')

    # ввод пароля
    def input_password(self, password):
        self._page.locator(LoginLocators.PASSWORD_INPUT).fill(password)
        print('Ввод пароля')

    # нажать кнопку входа
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
        logger.info('Проверка успешной авторизации')
        self.assert_url('https://fkniga.ru/cabinet/')
        try:
            logger.info('Проверка на присутствие заголовка "Личный кабинет"')
            self._page.locator(LoginLocators.CHECK_AUTH_WORD)
        except AssertionError as err:
            logger.error(f'Вход в личный кабинет с верными данными не выполнен. Ошибка проверки: {err}')
            raise
        logger.info('Авторизация успешно пройдена')


    # проверка на неверный ввод данных пользователя
    def not_logged_in(self):
        logger.info('Проверка авторизации c вводом неверных данных пользователя')
        try:
            locator = self._page.locator(LoginLocators.CHECK_WRONG_DATA)
            expect(locator).to_contain_text('Неверный телефон/почта или пароль.')
        except AssertionError as err:
            logger.error(f'Вход в личный кабинет с неверными данными выполнен. Ошибка проверки: {err}')
            raise
        logger.info('Авторизация не выполнена! Данные неверны. Проверка пройдена успешно')



