# tests/ui/test_cart_checkout.py
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_add_to_cart_and_badge(driver, base_url):
    login = LoginPage(driver)
    login.load(base_url)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    assert products.is_loaded()
    products.add_first_product_to_cart()
    # validar que el badge del carrito ahora tenga '1'
    badge = driver.find_element(*ProductsPage.CART_BADGE)
    assert badge.text == "1"
