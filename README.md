# QA Automatizado con Selenium + Pytest

Suite de pruebas automatizadas end-to-end para aplicaciones web, construida con **Selenium WebDriver** y **Pytest**, con integración continua (CI) mediante **GitHub Actions**.

## ✅ Qué cubre este proyecto

- Automatización de formularios de login (casos exitosos y fallidos)
- Manejo de **checkboxes**, **radio buttons** y **dropdowns**
- Manejo de las 3 variantes de **alerts de JavaScript** (simple, confirm, prompt)
- Lectura y validación de **tablas HTML**
- **Waits explícitos** (`WebDriverWait`) en vez de esperas fijas
- **Page Object Model (POM)** para separar localizadores de la lógica de los tests
- Tests parametrizados con `@pytest.mark.parametrize`
- Fixture compartida vía `conftest.py`
- **Reportes HTML** con `pytest-html`
- **CI/CD**: los tests corren automáticamente en cada `git push`, en modo headless

## 🛠️ Stack técnico

- Python 3.12
- Selenium WebDriver
- Pytest
- pytest-html
- GitHub Actions

## 📁 Estructura del proyecto

```
├── .github/workflows/tests.yml   # Configuración de CI
├── conftest.py                    # Fixture compartida (driver headless en CI)
├── login_page.py                  # Page Object de la página de login
├── test_login.py                  # Tests: login, dropdown, radios, alerts, tabla
├── test_login_pom.py              # Tests usando Page Object Model
├── test_login_parametrizado.py    # Mismo test, múltiples casos de datos
└── .gitignore
```

## ▶️ Cómo correrlo localmente

```bash
# Instalar dependencias
pip install selenium pytest pytest-html

# Correr todos los tests con reporte HTML
pytest test_login.py --html=reporte.html --self-contained-html
```

## 🔄 Integración continua

Cada `push` a la rama `main` dispara automáticamente:
1. Instalación de Python, Firefox y geckodriver
2. Instalación de dependencias
3. Ejecución de la suite completa en modo headless
4. Generación de reporte HTML

Ver el estado de las corridas en la pestaña [Actions](../../actions) del repositorio.

## 📚 Sitios usados para pruebas

- [the-internet.herokuapp.com](https://the-internet.herokuapp.com/) — login, dropdown, alerts
- [demoqa.com](https://demoqa.com/) — radio buttons, alerts, tablas

---

Proyecto construido como parte de mi aprendizaje en QA Automation.