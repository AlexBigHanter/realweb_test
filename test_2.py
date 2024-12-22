from selenium import webdriver
from selenium.webdriver.common.by import By

# пробный тест пробую схватиться по CSS Уже по хорошему отрибуту

# открываем браузер
browser = webdriver.Chrome()
browser.get('https://steamcommunity.com/id/wqseqwedqwedwqe')
tekst = browser.find_element(By.CSS_SELECTOR, "div[id='comment_content_4522261847574915895']")
tekst.text
assert tekst.text == "-REP"