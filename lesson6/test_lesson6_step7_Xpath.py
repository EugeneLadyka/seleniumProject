from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link= "http://suninjuly.github.io/find_xpath_form"

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

    # we can just copy our xpath to element from browser
    button = driver.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 25 секунд
    time.sleep(10)
    driver.quit()

def test_abs():
    pass