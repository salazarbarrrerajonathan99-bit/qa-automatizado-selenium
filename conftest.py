import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    nav = webdriver.Firefox()
    yield nav
    nav.quit()