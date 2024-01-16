import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class TestRegistal(unittest.TestCase):
    def test_registration1(self):

        browser = webdriver.Chrome()
        link = "https://suninjuly.github.io/registration1.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class .form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class .form-control.second")
        last_name.send_keys("Ivanov")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class .form-control.third")
        email.send_keys("Ivan@Ivanov.com")


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(10)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

        #Ожидаемый результат
        expected_welcome_text = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text, expected_welcome_text, "Should be absolute value of a number")    

    def test_registration2(self):

        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

            # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class .form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class .form-control.second")
        last_name.send_keys("Ivanov")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class .form-control.third")
        email.send_keys("Ivan@Ivanov.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

        #Ожидаемый результат
        expected_welcome_text = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text, expected_welcome_text, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()
