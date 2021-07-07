from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    driver =webdriver.Chrome()
    driver.get(link)
    textlink = driver.find_element_by_link_text("224592")
    textlink.click()

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
    time.sleep(20)
    driver.quit()

def test_abs():
    pass