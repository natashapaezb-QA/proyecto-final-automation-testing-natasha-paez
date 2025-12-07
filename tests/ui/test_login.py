# tests/ui/test_login.py
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.mark.parametrize("username,password,should_pass", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("invalid_user", "wrong_pass", False),
])
def test_login_flow(driver, base_url, username, password, should_pass):
    login = LoginPage(driver)
    login.load(base_url)
    login.login(username, password)

    products = ProductsPage(driver)
    if should_pass:
        assert products.is_loaded(), "La página de productos no se cargó después de login válido"
    else:
        # assert que aparece mensaje de error
        assert "Epic sadface" in login.get_error()
