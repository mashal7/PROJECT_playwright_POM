from base.base_class import Base
from pages.locators import CartLocators, BaseLocators


class CartPage(Base):
    """ Класс содержащий локаторы и методы для страницы авторизации"""

    def __init__(self, driver):
        super().__init__(driver)


    #----------------------------Actions----------------------------------
    def click_button_place_order(self):
        self._page.locator(CartLocators.PLACE_ORDER_BUTTON).click()
        print('Нажинаем на "Перейти к оформлению"')


    # ----------------------------Methods----------------------------------

    # Сверка автора и цены в корзине и каталоге
    def check_author_price(self, expect_author, expect_price):
        print('Сверяем автора и цену в каталоге и корзине')
        author = self._page.locator(CartLocators.CARD_AUTHOR)
        price = self._page.locator(CartLocators.CARD_PRICE)
        self.assert_word(author, expect_author)
        print('Автор указан верно')
        self.assert_word(price, expect_price)
        print('Цена указана верно')

    # Переход на страницу оформления заказа
    def go_to_place_order(self):
        self.click_button_place_order()
        self.assert_url('https://fkniga.ru/cart/order/')
        print('Страница оформления заказа верна')

