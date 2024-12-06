
class BaseLocators:
    LOGIN_BUTTON = '.btn.btn--controlMain.btn-auth'  # кнопка авторизации/личный кабинет
    BOOKS_BUTTON = '.btn.btn--link[href = "/catalog/knigi/"] >> span:has-text("Книги")'  # кнопка для раздела меню "книги"


class LoginLocators:
    MAIL_INPUT = '[name="phone_or_email"]'                            # ввод почты
    PASSWORD_INPUT = '[name="password"]'                              # ввод пароля
    ENTER_BUTTON = '.btn.btn--primary.btn--height60.btn--fullWidth'    # кнопка входа
    CHECK_AUTH_WORD = '.main__title.title.title--48'               # слово для проверки успешной авторизации 'Личный кабинет'
    CHECK_WRONG_DATA = '.errorlist'                              # надпись 'Неверный телефон/почта или пароль.'

class BooksLocators:
    FICTION_SECTION = '[data-id="2884"]'                        # раздел "Художественная литература"
    ALL_BOOKS_SECTIONS = '.nav--catalog .menu > li'             # все 4 раздела

class FictionLocators:
    locators_types_fiction = [f'//a[@data-id="{i}"]' for i in range(2885, 2898)]
    '.listProperties:first-child > li'
    # жанры художественной литературы
    FIELD_AUTHOR = '[@name="filter[576]"]/following-sibling::input[@placeholder="Поиск..."]'
    AUTHOR_BOCCACCIO = '[@data-ga-label="Боккаччо Д."]'
    BOOK_BINDING = '[@data-ga-label="Твердая обложка"]'
    BUTTON_APPLY_FILTER = '.btn.btn--primary.btn--fullWidth'
    BUTTON_ADD_TO_CART = '.class="btn.btn--border50.js-add-to-cart'
    CHECK_AUTHOR = '.card__subtitle.hiddenMobile'
    CHECK_PRICE = '.price.price--ruble'






