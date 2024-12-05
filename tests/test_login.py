import pytest

from pages.login_page import LoginPage


def test_buy_product(page):
    """Тест по покупке товара включает в себя:
        авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

    mail, password = 'petrova44as@yandex.ru', 'qwerty123'
    authorization = LoginPage(page)
