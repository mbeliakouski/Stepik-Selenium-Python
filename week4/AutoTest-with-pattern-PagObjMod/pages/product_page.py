from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_product_to_basket(self):
        self.should_be_basket_button()
        self.should_be_click_basket()
        self.should_be_find_value()
        self.should_be_name_book()
        self.should_be_name_book_add_to_basket()
        self.should_be_basket_total()
        self.should_be_cost_book()


    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button not found"

    def should_be_click_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_basket.click()

    def should_be_find_value(self):
        self.solve_quiz_and_get_code()


    def should_be_name_book(self):
        name_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        print(name_book)
        check_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK_ADDET_TO_BASKET).text
        print(check_name)
        assert check_name == name_book, "Name book is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_BOOK_ADDET_TO_BASKET), \
            "Success message is presented, but should not be"
        
    def should_be_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_BOOK_ADDET_TO_BASKET), \
            "A message stating that the element is disappearing, but should not be"

    def should_be_name_book_add_to_basket(self):
        name_book_add_basket = self.browser.find_element(*ProductPageLocators.NAME_BOOK_ADDET_TO_BASKET).text
        print(name_book_add_basket)
        check_name_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert check_name_book == name_book_add_basket, "Name book in basket is wrong"

    def should_be_basket_total(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        print(basket_total)
        check_basket_total = self.browser.find_element(*ProductPageLocators.COST_BOOK).text
        assert basket_total == check_basket_total, "Basket total is wrong"

    def should_be_cost_book(self):
        cost_book = self.browser.find_element(*ProductPageLocators.COST_BOOK).text
        print(cost_book)
        check_cost_book = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert cost_book == check_cost_book, "Cost book is wrong"
        