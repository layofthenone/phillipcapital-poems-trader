from connect_mobilg import *
import account as acc


class SendBuySelRequest:
    def __int__(self, quantity, price, stock):
        connect_poems = ConnectPoems()
        self.browser = connect_poems.browser

        self.quantity = quantity
        self.price = price

    def buy_request(self):
        pass

    def sell_request(self):
        pass
