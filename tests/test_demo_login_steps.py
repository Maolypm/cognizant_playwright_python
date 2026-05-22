import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect

# Importamos tus Page Objects basados en tu arquitectura
from pages.common.login_page import LoginPage
from pages.secure_page import SecurePage

scenarios('../features/demo_login.feature')

# --- FIXTURES PARA INSTANCIAR TUS CLASES ---
# Pytest creará una instancia fresca de cada página por cada test que las use

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def secure_page(page: Page) -> SecurePage:
    return SecurePage(page)


# --- STEP DEFINITIONS ---

@given('the user opens the login page')
def open_login_page(login_page: LoginPage):
    # Tu clase login_page maneja su propia URL interna
    login_page.navigate() 

@when(parsers.parse('the user types username "{username}" into Username field'))
def type_username(login_page: LoginPage, username: str):
    # Delegamos la interacción al método de la clase
    login_page.enter_username(username)

@when(parsers.parse('the user types password "{password}" into Password field'))
def type_password(login_page: LoginPage, password: str):
    login_page.enter_password(password)

@when('pushes Submit button')
def push_submit(login_page: LoginPage):
    login_page.click_submit()

@then(parsers.parse('the new page should contain expected text "{text}"'))
def verify_success_text(secure_page: SecurePage, text: str):
    # Como ya se inició sesión, interactuamos con la SecurePage para validar el texto de éxito
    success_message = secure_page.validar_login_exitoso()
    assert(text in success_message), f"Expected '{text}', but got '{success_message}'"

@then(parsers.parse('the error message text should be "{expected_error_text}"'))
def verify_error_text(login_page: LoginPage, expected_error_text: str):
    error_message = login_page.validar_login_incorrecto()
    assert(expected_error_text in error_message), f"Expected '{expected_error_text}', but got '{error_message}'"