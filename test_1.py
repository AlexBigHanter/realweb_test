from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# пробный тест пробую схватиться по CSS

# открываем браузер
browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
time.sleep(5)
click_button = browser.find_element(By.CSS_SELECTOR, "a[title='wikt:Викисловарь:Заглавная страница']")
click_button.click()

#проверка текста
tekst = browser.find_element(By.CSS_SELECTOR, "th[style='color:#fff; background:#69c; padding-top:0.5em; padding-bottom:0.5em; text-align:center; font-size:larger;']")
tekst.text
assert tekst.text == "Русский Викисловарь"




