from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


link ="http://suninjuly.github.io/explicit_wait2.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    button = driver.find_element_by_id("book")
    element = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    button.click()

    #alert_ok = driver.switch_to.alert
    #alert_ok.accept()

    submit_button = driver.find_element_by_id("solve")
    driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

    #time.sleep(1)
    find_element = driver.find_element_by_id("input_value")
    x = find_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    answer = calc(x)

    input_answer = driver.find_element_by_id("answer")
    input_answer.send_keys(answer)

    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()