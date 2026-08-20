from login_page import LoginPage

def test_login_exitoso_pom(driver):
    login_page = LoginPage(driver)
    login_page.ir_a_la_pagina()
    login_page.hacer_login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area" in login_page.obtener_mensaje()

def test_login_fallido_pom(driver):
    login_page = LoginPage(driver)
    login_page.ir_a_la_pagina()
    login_page.hacer_login("usuario_incorrecto", "password_incorrecto")

    assert "Your username is invalid" in login_page.obtener_mensaje()