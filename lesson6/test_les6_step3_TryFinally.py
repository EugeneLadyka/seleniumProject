from selenium.webdriver.common.by import By
from selenium import webdriver


link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    button = driver.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    driver.quit()

def test_abs2():
    pass