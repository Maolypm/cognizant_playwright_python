from pages.base_page import BasePage


class SecurePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_exitoso = "text=You logged into a secure area!"  # Usa get_by_text
    
    def validar_login_exitoso(self) -> str:
        # Espera a que el heading de éxito esté visible
        return self.get_text(self.login_exitoso)