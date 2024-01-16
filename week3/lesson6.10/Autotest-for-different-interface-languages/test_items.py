from selenium.webdriver.common.by import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_is_present(browser):
    browser.get(link)
    time.sleep(10)
    card_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert card_button, "Add to cart button is not present"
    