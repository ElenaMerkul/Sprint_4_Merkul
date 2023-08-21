import allure
import pytest
from pages.order_page import OrderPage
from url import Urls
from data import Registration
from data import PhoneNumber
from data import Date
from data import TextData, RentalData

@pytest.mark.usefixtures("driver")
class TestOrderButton:

    @allure.title('Оформление заказа 1 по кнопке "Заказать" в шапке страницы')
    def test_order1_passed(self, driver):

        order = OrderPage(driver)
        order.open_page(Urls.MAIN_PAGE)
        order.click_order_button_in_header()
        order.filling_form(Registration.fake_person_info(), PhoneNumber.get_phone_number())
        order.wait_for_rent_form()
        order.input_rental_information(Date.get_date_today(), RentalData.RENTAL_DATA_1)
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()

        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title

    @allure.title('Оформление заказа 2 по кнопке "Заказать" в шапке страницы')
    def test_order2_passed(self, driver):

        order = OrderPage(driver)
        order.open_page(Urls.MAIN_PAGE)
        order.click_order_button_in_header()
        order.filling_form(Registration.fake_person_info(), PhoneNumber.get_phone_number())
        order.wait_for_rent_form()
        order.input_rental_information(Date.get_date_tomorrow(), RentalData.RENTAL_DATA_2)
        order.wait_for_confirm()
        order.click_confirmation_order()
        order_title = order.get_new_order_title()
        order.wait_for_order_completed()

        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title