import pytest
import time
from pages.login_page import LoginPage


def test_buy_product(page):
    """Тест по покупке товара включает в себя:
        авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

    mail, password = 'petrova44as@yandex.ru', 'qwerty123'
    authorization = LoginPage(page)
    authorization.go_to_login_page()
    authorization.log_in(mail, password)
    authorization.is_logged_in()
    time.sleep()
