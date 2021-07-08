import unittest
from selenium import webdriver

class TestSuite(unittest.TestCase):

    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"

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

        welcome_text_elt = driver.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test Passed!")


    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"

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

        welcome_text_elt = driver.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test Passed!")

if __name__ == "__main__":
    unittest.main()

def test():
    pass
