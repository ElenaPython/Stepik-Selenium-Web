from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100, проверять в течение 13 секунд, пока кнопка не станет кликабельной
    element = WebDriverWait(browser, 13).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button = browser.find_element_by_css_selector("button")
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    field = browser.find_element_by_id('answer')
    field.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()