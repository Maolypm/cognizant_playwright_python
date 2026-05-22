from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Definimos los selectores usando los prefijos inteligentes de tu BasePage
        self.url = "https://practice.expandtesting.com/login"
        self.username_input = "label=Username"                  # Usa get_by_label
        self.password_input = "label=Password"                  # Usa get_by_label
        self.login_button = "#submit-login"                     # Usa locator estándar (CSS)
        self.error_message = "text=Your password is invalid!"   # Usa get_by_text

    def navigate(self):
        # 1. Utiliza navigate_to
        self.navigate_to(self.url)
    
    def enter_username(self, username: str):
        # 2. Utiliza fill_input (con el delay de escritura humana de 100ms por defecto)
        self.fill_input(self.username_input, username)

    def enter_password(self, password: str):
        # 3. Utiliza fill_input (con el delay de escritura humana de 100ms por defecto)        
        self.fill_input(self.password_input, password, delay=200)

    def click_submit(self):
        # 4. Utiliza click_element para hacer clic en el botón de login
        self.click_element(self.login_button)

    def validar_login_incorrecto(self) -> str:
        # Espera a que el mensaje de error esté visible
        return self.get_text(self.error_message)