from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    first_name = driver.find_element_by_name("firstname")
    first_name.send_keys("Ivan")
    second_name = driver.find_element_by_name("lastname")
    second_name.send_keys("Petrov")
    input_email = driver.find_element_by_name("email")
    input_email.send_keys("qman@gmail.com")

    # from os we get to python lesson7 folder and then get the file.txt
    element = driver.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Python.txt')
    element.send_keys(file_path)

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    driver.quit()