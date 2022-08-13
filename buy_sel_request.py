from connect_mobilg import *
from reques_data import *
import account as acc


class SendBuySelRequest:

    def __init__(self, stock, quantity, price):

        self.browser = ConnectPoems().browser

        self.future_stock = RequestDataNaming().future_contract_name_create(stock)
        self.quantity = quantity
        self.price = price

    def buy_request(self):
        self.browser.find_element("id", "ContentSection_txtSozlesme").send_keys(self.future_stock)  # contract names
        self.browser.find_element("id", "ContentSection_txtMiktar").send_keys(self.quantity)  # contract quantity
        self.browser.find_element("id", "ContentSection_ddlFiyat")  # contract price

        self.browser.find_element("id", "ContentSection_btnAl").click()  # buy request

    def sell_request(self):
        self.browser.find_element("id", "ContentSection_txtSozlesme").send_keys(self.future_stock)  # contract names
        self.browser.find_element("id", "ContentSection_txtMiktar").send_keys(self.quantity)  # contract quantity
        self.browser.find_element("id", "ContentSection_ddlFiyat")  # contract price

        self.browser.find_element("id", "ContentSection_btnSat").click()  # sell request
