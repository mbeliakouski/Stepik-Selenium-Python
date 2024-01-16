import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    print("\nstart browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestLogin():

        @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
    
        def test_message(self, browser, links):
                browser.implicitly_wait(20)
                link =links
                browser.get(link)

  
                login_button1 = browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth")
                login_button1.click()

 
                email = browser.find_element(By.ID, "id_login_email")
                email.send_keys("mikhail.beliakouski@gmail.com")

  
                password = browser.find_element(By.ID, "id_login_password")
                password.send_keys("123789456")


                login_button2 = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader")
                login_button2.click()


                WebDriverWait(browser, 10).until_not(EC.visibility_of_element_located((By.CLASS_NAME, 'box')))

                try:
                        browser.find_element(by="class name", value="again-btn").click()
                except:
                        pass

                input_value = WebDriverWait(browser, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".textarea"))
                        )
                answer = math.log(int(time.time()))
                input_value.send_keys(answer)


                submint_button = WebDriverWait(browser, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
                        )
                submint_button.click()


                value_text =  browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    
                assert "Correct!" == value_text,  f"Answer: {value_text}"



        
    


"""

browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(25)


answer = math.log(int(time.time()+20))


    
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
        time.sleep(20)

def test_input_text():
        input_text = browser.find_element(By.CSS_SELECTOR, ".textarea")
        input_text.send_keys(answer)

def test_submint_button():
        submint_button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        submint_button.click()

def test_corrrect_text():
        value_text = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
        available_text = value_text.text
        print(available_text)
        time.sleep(10)
        
        assert "Correct!" == available_text
"""

"""
pytest -s -v test_lesson6_step5.py
"""