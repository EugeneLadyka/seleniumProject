from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
    # Get accept alert and confirm
    confirm = driver.switch_to.alert
    confirm.accept()

    x_element = driver.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    def_answer = calc(x)

    input_answer = driver.find_element_by_id("answer")
    input_answer.send_keys(def_answer)

    submit_button = driver.find_element_by_css_selector("button.btn")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()