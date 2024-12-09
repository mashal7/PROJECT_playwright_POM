import logging
from pages.locators import BooksLocators
from base.base_class import Base

logger = logging.getLogger(__name__)

class BooksPage(Base):
    """ Класс, содержащий локаторы и методы для страницы Книги"""

    def __init__(self, page):
        super().__init__(page)

    # ----------------------------Actions----------------------------
    # выбор раздела "Художественная литература"
    def click_fiction_section(self):
        self._page.locator(BooksLocators.FICTION_SECTION)
        print('Переход в раздел "Художественная литература"')

    # получение словаря всех разделов книг {название: локатор}
    def get_list_of_sections_of_book(self):
        locators_of_sections = self._page.locator(BooksLocators.ALL_BOOKS_SECTIONS)
        print(locators_of_sections)
        keys = locators_of_sections.all_inner_texts()
        values = [locators_of_sections.nth(i) for i in range(locators_of_sections.count())]
        sections_of_books =  dict(zip(keys, values))
        return sections_of_books

    # ----------------------------Methods----------------------------
    # переход в раздел "Художественная литература"
    def choose_fiction_section(self):
        self.go_to_book_section()
        self.assert_url('https://fkniga.ru/catalog/knigi/')
        self.click_fiction_section()
        self.assert_url('https://fkniga.ru/catalog/hudozhestvennaja-literatura/')

    # универсальный метод: выбор одного из 4 разделов, передача в функцию названия раздела
    def select_section_of_book(self, section):
        self.assert_url('https://fkniga.ru/catalog/knigi/')
        sections_of_books = self.get_list_of_sections_of_book()
        # проверка на существование определенного типа
        try:
            sections_of_books[section].click()
            print(f'Переход в каталог "{section}"')
        except KeyError as err:
            logger.error(f'Такого выбора в каталоге нет: {err}')
        except Exception as err:
            logger.error(f'Произошла ошибка: {err}')
            raise

        self.assert_url('https://fkniga.ru/catalog/hudozhestvennaja-literatura/')


