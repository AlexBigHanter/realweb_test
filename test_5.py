from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# тест кортеджей

@pytest.mark.parametrize(
    'creds',
    [
        ('123@1', 'qwqwfq'),
        ('123@2', 'bhbhbh'),
        ('123@3', 'fdffdf')
    ]
)


def test_login(creds):
    login, passw = creds
    browser = webdriver.Chrome()
    browser.get("https://koto-shef.ru/auth/")
    browser.maximize_window()
    browser.find_element(By.CSS_SELECTOR,  "input[name='email']").send_keys(login)
    browser.find_element(By.CSS_SELECTOR, "input[name='pwd']").send_keys(passw)
    browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    browser.implicitly_wait(5)
    error_texx = browser.find_element(By.CSS_SELECTOR, "p[class='error']").text
    assert error_texx == 'Пользователь с такими данными не найден'
    browser.quit()

