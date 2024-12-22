from selenium import webdriver
from selenium.webdriver.common.by import By
# импортировали явные ожидание
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# тест проверка явных ожидайни + тест ждём 5 сек. пока появится номер (тест демонстрация кода а не функцианала)
browser = webdriver.Chrome()
browser.get("https://realweb.ru")
browser.maximize_window()

knopka = browser.find_element(By.CSS_SELECTOR, "div[class='t396__elem tn-elem tn-elem__7035698311707407679271']")
knopka.click()

# ищем номер + ждем его и проверяем с ОР
nomer = browser.find_element(By.CSS_SELECTOR, "div[id='sbs-754751996-1707807739270']")
wait = WebDriverWait(browser, 5)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='sbs-754751996-1707807739270']")))
nomer.text
assert nomer.text == "+7 (495) 229-01-61"
