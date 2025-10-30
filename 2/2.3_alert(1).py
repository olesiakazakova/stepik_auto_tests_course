import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element("css selector", ".btn.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    # 4. Получить значение x
    x_element = browser.find_element("id", "input_value")
    x = int(x_element.text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    answer_input = browser.find_element("id", "answer")
    answer_input.send_keys(str(y))

    # 7. Нажать кнопку отправки
    submit_button = browser.find_element("css selector", "button[type='submit']")
    submit_button.click()

    # 8. Получить ответ из алерта
    alert = browser.switch_to.alert
    alert_text = alert.text
    print("Число-ответ:", alert_text)
    alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()