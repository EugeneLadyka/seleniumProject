from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    new_window = driver.window_handles[1]
    first_window = driver.window_handles[0]
    driver.switch_to.window(new_window)

    x_element = driver.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    def_answer = calc(x)

    answer = driver.find_element_by_id("answer")
    answer.send_keys(def_answer)

    submit_button = driver.find_element_by_css_selector("button.btn")
    submit_button.click()

finally:
    time.sleep(15)
    driver.quit()