import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

@pytest.fixture
def driver():
    opciones = Options()

    # Si la variable de entorno CI existe (GitHub la crea automáticamente),
    # corremos Firefox sin ventana visible
    if os.environ.get("CI"):
        opciones.add_argument("--headless")

    nav = webdriver.Firefox(options=opciones)
    yield nav
    nav.quit()