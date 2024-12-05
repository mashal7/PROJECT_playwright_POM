import pytest
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright


# Фикстура для браузера, открывается один раз на всю сессию
@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)  # Открываем браузер
    yield browser
    #browser.close()  # Уберите эту строку, чтобы не закрывать браузер
    #playwright.stop()

# Фикстура для страницы, открывается для каждого теста
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()  # Создаем новый контекст
    page = context.new_page()  # Создаем новую страницу
    page.goto('https://fkniga.ru/')
    yield page
    #context.close()  # Уберите эту строку, чтобы контекст не закрывался


