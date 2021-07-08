from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    treasure_element = driver.find_element_by_id("treasure")
    treasure_attribute = treasure_element.get_attribute("valuex")
    x = treasure_attribute
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    answer = calc(x)

    answer_element = driver.find_element_by_id("answer")
    answer_element.send_keys(answer)
    checkbox = driver.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio_button = driver.find_element_by_id("robotsRule")
    radio_button.click()
    submit_button = driver.find_element_by_css_selector("button.btn")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()

