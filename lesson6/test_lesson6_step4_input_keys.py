from selenium import webdriver
import time

link= "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    input1 = driver.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name("form-control.city")
    input3.send_keys("Kyiv")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Ukraine")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 25 секунд
    time.sleep(25)
    driver.quit()

def test_abs2():
    pass


