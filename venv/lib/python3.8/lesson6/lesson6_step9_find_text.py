from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    input1 = driver.find_element_by_xpath("//input[@placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_xpath("//input[@placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_xpath("//input[@placeholder='Input your email']")
    input3.send_keys("petrov@gmail.com")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    driver.quit()


 #required_elements = driver.find_elements_by_css_selector("input:placeholder")
    #for element in required_elements:
        #.send_keys("required")

# work link for this test
link = "http://suninjuly.github.io/registration1.html"