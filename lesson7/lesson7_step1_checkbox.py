from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    x_element = driver.find_element_by_css_selector("#input_value")
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x = x_element.text
    answer = calc(x)

    answer_element = driver.find_element_by_css_selector("#answer")
    answer_element.send_keys(answer)

    check_box = driver.find_element_by_css_selector("#robotCheckbox")
    check_box.click()
    radio_button = driver.find_element_by_css_selector("#robotsRule")
    radio_button.click()
    time.sleep(1)
    submit_button = driver.find_element_by_css_selector("button.btn")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()