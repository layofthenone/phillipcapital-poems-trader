import buy_sel_request
import connect_mobilg
import reques_data
import account
import time
from selenium import webdriver


def main():
    # login poems
    connect_poems = buy_sel_request.ConnectPoems()
    connect_poems.open_browser()
    connect_poems.login_poems()
    time.sleep(15)
#    connect_poems.accept_the_statement_of_account()
    connect_poems.open_future_contract_tab()

    # send request to phillip
    print("connection completed")
    request = buy_sel_request.SendBuySelRequest("15", "25.12", "eregl")
    request.buy_request()


if __name__ == "__main__":
    main()
"""


"""