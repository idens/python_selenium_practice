from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()
    valX = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    valCalc = calc(valX)
    lastBtn = browser.find_element(By.ID, "solve")

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(valCalc)

    lastBtn.click()

finally:
    time.sleep(20)
    browser.quit()
