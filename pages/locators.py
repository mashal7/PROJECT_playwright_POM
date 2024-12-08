
class BaseLocators:
    MAIN_PAGE_LINK = 'div.header__column.header__column--logo'          # ссылка на главную страницу
    LOGIN_BUTTON = '.btn.btn--controlMain.btn-auth'                     # кнопка авторизации/личный кабинет
    BOOKS_BUTTON = '.btn.btn--link[href = "/catalog/knigi/"] >> span:has-text("Книги")'  # кнопка для раздела меню "книги"
    CART_BUTTON = '[href="/cart/"]'

class LoginLocators:
    MAIL_INPUT = '[name="phone_or_email"]'                              # ввод почты
    PASSWORD_INPUT = '[name="password"]'                                # ввод пароля
    ENTER_BUTTON = '.btn.btn--primary.btn--height60.btn--fullWidth'     # кнопка входа
    CHECK_AUTH_WORD = '.main__title.title.title--48'                    # слово для проверки успешной авторизации 'Личный кабинет'
    CHECK_WRONG_DATA = '.errorlist'                                     # надпись 'Неверный телефон/почта или пароль.'

class BooksLocators:
    FICTION_SECTION = '[data-id="2884"]'                                # раздел "Художественная литература"
    ALL_BOOKS_SECTIONS = '.nav--catalog .menu > li'                     # все 4 раздела

class FictionLocators:
    locators_types_fiction = [f'//a[@data-id="{i}"]' for i in range(2885, 2898)]
    '.listProperties:first-child > li'                                  # жанры художественной литературы
    FIELD_AUTHOR = '[name="filter[576]"] + input[placeholder="Поиск..."]'   # поле автора в фильтре
    AUTHOR_BOCCACCIO = '[data-ga-label="Боккаччо Д."]'                      # выбор автора Бокаччо
    BOOK_BINDING = '[data-ga-label="Твердая обложка"]'                      # выбор твердой обложки
    BUTTON_APPLY_FILTER = '.btn.btn--primary.btn--fullWidth'                # кнопка "принять фильтр"
    BUTTON_ADD_TO_CART = '.btn--border50.js-add-to-cart[data-id="919581"]'  # кнопка "добавить в корзину"
    CHECK_AUTHOR = '.card__subtitle.hiddenMobile'                           # название автора в каталоге
    CHECK_PRICE = '.price.price--ruble'                                     # цена книги в каталоге

class CartLocators:
    CARD_PRICE = 'span[style="font-size: 16px;"]'                           # цена книги в корзине
    CARD_AUTHOR = '//p["data-v-6c0c2814"][1]'                               # название автора в корзине
    PLACE_ORDER_BUTTON = '.cartBox__buttons [href="/cart/order/"]'          # кнопка "оформить заказ"






