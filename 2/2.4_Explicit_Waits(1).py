import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    # 2. Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # 3. Получить значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)

    # 4. Вычислить функцию
    def calc(x):
        return math.log(abs(12 * math.sin(x)))

    y = calc(x)

    # 5. Ввести ответ в поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(str(y))

    # 6. Нажать кнопку отправки
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()