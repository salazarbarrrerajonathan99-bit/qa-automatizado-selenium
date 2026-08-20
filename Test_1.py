from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

# Vamos a la página de login de práctica
driver.get("https://the-internet.herokuapp.com/login")

# Buscamos los campos por su atributo "id"
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

# Escribimos las credenciales (son las de prueba del sitio)
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

# Buscamos el botón y hacemos click
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

time.sleep(8)

# Verificamos que el login funcionó
mensaje = driver.find_element(By.ID, "flash").text
print(mensaje)

driver.quit()