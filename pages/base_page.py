from playwright.sync_api import Page, Locator, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 5000

    def navigate_to(self, url: str):
        # Usamos domcontentloaded para mayor rapidez o networkidle para carga completa
        self.page.goto(url, wait_until="networkidle")
    
    def get_locator(self, selector: str) -> Locator:
        strategies = {
            "text=": self.page.get_by_text,
            "label=": self.page.get_by_label,
            "placeholder=": self.page.get_by_placeholder,
            "role=": self.page.get_by_role,
            "alt=": self.page.get_by_alt_text,
            "title=": self.page.get_by_title,
            "test_id=": self.page.get_by_test_id
        }
        
        found_method = None
        clean_selector = selector

        for prefix, method in strategies.items():
            if selector.startswith(prefix):
                found_method = method
                clean_selector = selector.replace(prefix, "", 1)
                break

        locator = found_method(clean_selector) if found_method else self.page.locator(selector)
        
        # Aseguramos que el elemento sea accionable antes de devolverlo
        locator.wait_for(state="visible", timeout=self.timeout)
        return locator

    def click_element(self, selector: str):
        print(f"Haciendo clic en: {selector}")
        self.get_locator(selector).click()

    def fill_input(self, selector: str, text: str, delay: int = 100):
        # Rellena un input simulando escritura humana.
        # param selector: El selector del elemento.
        # param text: El texto a escribir.
        # param delay: Milisegundos entre cada pulsación de tecla.
        element = self.get_locator(selector)
        element.clear()
        
        # press_sequentially es la forma moderna de simular escritura letra por letra
        print(f"Escribiendo '{text}' en {selector} con delay de {delay}ms")
        element.press_sequentially(text, delay=delay)

    def wait_for_seconds(self, seconds: int):
        # Espera explícita (usar solo si es estrictamente necesario)
        self.page.wait_for_timeout(seconds * 1000)

    def get_text(self, selector: str) -> str:
        # 1. Creamos el locator (Playwright no lo busca en el DOM hasta que interactuamos)
        element = self.get_locator(selector)
        
        # 2. Extraemos el texto (Playwright espera automáticamente a que el elemento aparezca)
        text = element.inner_text()
        
        # 3. Retornamos el texto limpio o un string vacío si es None
        return text.strip() if text else ""
    
    def is_element_displayed(self, selector: str) -> bool:
        # Verifica si el elemento está visible en la página. Devuelve True o False.
        return self.page.locator(selector).is_visible()