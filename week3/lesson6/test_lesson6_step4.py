import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/236895/step/1"
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(10)


    
def test_login_button1():
        button = browser.find_element(By.ID, "ember33")
        button.click()

def test_email_field():
        email = browser.find_element(By.ID, "id_login_email")
        email.send_keys("mikhail.beliakouski@gmail.com")

def test_passwd_field():
        password = browser.find_element(By.ID, "id_login_password")
        password.send_keys("123789456")

def test_login_button2():
        button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader")
        button.click()



        


"""
try: 
    link = "https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.implicitly_wait(10)

    login_button = browser.find_element(By.ID, "ember33")
    login_button.click()

    email = browser.find_element(By.ID, "id_login_email")
    email.send_keys("mikhail.beliakouski@gmail.com")

    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("123789456")

    button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader")
    button.click()

    



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

"""



"""
pytest -s -v test_lesson6_step4.py 
"""