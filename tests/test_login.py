import allure
from pages.login_page import LoginPage

@allure.feature('Авторизация')
@allure.title("Тест на авторизацию с верными данными")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_with_correct_data(page):
    """Тест на авторизацию с верными данными"""

    mail, password = 'petrova44as@yandex.ru', 'qwerty123'
    authorization = LoginPage(page)
    with allure.step('Открыть страницу авторизации'):
        authorization.go_to_login_page()
    with allure.step('Ввести в форму авторизации действительные учетные данные'):
        authorization.log_in(mail, password)
    with allure.step('Проверить, что авторизация прошла успешно'):
        authorization.is_logged_in()

@allure.feature('Авторизация')
@allure.title("Тест на авторизацию с неверными данными")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_with_wrong_data(page):
    """Тест на авторизацию с неверными данными. Должен упасть"""

    mail, password = 'petrova44as@yandex.ru', 'qwerty111111'
    authorization = LoginPage(page)
    with allure.step('Открыть страницу авторизации'):
        authorization.go_to_login_page()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        authorization.log_in(mail, password)
    with allure.step('Проверить, что авторизация не прошла'):
        authorization.not_logged_in()


