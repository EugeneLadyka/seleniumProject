from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    find_element = driver.find_element_by_id("input_value").text
    x = find_element

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    answer = calc(x)

    input_answer = driver.find_element_by_class_name("form-control")
    input_answer.send_keys(answer)
    check_box = driver.find_element_by_id("robotCheckbox")
    check_box.click()

    # there we execute JAVA script for scroll the page
    submit_button = driver.find_element_by_css_selector("button.btn")
    driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

    radio_button = driver.find_element_by_id("robotsRule")
    radio_button.click()
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
