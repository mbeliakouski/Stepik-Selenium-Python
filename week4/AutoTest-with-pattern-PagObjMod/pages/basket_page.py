from .base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):

    def should_be_see_basket(self):
        self.should_be_see_empty_basket()
        self.should_be_see_message_empty_basket()

    def should_be_see_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty!!!"

    def should_be_see_message_empty_basket(self):
        message_basket = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET).text
        print(message_basket)
        should_be_message = "Your basket is empty. Continue shopping"
        assert message_basket == should_be_message, "Basket has something else!!!"
