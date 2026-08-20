from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_login_exitoso(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # En vez de time.sleep(2), esperamos a que el elemento "flash" exista
    wait = WebDriverWait(driver, 10)
    mensaje_elemento = wait.until(EC.visibility_of_element_located((By.ID, "flash")))

    assert "You logged into a secure area" in mensaje_elemento.text


def test_login_fallido(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("usuario_incorrecto")
    driver.find_element(By.ID, "password").send_keys("password_incorrecta")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait = WebDriverWait(driver, 10)
    mensaje_elemento = wait.until(EC.visibility_of_element_located((By.ID, "flash")))

    assert "Your username is invalid" in mensaje_elemento.text



def test_dropdown(driver):
        driver.get("https://the-internet.herokuapp.com/dropdown")

        # Encontramos el <select> y lo "envolvemos" con Select para poder manejarlo
        elemento_dropdown = driver.find_element(By.ID, "dropdown")
        select = Select(elemento_dropdown)

        # Elegimos "Option 1" por su texto visible
        select.select_by_visible_text("Option 1")

        # Verificamos que la opción seleccionada sea la correcta
        opcion_actual = select.first_selected_option
        assert opcion_actual.text == "Option 1"

        # Cambiamos a la otra opción, por su value en vez de por texto
        select.select_by_value("2")
        opcion_actual = select.first_selected_option
        assert opcion_actual.text == "Option 2"


def test_radio_buttons(driver):
    driver.get("https://demoqa.com/radio-button")

    # Localizamos los 3 radio buttons
    radio_yes = driver.find_element(By.ID, "yesRadio")
    radio_impressive = driver.find_element(By.ID, "impressiveRadio")
    radio_no = driver.find_element(By.ID, "noRadio")

    # Verificamos que arrancan todos sin marcar
    assert radio_yes.is_selected() == False
    assert radio_impressive.is_selected() == False

    # Hacemos click en "Yes"
    radio_yes.click()
    assert radio_yes.is_selected() == True

    # Cambiamos a "Impressive" (al ser radio buttons, "Yes" se desmarca solo)
    radio_impressive.click()
    assert radio_impressive.is_selected() == True
    assert radio_yes.is_selected() == False   # "Yes" ya no está marcado

    # Verificamos que "No" está deshabilitado y no se puede clickear
    assert radio_no.is_enabled() == False

def test_alert_simple(driver):
    driver.get("https://demoqa.com/alerts")

    boton = driver.find_element(By.ID, "alertButton")
    boton.click()

    # Esperamos a que el alert exista antes de tocarlo
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())

    # "Cambiamos el foco" de Selenium hacia el alert
    alert = driver.switch_to.alert

    # Leemos el texto que muestra
    texto_alert = alert.text
    assert "You clicked a button" in texto_alert

    # Aceptamos el alert (equivale a clickear "OK")
    alert.accept()


def test_alert_confirm(driver):
    driver.get("https://demoqa.com/alerts")

    boton = driver.find_element(By.ID, "confirmButton")
    boton.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    assert "Do you confirm action?" in alert.text

    # Esta vez CANCELAMOS en vez de aceptar
    alert.dismiss()

    # El sitio muestra un texto distinto según elijas OK o Cancel.
    # Verificamos que efectivamente detectó que elegiste "Cancel"
    resultado = driver.find_element(By.ID, "confirmResult").text
    assert "Cancel" in resultado


def test_alert_prompt(driver):
    driver.get("https://demoqa.com/alerts")

    boton = driver.find_element(By.ID, "promtButton")
    boton.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    assert "Please enter your name" in alert.text

    # Escribimos texto DENTRO del prompt, antes de aceptar
    alert.send_keys("Estudiante QA")
    alert.accept()

    # Verificamos que la página muestre el texto que escribimos
    resultado = driver.find_element(By.ID, "promptResult").text
    assert "Estudiante QA" in resultado


def test_tabla(driver):
    driver.get("https://demoqa.com/webtables")

    # Buscamos TODAS las filas del cuerpo de la tabla (tbody), no del encabezado
    filas = driver.find_elements(By.CSS_SELECTOR, "tbody tr")

    # Verificamos que haya exactamente 3 filas (como viste en pantalla)
    assert len(filas) == 3

    # Recorremos cada fila con un for, para revisar sus celdas
    for fila in filas:
        celdas = fila.find_elements(By.TAG_NAME, "td")
        nombre = celdas[0].text
        apellido = celdas[1].text
        print(f"{nombre} {apellido}")

    # Verificamos que "Cierra" aparezca en la primera fila
    primera_fila = filas[0]
    celdas_primera_fila = primera_fila.find_elements(By.TAG_NAME, "td")
    assert celdas_primera_fila[0].text == "Cierra"
    assert celdas_primera_fila[1].text == "Vega"