import allure

from pages.book_page import BooksPage
from pages.cart_page import CartPage
from pages.fiction_page import FictionPage
from pages.login_page import LoginPage

@allure.feature('Авторизация')
@allure.title("Тест по покупке товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_buy_product(page):
    """Тест по покупке товара (книга Бокаччо "Декамерон", твердая обложка) включает в себя:
        авторизацию, выбор товара по фильтру, заполнение данных получателя, подтверждение покупки."""

    mail, password = 'petrova44as@yandex.ru', 'qwerty123'
    authorization = LoginPage(page)
    with allure.step('Открыть страницу авторизации'):
        authorization.go_to_login_page()
    with allure.step('Ввести в форму авторизации действительные учетные данные'):
        authorization.log_in(mail, password)
    with allure.step('Проверить, что авторизация прошла успешно'):
        authorization.is_logged_in()
    with allure.step('Перейти в каталог книг'):
        authorization.go_to_book_section()

    books = BooksPage(page)
    with allure.step('Перейти в секцию "Художественная литература"'):
        books.select_section_of_book('Художественная литература')

    fiction = FictionPage(page)
    with allure.step('Перейти в секцию "Классическая литература"'):
        fiction.select_section_fiction('Классическая литература')
    with allure.step('Применить в фильтре автора "Боккаччо" и переплет "Твердая обложка"'):
        fiction.set_up_filter_author_binding('Боккаччо')
    with allure.step('Добавить книгу в корзину'):
        fiction.add_book_to_cart()
    expect_author, expect_price = fiction.autor_price_for_checking
    with allure.step('Перейти в корзину'):
        fiction.go_to_cart_page()

    cart = CartPage(page)
    with allure.step('Проверить, что автор и цена в корзине совпадают с данными в каталоге'):
        cart.check_author_price(expect_author, expect_price)
    with allure.step('Перейти к оформлению товара'):
        cart.go_to_place_order()

