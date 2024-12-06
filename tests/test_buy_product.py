from pages.book_page import BooksPage
from pages.fiction_page import FictionPage
from pages.login_page import LoginPage


def test_buy_product(page):
    """Тест по покупке товара включает в себя:
        авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

    mail, password = 'petrova44as@yandex.ru', 'qwerty123'
    authorization = LoginPage(page)
    authorization.go_to_login_page()
    authorization.log_in(mail, password)
    authorization.is_logged_in()

    books = BooksPage(page)
    books.select_section_of_book('Художественная литература')

    fiction = FictionPage(page)
    fiction.select_section_fiction('Классическая литература')
    page.pause()
    fiction.set_up_filter_author_binding('Боккаччо')
    fiction.add_book_to_cart()

    # cart = CartPage(set_up)
    # expect_author, expect_price = fiction.autor_price_for_checking
    # cart.check_author_price(expect_author, expect_price)

