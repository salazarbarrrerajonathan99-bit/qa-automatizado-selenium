import pytest
from login_page import LoginPage

@pytest.mark.parametrize("usuario, clave, mensaje_esperado", [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area"),
    ("usuario_incorrecto", "password_incorrecta", "Your username is invalid"),
    ("tomsmith", "clave_mala", "Your password is invalid"),
])
def test_login_variado(driver, usuario, clave, mensaje_esperado):
    login_page = LoginPage(driver)
    login_page.ir_a_la_pagina()
    login_page.hacer_login(usuario, clave)

    assert mensaje_esperado in login_page.obtener_mensaje()