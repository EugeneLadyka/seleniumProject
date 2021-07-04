from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/wait2.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
        )
    button.click()
    message = driver.find_element_by_id("verify_message")

    assert "Verification was successful!" == message.text


finally:
    driver.quit()