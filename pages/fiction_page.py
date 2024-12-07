from base.base_class import Base
from pages.locators import FictionLocators


class FictionPage(Base):
    """ Класс содержащий локаторы и методы для страницы книги, подтип - Художественная литература"""

    def __init__(self, driver):
        super().__init__(driver)


    #---------------------------------Actions----------------------------------------------

    # получение словаря всех разделов книг {название: локатор}
    @property
    def list_of_sections_of_fiction(self):
        d = {}
        for locator in FictionLocators.locators_types_fiction:
            section = self._page.locator(locator)
            d[section.inner_text().rsplit(' ', 1)[0]] = section
        return d

    def input_author(self, author):
        self._page.locator(FictionLocators.FIELD_AUTHOR).fill(author)
        print(f'Пишем в фильтре автора {author}')

    def click_specific_author(self):
        self._page.locator(FictionLocators.AUTHOR_BOCCACCIO).click()
        print('Выбираем фильтр с нужным автором')

    def click_book_binding(self):
        self._page.locator(FictionLocators.BOOK_BINDING).click()
        print('Выбираем фильтр, где переплетом книги является "Твердая обложка"')

    def click_button_apply_filter(self):
        self._page.locator(FictionLocators.BUTTON_APPLY_FILTER).click()
        print('Подтверждаем фильтр')

    def click_button_add_to_cart(self):
        self._page.locator(FictionLocators.BUTTON_ADD_TO_CART).click()
        print('Кладем книгу в корзину')


    # -----------------------------Methods---------------------------
    # выбор типа литературы
    def select_section_fiction(self, section):
        self.get_current_url()
        sections_fiction = self.list_of_sections_of_fiction
        print(sections_fiction)
        try:
            sections_fiction[section].click()
            print(f'Переход в каталог "{section}"')
        except KeyError:
            print('Такого выбора в каталоге нет')
        except Exception as err:
            print(f'Произошла ошибка: {err}')

    # Настройка фильтра 'автор' и 'обложка', проверка
    def set_up_filter_author_binding(self, author):
        print(f'Установка фильтра книг с автором {author}')
        self.input_author(author)
        self.click_specific_author()
        print(f'Установка фильтра книг с твёрдой обложкой')
        self.click_book_binding()
        self.click_button_apply_filter()
        self.assert_url('https://fkniga.ru/catalog/klassicheskaja-proza/?filter%5B576%5D=43228&filter%5B578%5D=40368')
        print('Фильтр применен успешно')


    # добавление книги в корзину
    def add_book_to_cart(self):
        self.click_button_add_to_cart()
        print('Книга в корзине')

    # возврат названия и цены для сверки с корзиной
    @property
    def autor_price_for_checking(self):
        author = self._page.locator(FictionLocators.CHECK_AUTHOR, has_text="Боккаччо Д.")
        author_text = author.inner_text().split(' ', 1)[1]
        price = self._page.locator(FictionLocators.CHECK_PRICE).first
        price_text = price.inner_text()
        print(author_text, price_text)
        return author_text, price_text



