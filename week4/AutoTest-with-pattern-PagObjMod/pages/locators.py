from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group .btn.btn-default:nth-child(1)")


class LoginPageLocators():
    REGISER_FORM = (By.CSS_SELECTOR,"form#register_form.well")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")
    EMAIL = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    PASSWD = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    CONFR_PASSWD = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button.btn")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    NAME_BOOK_ADDET_TO_BASKET = (By.CSS_SELECTOR,".alert-safe:nth-of-type(1) .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    COST_BOOK = (By.CSS_SELECTOR, 'p.price_color')
    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_BASKET = (By.TAG_NAME, "p")