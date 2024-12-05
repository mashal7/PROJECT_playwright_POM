from playwright.sync_api import Page
from locators.locators import LoginLocators

class LoginPage:
    def __init__(self, page: Page):
        super().__init__(page)

    username_input = page.get_by_placeholder(LoginLocators.MAIL_INPUT)
    password_input = page.get_by_placeholder(LoginLocators.PASSWORD_INPUT)


    def navigate(self):
        """Открывает страницу логина."""
        self.page.goto('https://zimaev.github.io/pom/')

    def login(self, username: str, password: str):
        """Выполняет вход с заданными учетными данными."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        """Возвращает текст сообщения об ошибке."""
        return self.error_message.inner_text()