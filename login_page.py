from selenium.webdriver.common.by import By

class LoginPage:
    # Localizadores, todos juntos y centralizados en un solo lugar
    URL = "https://the-internet.herokuapp.com/login"
    CAMPO_USERNAME = (By.ID, "username")
    CAMPO_PASSWORD = (By.ID, "password")
    BOTON_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    MENSAJE_RESULTADO = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def ir_a_la_pagina(self):
        self.driver.get(self.URL)

    def hacer_login(self, usuario, clave):
        self.driver.find_element(*self.CAMPO_USERNAME).send_keys(usuario)
        self.driver.find_element(*self.CAMPO_PASSWORD).send_keys(clave)
        self.driver.find_element(*self.BOTON_SUBMIT).click()

    def obtener_mensaje(self):
        elemento = self.driver.find_element(*self.MENSAJE_RESULTADO)
        return elemento.text