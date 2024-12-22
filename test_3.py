from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# fixture полная настройка с неявным ожиданием !

# функция откроет и мак.икран +вернят наши дествия return +implicitly_wait(5)
@pytest.fixture()
def open():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()

    yield browser
    browser.quit()

def test_nomer(open):
    open.get("https://realweb.ru")
    coll = open.find_element(By.CSS_SELECTOR, "div[class='t396__elem tn-elem tn-elem__7035698311707407679271']")
    coll.click()
    nomer = open.find_element(By.CSS_SELECTOR, "div[id='sbs-754751996-1707807739270']")
    nomer.text
    assert nomer.text == "+7 (495) 229-01-61"
