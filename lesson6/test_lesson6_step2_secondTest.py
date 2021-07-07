from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/simple_form_find_task.html")
button = driver.find_element_by_id("submit_button")

# закрываем браузер после всех манипуляций
driver.quit()

def test_abs2():
    pass