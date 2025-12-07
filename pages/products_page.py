# pages/products_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductsPage(BasePage):
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn_inventory")

    def is_loaded(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEM)) > 0

    def add_first_product_to_cart(self):
        btns = self.driver.find_elements(*self.ADD_TO_CART_BTN)
        if btns:
            btns[0].click()
