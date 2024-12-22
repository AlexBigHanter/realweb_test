from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# чек-лист номер-59
browser = webdriver.Chrome()
browser.get("https://realweb.ru")
browser.maximize_window()
browser.implicitly_wait(5)
browser.find_element(By.CSS_SELECTOR, "div[class='t396__elem tn-elem tn-elem__7035698311707407911977']").click()
browser.implicitly_wait(5)

# заполняем форму
browser.find_element(By.CSS_SELECTOR, "input[id='input_1247071055600']").send_keys("AlexTest")
browser.find_element(By.CSS_SELECTOR, "input[id='input_1247071055601']").send_keys("ДомTest")
browser.find_element(By.CSS_SELECTOR, "input[id='input_1247071055602']").send_keys("1234test@gmail.com")
browser.find_element(By.CSS_SELECTOR, "input[id='input_1247071055603']").send_keys("9999999999")
browser.find_element(By.CSS_SELECTOR, "input[class='t-radio js-tilda-rule']").click()
# можно заменить на xpath, для устойчевочти
browser.find_element(By.CSS_SELECTOR, "textarea[id='input_1247071055605']").send_keys("test текс")
browser.find_element(By.CSS_SELECTOR, "div[data-input-lid='1247071055609']").click()
browser.find_element(By.CSS_SELECTOR, "div[data-input-lid='1715606258868']").click()
browser.find_element(By.CSS_SELECTOR, "button[data-field='buttontitle']").click()

# проверям текс при успешно вводе данныйх
tekct = browser.find_element(By.LINK_TEXT, 'Спасибо! Данные успешно отправлены.').text
assert tekct == 'Спасибо! Данные успешно отправлены'






