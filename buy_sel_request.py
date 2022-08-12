from connect_mobilg import *
from reques_data import *
import account as acc


class SendBuySelRequest:
    def __int__(self, quantity, price, stock):
        request_data_naming = RequestDataNaming()
        connect_poems = ConnectPoems()

        self.browser = connect_poems.browser
        self.stock = request_data_naming.future_contract_name_create(stock)

        self.quantity = quantity
        self.price = price

    def buy_request(self):
        self.browser.find_element_by_id("ContentSection_txtSozlesme").send_keys(self.stock)  # contract names
        self.browser.find_element_by_id("ContentSection_txtMiktar").send_keys(self.quantity)  # contract quantity
        self.browser.find_element_by_id("ContentSection_ddlFiyat")  # contract price
        self.browser.find_element_by_id("ContentSection_btnAl").click()  # buy request

    def sell_request(self):
        self.browser.find_element_by_id("ContentSection_txtSozlesme").send_keys(self.stock)  # contract names
        self.browser.find_element_by_id("ContentSection_txtMiktar").send_keys(self.quantity)  # contract quantity
        self.browser.find_element_by_id("ContentSection_ddlFiyat")  # contract price
        self.browser.find_element_by_id("ContentSection_btnSat").click()  # sell request

