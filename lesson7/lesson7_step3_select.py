from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    value_attr_1 = driver.find_element_by_id("num1").text
    value_attr_2 = driver.find_element_by_id("num2").text
    x, y = int(value_attr_1), int(value_attr_2)
    def sum(x, y):
        return str(x + y)
    sum_of_value_attr = sum(x, y)

    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_value(sum_of_value_attr)

    submit_button = driver.find_element_by_css_selector("button.btn")
    submit_button.click()

finally:
    time.sleep(5)
    driver.quit()

