from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    elements = driver.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Ronny")

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(20)
    driver.quit()

def test_abs():
    pass