from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Definimos los selectores usando los prefijos inteligentes de tu BasePage
        self.url = "https://ejemplo-automation.com/login"
        self.username_input = "placeholder=Nombre de usuario" # Usa get_by_placeholder
        self.password_input = "label=Contraseña"              # Usa get_by_label
        self.login_button = "text=Iniciar Sesión"            # Usa get_by_text
        self.error_message = ".alert-danger"                 # Usa locator estándar (CSS)

    def login_con_exito(self, usuario, contrasenia):
        # Simula un login completo usando todos los métodos de la BasePage.
        # 1. Utiliza navigate_to
        self.navigate_to(self.url)

        # 2. Utiliza fill_input (con el delay de escritura humana de 100ms por defecto)
        self.fill_input(self.username_input, usuario)
        
        # También podemos aumentar el delay para la contraseña si queremos ser más lentos
        self.fill_input(self.password_input, contrasenia, delay=200)

        # 3. Utiliza click_element
        self.click_element(self.login_button)

    def obtener_error(self):
        # Ejemplo de uso de get_locator para validaciones.
        # 4. Utiliza get_locator para obtener el texto y validar
        return self.get_locator(self.error_message).inner_text()