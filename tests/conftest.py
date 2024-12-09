import pytest
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='test.log',
    filemode='w',
    encoding='utf-8'
)
logger = logging.getLogger(__name__)

# Фикстура для браузера, открывается один раз на всю сессию
@pytest.fixture(scope="session")
def browser():
    logger.info('Запуск Playwright')
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)  # Открываем браузер
    yield browser
    logger.info('Закрытие браузера')
    browser.close()
    playwright.stop()

# Фикстура для страницы, открывается для каждого теста
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()  # Создаем новый контекст
    page = context.new_page()  # Создаем новую страницу
    page.goto('https://fkniga.ru/')
    yield page
    context.close()


